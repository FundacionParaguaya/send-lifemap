from pymongo import MongoClient
#this needs to be changed for the actual mongo string
client = MongoClient('mongodb+srv://LifeMap:helloworld@cluster0-6nhz3.mongodb.net/test?retryWrites=true')
#putting the name of the database in mongo here
db=client.PovertyStopLight

def query_db(phone_number):
    register= db.Family.find_one({'phoneNumber': phone_number}) # .Family needs to be the name of the collection where the registers are loaded
    if register :
        print(register)
        if 'lifeMap' in register: 
            print(register['lifeMap'])
            send_lifemap(register['lifeMap']) #this function has to be the one that sends the pdf to the WA
        else:
            pdf=generatepdf(register)
            #saves the pdf generated file in blob to save it in the db 
            register1=db.Family.update_one({'phoneNumber': phone_number},{'$set': {'lifeMap' : pdf}}) 
    else:
        send_not_in_db_message() #the function sends a message that the number is not in the database and should be checked
        print("error")

