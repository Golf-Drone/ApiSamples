from openai import OpenAI
from dotenv import load_dotenv
import os
import sys

load_dotenv()
api_key=os.getenv("OPEN_AI_KEY")
if api_key == None:
    print("You must create a .env file in the project root folder that contains a value for OPEN_AI_KEY")
    sys.exit()

client = OpenAI(
    api_key=api_key
)

completion = client.chat.completions.create(
    model="gpt-3.5-turbo-0125",
    messages=[
        {"role": "system", "content": "You are a famous country and western singer"},
        {"role": "user", "content": "Compose a song about how much you love custard"}
    ]
)

print(completion.choices[0].message)

# response = client.chat.completions.create(
#     model="gpt-4o-mini",
#     messages=[
#         {
#             "role": "user",
#             "content": [
#                 {"type": "text", "text": "could you guess how many people are wearing glasses?"},
#                 {
#                     "type": "image_url",
#                     "image_url": {
#                         "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/8e/Batsheva_theater_crowd_in_Tel_Aviv_by_David_Shankbone.jpg/2880px-Batsheva_theater_crowd_in_Tel_Aviv_by_David_Shankbone.jpg",
#                     },
#                 },
#             ],
#         }
#     ],
#     max_tokens=300,
# )
#
# print(response.choices[0])