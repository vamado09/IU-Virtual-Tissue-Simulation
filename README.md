## Objective
The main goal is to create a Knowledge Object Generator class to simplify and streamline the process of generating
knowledge objects for the purpose of our searchable encyclopedia; this class would incorporate RAG and LLMs to
automate the creation of markdown knowledge object files which can be easily integrated with our web application.

## Notes
Currently, scripts generate_ko and populate_db are still a work in progress, would recommend starting out with a
notebook and importing the Generator class to get familiar with it, or playing around with the provided scripts 
(e.g., using different templates, chunk sizes, etc.)

If you do decide to import it and play around with it just make sure that you have the .env file set up as shown below 
and run this in your notebook:

```python 
from dotenv import load_dotenv

load_dotenv()
```

## Getting started

1. First install the required packages

    ```pip install -r requirements.txt```


2. Create a .env file in the same directory


3. In .env store your OpenAI API key as OPENAI_API_KEY

    `OPENAI_API_KEY=<your API key>`

## Scripts

### ko_generation.py 
This contains the Generator class used for processes in loading input files, create vector embeddings, 
and create Knowledge Objects (KOs).

### populate_db.py
This script uses the Generator class to create a vector store, from your input files, to be used by the LLM for KO 
generation.

Run through command line using:

```
python populate_db.py <name of input directory> <file type> <optional: name of existing db>
```

Arguments:
- name of input directory - name of directory holding the files you want to load


- file type - type of file you want to load
  - Currently, must be one of md, txt, html, or all if you want to load all of these file types
  - Other file types will soon be added


- Name of existing db, if any. This argument is optional; if you do not have an existing db (vector store), just pass in
the other 2 arguments, and you will be asked to input how to save the db as.



### generate_ko.py

Once you have an existing vector store, you can use this script to generate a markdown KO on a given subject. The KO
will be saved as a markdown file in a directory called **knowledge_objects**.

Run through command line using:

```
python generate_ko.py <db name> <subject of KO>
```

Arguments:

- db name: name of your vector store
- subject of KO: topic for KO (e.g., Morpheus)