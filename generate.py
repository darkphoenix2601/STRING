import os
os.system("pip install dnspython")
os.system("pip  install pymongo[srv]")
from cryptography.fernet import Fernet
from pymongo import MongoClient
from pymongo.errors import ConfigurationError
from pyrogram import Client
os.system("clear")
try:

 api_id = int(input("Input App Id, Do not steal!\n:"))
 hash = input("Input Api Hash, Do not steal!\n:")
except BaseException:
  print("Either Correct App ID")
  exit(1)
app = Client("string",api_id,hash)

def encrypt(message: bytes, key: bytes) -> bytes:
    return Fernet(key).encrypt(message)


mongo = input("Enter Your Mongo DB Url\n: ")


app.storage.SESSION_STRING_FORMAT=">B?256sQ?" 


with app:

  # with app:
   string = app.export_session_string()
   kek = Fernet.generate_key()
   client =  MongoClient(mongo)
   db = client['VisionEncryption']
   db = db['string_db']
   db.insert_one({'tk': kek.decode()})
   encryped = encrypt(string.encode(),kek )
   app.send_message("me", f"**Here's Your String**\n\n`{encryped.decode()}`\n\n**Contact @VisionTalks for help**",parse_mode="markdown")
