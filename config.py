#!/usr/bin/env python3


### Importing
from os import environ

class Config(object):
    TG_BOT_TOKEN = environ.get("BOT_TOKEN", "5989031691:AAFVsArCLMljqRf1ABbSNcQMV5FCe-dMlZE") # Make a bot from https://t.me/BotFather and enter the token here
    
    APP_ID = int(environ.get("API_ID", "9544521")) # Get this value from https://my.telegram.org/apps
    
    API_HASH = environ.get("API_HASH", "5cf32e97dc94510e46524f2286c95116") # Get this value from https://my.telegram.org/apps
    
    OWNER_ID = int(environ.get("OWNER_ID", "1358657527")) # Your(owner's) telegram id
    
    MONGO_STR = environ.get("MONGO_STR", "mongodb+srv://test:test@cluster0.09gee3a.mongodb.net/?retryWrites=true&w=majority") # Get from MongoDB Atlas

    DOWNLOAD_LOCATION = "app//DOWNLOADS//" # The download location for users. (Don't change anything in this field!)

    
