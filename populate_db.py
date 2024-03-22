from dotenv import load_dotenv
from ko_generation import Generator
import sys
import os
import requests


def drive(generator, db_name, db_save_name):

    # scrape websites in urls.txt
    if os.path.exists('urls.txt'):
        with open('urls.txt', 'r') as f:
            for url in f:
                try:
                    gen.scrape(url, file_name=url[:10])
                except requests.exceptions.MissingSchema:
                    print(f'Add schema (http or https) to {url}')

    generator.read_all(ignore=True)

    generator.chunk_docs(chunk_size=1000, overlap=200)

    generator.ingest_db(db=db_name)

    generator.save_db(name=db_save_name)


if __name__ == "__main__":
    load_dotenv()

    input_dir = sys.argv[1]
    if len(sys.argv) == 3:
        db = sys.argv[2]
        db_save = sys.argv[2]
    else:
        db = None
        db_save = input("How would you like to save the vector store as? ")

    gen = Generator(input_dir, 'knowledge_objects')

    drive(
        generator=gen,
        db_name=db,
        db_save_name=db_save
    )
