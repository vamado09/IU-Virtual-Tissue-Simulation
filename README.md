## Objective
The main goal is to create a Knowledge Object Generator class to simplify and streamline the process of generating
knowledge objects for the purpose of our searchable encyclopedia; this class would incorporate RAG and LLMs to
automate the creation of markdown knowledge object files which can be easily integrated with our web application.

## Getting started

1. First install the required packages

    ```pip install -r requirements.txt```


2. Create a .env file in the same directory


3. In .env store your OpenAI API key as OPENAI_API_KEY

    `OPENAI_API_KEY=<your API key>`


4. In the same directory, create/edit 'template.txt' which contains your knowledge object template. 
An example template is provided


5. If wanting to scrape urls, create a 'urls.txt' file which lists the urls, line by line


6. Create a subdirectory containing the source files you want to load. Currently, supports pdf, txt, html, and md


7. Run main.py as specified below

## Scripts
### main.py
This is the script encompassing the entire workflow for generating knowledge objects (
using the generator class from ko_generation.py); you can load source documents to create a vector embeddings db,
load/save a vector embeddings db, and finally generate a knowledge object markdown file.

#### How to run
To run this script, use the following command in your command line - arguments are explained further below:

```
python main.py <input_dir> <topic> <loading> <deserialize> <optional: existing_db>
```

#### Examples:
```
python main.py docs Morpheus true false
```


Note that we can also have multiple subjects, separated by a single comma (no spaces):
```
python main.py docs Morpheus,Chaste true false
```

or in the case your subject contains multiple words

```
python main.py docs "Morpheus,Tissue Forge" true false
```


##### Arguments:
1. input_dir: name of input directory that stores the files you wish to load
2. topic: subject of your knowledge object
3. loading: whether you want to load new documents - True or False
4. deserialize: whether you want to allow for deserialization when loading a db - True or False
5. existing_db: Optional - the name of your existing embeddings db, if any

- Tip: if not loading any new documents, use "knowledge_objects" as your input directory


### ko_generation.py 
This contains the Generator class used for processes in loading input files, creating vector embeddings, 
and creating Knowledge Objects (KOs).
