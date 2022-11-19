from datetime import datetime

database = None

def __init__(db):
    global database
    database = db


def get_products():
    collection = database["Products"]
    doc_count = collection.count_documents({})
    print(doc_count)
    all_products = []
    for product in collection.find({}, {'_id':0}):
        all_products.append(product)

    return all_products

def get_users():
    user_collection = database['Products']
    user = user_collection.find_one({'name':"Raman"}, {'_id':0, 'product.picture':0})
    print(user)
    return user