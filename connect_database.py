import os
import pymongo
import pdfkit

def connect_mongo():
    MONGO_URI = os.getenv('MONGO_URI')
    DB_NAME = os.getenv('DB_NAME')
    mongo_client = pymongo.MongoClient(MONGO_URI)
    db = mongo_client[str(DB_NAME)]
    return db

def generate_pdf(family):
    filename = "out4.py"
    pdfkit.from_url("http://127.0.0.1:5000/render-template", filename, options={"javascript-delay":2000})
    return filename

def get_lifemap(phone_number):
    db = connect_mongo()
    familyCol = db['family']
    family = familyCol.find_one({'phoneNumber': phone_number}) # .Family needs to be the name of the collection where the familys are loaded
    if family :
        print(family)
        # if 'lifeMap' in family: 
        #     print(family['lifeMap'])
        #  ** send_lifemap(family['lifeMap']) #this function has to be the one that sends the pdf to the WA
    # else:
            # ** pdf=generatepdf(family)
            # ** saves the pdf generated file in blob to save it in the db 
        filename = generate_pdf('family')
        return filename
        # familyCol.update_one({'phoneNumber': phone_number},{'$set': {'lifeMap' : 'pdf'}}) 
    else:
        return "The famiy is not in the database" #the function sends a message that the number is not in the database and should be checked
