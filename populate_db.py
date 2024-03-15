from dotenv import load_dotenv
from ko_generation import Generator
import sys


def drive(generator, file_type, db_name, db_save_name):
    if file_type not in ['all', 'md', 'pdf', 'txt', 'html']:
        raise ValueError("File Type not supported. File type must be one of ['all', 'md', 'pdf', 'txt', 'html']")

    elif file_type == 'md':
        generator.read_md()

    elif file_type == 'pdf':
        generator.read_pdf()

    elif file_type == 'txt':
        generator.read_txt()

    elif file_type == 'html':
        generator.read_md()

    else:
        generator.read_all()

    generator.chunk_docs(chunk_size=1000, overlap=200)

    generator.ingest_db(db=db_name)

    generator.save_db(name=db_save_name)


if __name__ == "__main__":
    load_dotenv()

    input_dir = sys.argv[1]
    file = sys.argv[2]
    if len(sys.argv) == 4:
        db = sys.argv[4]
        db_save = sys.argv[4]
    else:
        db = None
        db_save = input("How would you like to save the vector store as? ")

    gen = Generator(input_dir, 'knowledge_objects')

    drive(
        generator=gen,
        file_type=file,
        db_name=db,
        db_save_name=db_save
    )
