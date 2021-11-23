
from flask import Flask, request, jsonify, redirect, url_for, render_template
from flask_sqlalchemy import SQLAlchemy 
from flask_cors import CORS
#  converting complex datatypes, such as objects, to and from native Python datatypes
from flask_marshmallow import Marshmallow 
from twilio.rest import Client

import os

#init app
app = Flask(__name__)
CORS(app)
#setup alchemy database, ensure we can locate our db file, which will be in the root
basedir = os.path.abspath(os.path.dirname(__file__))
#database, naming postscript, looking for db.postscript file
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
#seting to false to avoid console warnings
app.config['SQLACLHEMY_Track_MODIFICATIONS'] = False

#init db
db = SQLAlchemy(app)

#init ma
ma = Marshmallow(app)


#Product Class/Model
class Product(db.Model):
    #define fields
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100), unique = True)
    #initializer/constructor, id autoincremented, only need to pass in name. 
    def __init__(self, name):
        self.name = name


#product schema
class ProductSchema(ma.Schema):
    #fields we want to show
    class Meta: 
        fields = ('id', 'name')

#init schema, avoid console warnings
product_schema = ProductSchema()
#as we are either dealing with a single product or getting multiple as an array, we need a 'products' schema as well
products_schema = ProductSchema(many = True)


class ProductMessages(db.Model):
    #define fields 
    id = db.Column(db.Integer, primary_key = True)
    productId = db.Column(db.Integer)
    message = db.Column(db.String(300))
    draftStatus = db.Column(db.Boolean, unique= False, default = True)

    #initializer/constructor
    def __init__(self, productId, message, draftStatus):
        self.productId = productId
        self.message = message 
        self.draftStatus = draftStatus

class ProductMessagesSchema(ma.Schema):
    class Meta:
        fields = ('id', 'productId', 'message', 'draftStatus')
        #init schema
productMessage_schema = ProductMessagesSchema()
productMessages_schema = ProductMessagesSchema(many = True)
     

#create a Product
@app.route('/product', methods=['POST'])
def add_product():
    name = request.json['name']
    new_product = Product(name)
    db.session.add(new_product)
    db.session.commit()
    return product_schema.jsonify(new_product)


#get all Products
@app.route('/product', methods=['GET'])
def get_products():
    all_products = Product.query.all()
    result = products_schema.dump(all_products)
    return jsonify(result)


#get all productsMessages associated with a product id
@app.route("/productMessage/<productId>", methods= ['GET'])
def get_productMessages(productId):
    productMessages = ProductMessages.query.filter(ProductMessages.productId == productId).all()
    result = productMessages_schema.dump(productMessages)
    return jsonify(result)

#send a draft as a text message with twilio

#twilio credentials
account_sid =  'ACb6a3dbd15a35f3b4fe0f0d3da062d37e'
auth_token = 'c6f020562c4d28312775bae5583323ec'
client = Client(account_sid, auth_token)

def sendMessage(smsMessage):
    message = client.messages \
        .create(
            body= smsMessage,
            from_= '+17194975835',
            to='+17816860591'
        )  

#submit a new message draft associated with product id
@app.route('/productMessage/<productId>', methods=['POST'])
def add_productMessageDraft(productId):
    productId = productId
    message = request.json['message']    
    new_productMessage = ProductMessages(productId, message, True)
    db.session.add(new_productMessage)
    db.session.commit()
    return  productMessage_schema.jsonify(new_productMessage)


@app.route('/productMessageSend/<productId>', methods=['POST'])
def sendAndSaveFinalMessage(productId):
    productId = productId
    message = request.json['message']
    sendMessage(message)
    return {"success": True}


@app.route("/health-check")
def health_check():
    return {"success": True}

#Run Server
if __name__ == "__main__":
    db.create_all()
    app.run(debug=os.environ.get("FLASK_DEBUG", False))

#todos:
#1. store Twillio cred as enviro variables
#2. Modularize this file, import DB, models, endpoints, and general functions all separately.