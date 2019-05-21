import configparser
import pymongo

config_file = "config/db.ini"
parser = configparser.ConfigParser()
parser.read(config_file)

def connect_mongo():
    mongodb_dbname = parser.get('povstop','dbname')
    mongodb_user = parser.get('povstop','dbuser')
    mongodb_dbpass = parser.get('povstop', 'dbpass')
    mongodb_host = parser.get('povstop', 'dbhost')
    mongo_client = pymongo.MongoClient('mongodb+srv://'+ str(mongodb_user) +':' + str(mongodb_dbpass) + '@'+ str(mongodb_host)+'/' +str(mongodb_dbname)+'?retryWrites=true')
    db = mongo_client[str(mongodb_dbname)]
    return db