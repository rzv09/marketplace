from flask import Flask
from flask_pymongo import PyMongo
from pymongo import MongoClient


uri = "mongodb://ac-ofbreqq-shard-00-00.zqp0xzh.mongodb.net:27017,ac-ofbreqq-shard-00-01.zqp0xzh.mongodb.net:27017,ac-ofbreqq-shard-00-02.zqp0xzh.mongodb.net:27017/?ssl=true&replicaSet=atlas-4i6we9-shard-0&authSource=%24external&authMechanism=MONGODB-X509&retryWrites=true&w=majority"
certificate_path = "X509-cert-1318022604136865598.pem"

client = MongoClient(uri,
                     tls=True,
                     tlsCertificateKeyFile=certificate_path)

# print(client.server_info())

db = client['Marketplace']
print(db)
# collection = db['Products']
# doc_count = collection.count_documents({})
# print(doc_count)

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://ac-ofbreqq-shard-00-00.zqp0xzh.mongodb.net:27017,ac-ofbreqq-shard-00-01.zqp0xzh.mongodb.net:27017,ac-ofbreqq-shard-00-02.zqp0xzh.mongodb.net:27017/?ssl=true&replicaSet=atlas-4i6we9-shard-0&authSource=%24external&authMechanism=MONGODB-X509&retryWrites=true&w=majority"

# mongo = PyMongo(app)

@app.route("/Products")
def ret():
    collection = db["Products"]
    doc_count = collection.count_documents({})
    print(doc_count)

    return "<h1>" + str(doc_count) + "</h1>"

@app.route("/members")
def members():
    return {"members": ["Member1", "Member2", "Member3"]}


@app.route("/users")
def users():
    user_collection = mongo.db.users
    user_collection.insert({
        'name': 'Raman'
    })
    return "<h1>Added a User</h1>"


if __name__=="__main__":
    # create_app()
    app.run(debug=True)
