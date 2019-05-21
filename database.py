from pymongo import MongoClient
#this needs to be changed for the actual mongo string
client = MongoClient('mongodb+srv://LifeMap:helloworld@cluster0-6nhz3.mongodb.net/test?retryWrites=true')
#putting the name of the database in mongo here
db=client.PovertyStopLight
def query_db(phone_number):
    # .Family needs to be the name of the collection where the registers are loaded
    register= db.Family.find_one({'phoneNumber': phone_number})
    print(register)
    if 'lifeMap' in register: 
       send_lifemap(register['lifeMap']) #this function has to be the one that sends the pdf to the WA

    else:
        pdf=generatepdf()
        #saves the pdf generated file in blob to save it in the db 
        register1=db.Family.update_one({'phoneNumber': phone_number},{'$set': {'lifeMap' : pdf}}) 
