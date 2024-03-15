from dotenv import load_dotenv
from ko_generation import Generator
import sys
import os

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

    if not os.path.exists('knowledge_objects'):
        os.mkdir('knowledge_objects')

    db_name = sys.argv[1]
    topic = sys.argv[2]

    generator = Generator('knowledge_objects', 'knowledge_objects')

    if len(sys.argv) == 4 and sys.argv[3].lower() == 'true':
        generator.load_db(db_name, allow_deserialization=True)

    else:
        generator.load_db(db_name)

    generator.create_ko(template=template, topic=topic)
