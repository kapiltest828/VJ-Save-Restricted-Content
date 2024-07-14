import os

#Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

#Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "20116095"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "3ed1ce1f57b104b5cbefebacc8c47e97")

#Database 
DB_URI = os.environ.get("DB_URI", "mongodb+srv://sachin0274936:chalubhaichecking@cluster0.q2sjjxz.mongodb.net/?retryWrites=true&w=majority")
