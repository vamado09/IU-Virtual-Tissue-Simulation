import os
from langchain_community.document_loaders import DirectoryLoader
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
import requests


class Generator:
    def __init__(self, input_dir, output_dir, model=None):
        if not os.path.exists(input_dir) or not os.path.isdir(input_dir):
            raise FileNotFoundError(f"The path '{input_dir}' does not exist or is not a directory.")

        if not os.path.exists(output_dir):
            os.mkdir(output_dir)
            print(f"Output Directory '{output_dir}' created successfully.")

        self.input_dir = input_dir
        self.output_dir = output_dir
        self.docs = None
        self.db = None
        self.embeddings = OpenAIEmbeddings()
        if model:
            self.model = model
        else:
            self.model = ChatOpenAI(
                temperature=0,
                model_name="gpt-3.5-turbo"
            )

    def scrape(self, url: str, file_name: str):
        """
        Function to scrape website and write HTML content to an HTML file.
        File will be saved in the object's input directory.
        :param url: website to scrape
        :param file_name: name of file HTML will be saved as in the input directory
        """
        response = requests.get(url)

        # Check if the request was successful
        if response.status_code == 200:
            # Get the HTML content
            html_content = response.text

            file_path = os.path.join(self.input_dir, f"{file_name}.html")

            # Save the HTML content to a file
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(html_content)
            print(f"HTML content saved in {file_path}")
        else:
            print(f"Failed to fetch HTML content from {url}")

    def read_md(self, ignore=False):
        """
        Load markdown files in input directory
        :param ignore: If True will ignore errors when loading files
        """
        if ignore:
            loader = DirectoryLoader(self.input_dir, glob="**/*.md", silent_errors=True)
        else:
            loader = DirectoryLoader(self.input_dir, glob="**/*.md")
        docs = loader.load()
        print(f"You have {len(docs)} documents.")
        self.docs = docs

    def read_txt(self, ignore=False):
        """
        Load txt files in input directory
        :param ignore: If True will ignore errors when loading files
        """
        if ignore:
            loader = DirectoryLoader(self.input_dir, glob="**/*.txt", silent_errors=True)
        else:
            loader = DirectoryLoader(self.input_dir, glob="**/*.txt")
        docs = loader.load()
        print(f"You have {len(docs)} documents.")
        self.docs = docs

    def read_html(self, ignore=False):
        """
        Load HTML files in input directory
        :param ignore: If True will ignore errors when loading files
        """
        if ignore:
            loader = DirectoryLoader(self.input_dir, glob="**/*.html", silent_errors=True)
        else:
            loader = DirectoryLoader(self.input_dir, glob="**/*.html")
        docs = loader.load()
        print(f"You have {len(docs)} documents.")
        self.docs = docs

    def read_all(self, ignore=False):
        """
        Load all file types in input directory
        :param ignore: If True will ignore errors when loading files
        """
        if ignore:
            loader = DirectoryLoader(self.input_dir, silent_errors=True)
        else:
            loader = DirectoryLoader(self.input_dir)
        docs = loader.load()
        print(f"You have {len(docs)} documents.")
        self.docs = docs

    def chunk_docs(self, chunk_size: int, overlap: int, separator: str = None):
        """
        Chunk your loaded documents
        :param chunk_size: No. characters in chunk
        :param overlap: Overlap between chunks
        :param separator: Character to be used for separating chunks
        """
        if separator:
            text_splitter = RecursiveCharacterTextSplitter(
                chunk_size=chunk_size,
                chunk_overlap=overlap,
                separator=separator
            )
        else:
            text_splitter = RecursiveCharacterTextSplitter(
                chunk_size=chunk_size,
                chunk_overlap=overlap
            )
        self.docs = text_splitter.split_documents(self.docs)

    def ingest_db(self, db: str = None):
        """
        Ingest vector store with vector embeddings from loaded docs.
        :param db: Name of existing db if any, otherwise defaults to None
        """
        if not db:
            self.db = FAISS.from_documents(self.docs, self.embeddings)
        else:
            db_temp = FAISS.from_documents(self.docs, self.embeddings)
            self.load_db(db)
            self.db.merge_from(db_temp)

    def query_vs(self, query: str):
        """
        :param query: Query to run with the vector store
        :return: Content of most similar doc
        """
        docs = self.db.similarity_search(query)
        return docs[0].page_content

    def save_db(self, name: str):
        """
        :param name: name to save db as
        """
        self.db.save_local(name)

    def load_db(self, name: str):
        """
        :param name: name of existing db
        """
        self.db = FAISS.load_local(name, self.embeddings)

    def create_ko(self, template, topic):
        """
        Function to generate KO .md files
        :param template: Prompt template used for generating output
        :param topic: The topic of the KO (e.g., Morpheus)
        """
        retriever = self.db.as_retriever()
        prompt = ChatPromptTemplate.from_template(template)
        chain = (
                {"context": retriever, "topic": RunnablePassthrough()}
                | prompt
                | self.model
                | StrOutputParser()
        )

        result = chain.invoke(topic)

        output_path = os.path.join(self.output_dir, f"{topic}.md")

        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(result)
