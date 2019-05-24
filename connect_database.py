import os
import pymongo

def connect_mongo():
    MONGO_URI = os.getenv('MONGO_URI')
    DB_NAME = os.getenv('DB_NAME')
    mongo_client = pymongo.MongoClient(MONGO_URI)
    db = mongo_client[str(DB_NAME)]
    return db

def save_number(phone_number):
    db = connect_mongo()
    numbers = db["numbers"]
    numbers.insert({"number":phone_number})

def get_lifemap(phone_number):
    db = connect_mongo()
    familyCol = db['family']
    family = familyCol.find_one({'phoneNumber': phone_number}) # .Family needs to be the name of the collection where the families are loaded
    if family :
        print(family)
        if 'lifemapPdf' in family:
            print(family['lifemapPdf'])
            # ** send_lifemapPdf(family['lifemapPdf']) #this function has to be the one that sends the pdf to the WA
        else:
            # ** pdf=generatepdf(family)
            # ** saves the pdf generated file in blob to save it in the db
            familyCol.update_one({'phoneNumber': phone_number}, {'$set': {'lifemapPdf' : 'pdf'}})
    else:
        return "The family is not in the database" #the function sends a message that the number is not in the database and should be checked
