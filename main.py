from dotenv import load_dotenv
from ko_generation import Generator
import sys
import os
import requests


class NoExistingDBError(Exception):
    pass


def main(inputs_dir: str, context: str, subjects: list, load_docs: bool, db_name: str = None):

    # initiate generator instance
    gen = Generator(inputs_dir, 'knowledge_objects')

    if not load_docs and not db_name:
        raise NoExistingDBError('If not loading docs, must pass an existing vector store.')

    # if the user wants to load input documents
    elif load_docs:

        # scrape websites in urls.txt and create html files
        if os.path.exists(os.path.join(inputs_dir, 'urls.txt')):
            with open(os.path.join(inputs_dir, 'urls.txt'), 'r') as f:
                for line in f:
                    url, file_name = line.strip().split()[0], line.strip().split()[1]
                    try:
                        gen.scrape(url, file_name=file_name)
                    except requests.exceptions.MissingSchema:
                        print(f'Add schema (http or https) to {url}')
                    except requests.exceptions.HTTPError as e:
                        print(f'HTTP Error: {e}')

        # load all supported input documents
        gen.read_all(ignore=True)

        # raise error
        if len(gen.docs) == 0:
            raise ValueError(f"There are no valid input documents in directory {inputs_dir}")

        gen.chunk_docs(chunk_size=1000, overlap=200)

        # if there is an existing db to add to make sure to load it
        if db_name:
            gen.ingest_db(db=db_name)
        else:
            gen.ingest_db()

        save_name = input('How would you like to save the vector DB as? If not saving, simply press Enter')
        if len(save_name) > 0:
            gen.save_db(save_name)

    else:
        gen.load_db(db_name)

    for subject in subjects:
        gen.create_ko(template=context, topic=subject)


if __name__ == "__main__":
    load_dotenv()

    input_dir = sys.argv[1]
    topics = sys.argv[2].split(",")
    if sys.argv[3].lower() == 'true':
        loading = True
    else:
        loading = False

    if len(sys.argv) == 5:
        existing_db = sys.argv[4]
    else:
        existing_db = None

    path_to_template = 'template.txt'

    if not os.path.exists(path_to_template):
        raise FileNotFoundError(f"The path '{input_dir}' does not contain template.txt file.")

    with open(path_to_template, 'r') as t:
        template = t.read()

    main(input_dir, context=template, subjects=topics, load_docs=loading, db_name=existing_db)

# for running the script:

# 1. if you want to scrape multiple urls, add file "urls.txt" to inputs directory.
# This file should on each line have the url, then a space, and then the html file name
# It will look like this:
# <url1> <how you would like to save the html as>
# <url2> <how you would like to save the html as>
# ...
# example line in the text file:
# https://github.com/vamado09/IU-Virtual-Tissue-Simulation github_repo
# file will be saved as github_repo.html in inputs directory

# 2. Have a template.txt file in the same directory as this script containing the template you want to use

# 3. If you want to create KOs for different topics:
# pass in the different topics as an argument separated with a comma.
# Example: Morpheus,Chaste,Artistoo
# Todo: see how it would work when the topic is two different words (e.g., Tissue Forge)
# I think it would have to be passed in as "Tissue Forge" or "Morpheus,Tissue Forge" if using multiple topics

# to run the script the command would look something like:
# python main.py <input dir> <topic(s) for KOs> <loading input docs (true or false)> <optional: existing db name>
# Example:
# python main.py inputs Morpheus,Artistoo True
