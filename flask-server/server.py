from flask import Flask
from pymongo import MongoClient
from datetime import datetime
import auth
import routes


client = MongoClient(auth.URI,
                     tls=True,
                     tlsCertificateKeyFile=auth.CERT_PATH)

database = client['Marketplace']

routes.__init__(database)

app = Flask(__name__)

@app.route("/products")
def get_products():
    print(datetime.utcnow())
    return routes.get_products()


@app.route("/members")
def members():
    collection = database["Users"]
    print(collection)
    return {"members": ["Member1", "Member2", "Member3"]}


@app.route("/users")
def get_users():
    return routes.get_users()
    


if __name__=="__main__":
    app.run(debug=True)
