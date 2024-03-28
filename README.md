## Generating Knowledge Objects Using RAG with LangChain
The main goal of this project is to create knowledge objects based on the source documents and/or a list of URLs using Retrieval-Augmented Generation (RAG) with LangChain.

The Generator class is based on the [LangChain's RAG documentation](https://python.langchain.com/docs/expression_language/cookbook/retrieval) and it streamlines and automates the process of generating
knowledge objects for the purpose of our searchable encyclopedia; the generated knowledge object files are in the markdown format which can be easily integrated with our web application.



## Requirements
1. OpenAI API key: [https://platform.openai.com/api-keys](https://platform.openai.com/api-keys). OpenAI offers a promotional credit which expires after about 2 months. If this is the case, an account with at least Tier 1 might be needed: [https://platform.openai.com/account/limits](https://platform.openai.com/account/limits)

2. Python 3 installed



## Usage

1. First install the required packages:

    ```
    pip install -r requirements.txt
    ```

2. Create a `.env` file in the same directory:


3. In `.env` store your OpenAI API key as `OPENAI_API_KEY`:

    ```
    OPENAI_API_KEY=<your API key>
    ```


4. In the same directory, create/edit `template.txt` which contains your knowledge object template. 
An example template file is provided.


5. If wanting to scrape URLs, create a `urls.txt` file which lists the URLs, line by line.


6. Create a subdirectory containing the source files you want to load. Currently, pdf, txt, html, and md are supported.


7. Run `main.py` as specified:
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
#### Arguments:
  1. input_dir: name of input directory that stores the files you wish to load
  2. topic: subject of your knowledge object
  3. loading: whether you want to load new documents - True or False
  4. deserialize: whether you want to allow for deserialization when loading a db - True or False
  5. existing_db: Optional - the name of your existing embeddings db, if any
- Tip: if not loading any new documents, use "knowledge_objects" as your input directory



## Scripts
### main.py
This is the script encompassing the entire workflow for generating knowledge objects (using the Generator class from `ko_generator.py`); you can load source documents to create a vector embeddings db,
load/save a vector embeddings db, and finally generate a knowledge object markdown file.


### ko_generator.py 
This contains the Generator class used for processes in loading input files, creating vector embeddings, 
and creating Knowledge Objects (KOs).


## Contributors
- [@dani-dr06](https://github.com/dani-dr06)
- [@vamado09](https://github.com/vamado09)
- [@martinbreth](https://github.com/martinbreth)