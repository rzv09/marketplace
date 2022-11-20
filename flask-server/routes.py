import util

database = None

def __init__(db):
    global database
    database = db


def get_products():
    collection = database["Products"]
    all_products = []
    for product in collection.find({}, {'contact':0, 'name':0}):
        product['_id'] = str(product['_id'])
        all_products.append(product)

    return all_products

def get_topic(topic, input):
    collection = database['Products']
    data = []
    for d in (collection.find({topic: input}, {'_id':0})):
        data.append(d)
    if len(data) == 1:
        return data[0]
    return data

def get_users():
    collection = database['Products']
    all_users = []
    for user in collection.find({}, {'_id':0}):
        curr_user = {}
        curr_user['name'] = user['name']
        curr_user['email'] = user['contact']['email']
        curr_user['phone'] = user['contact']['phone']
        all_users.append(curr_user)
    return all_users

def get_all_data():
    collection = database['Products']
    al = []
    for prod in collection.find({}, {'_id':0}):
        al.append(prod)
    return al

def add_product(data):
    """
    data: {
        name: String, 
        email: String, 
        phone: int,
        location: String,
        product_name: String,
        description: String,
        picture: String?,
        price: int,
        currency: String,
        category: String,
    }
    """
    try:
        new_data = {
            'name': data['name'],
            'contact':{
                'email': data['email'],
                'phone': data['phone']
            }, 
            'location': data['location'],
            'product': {
                'description': data['description'],
                'category': data['category'],
                'product_name': data['product_name'],
                'price': data['price'],
                'currency': data['currency'], 
                'picture': data['picture']
            }, 
            'time_added': util.get_time(),
            'last_updated': util.get_time()
        }
        collection = database['Products']
        collection.insert_one(new_data)
        return True
    except:
        return False
