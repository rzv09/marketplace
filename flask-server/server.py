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

@app.route("/")
def home():
    return "<h1>Welcome to RIT's Student Marketplace</h1>\n<p>(not affiliated with Meta in any way)</p>\n"

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

@app.route("/users/<name>")
def get_user(name=None):
    if name is None:
        return get_users()
    return routes.get_topic('name', name)


@app.route("/all")
def get_all():
    return routes.get_all_data()
    

if __name__=="__main__":
    app.run(debug=True)
