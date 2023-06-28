import os
# from dotenv import load_dotenv

# load_dotenv()

os.environ["MODE"] = "TEST"

print(os.getenv('MODE'))
