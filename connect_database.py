import os
import configparser
import pymongo

config_file = "config/db.ini"
parser = configparser.ConfigParser()
parser.read(config_file)

def connect_mongo():
    MONGO_URI = os.environ('MONGO_URI')
    DB_NAME = os.environ('DB_NAME')
    mongo_client = pymongo.MongoClient(MONGO_URI)
    db = mongo_client[str(DB_NAME)]
    return db


def get_lifemap(phone_number):
    db = connect_mongo()
    familyCol = db['family']
    family = familyCol.find_one({'phoneNumber': phone_number}) # .Family needs to be the name of the collection where the familys are loaded
    if family :
        print(family)
        if 'lifeMap' in family: 
            print(family['lifeMap'])
            # ** send_lifemap(family['lifeMap']) #this function has to be the one that sends the pdf to the WA
        else:
            # ** pdf=generatepdf(family)
            # ** saves the pdf generated file in blob to save it in the db 
            familyCol.update_one({'phoneNumber': phone_number},{'$set': {'lifeMap' : 'pdf'}}) 
    else:
        return "The famiy is not in the database" #the function sends a message that the number is not in the database and should be checked