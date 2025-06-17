from dotenv import load_dotenv
from service import run

load_dotenv()

res = run()

print(res)
