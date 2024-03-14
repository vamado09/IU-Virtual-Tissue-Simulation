from dotenv import load_dotenv
from ko_generation import Generator
import sys

if __name__ == "__main__":
    load_dotenv()

    template = """Create a knowledge object based only on the following context:
    {context}

    Create a knowledge object about {topic} containing these sections and format it into a markdown 
    (each section should be header 2):

    - What Is {topic}
    - Who Should Use {topic}
    - When Should I Use {topic}
    - How Do I Learn About {topic}
    - Strengths
    - Limitations
    - Alternative Options
    - Example Deployments
    - References
    """

    db_name = sys.argv[1]
    topic = sys.argv[2]

    generator = Generator('inputs', 'knowledge_objects')
    generator.load_db(db_name)
    generator.create_ko(template=template, topic=topic)
