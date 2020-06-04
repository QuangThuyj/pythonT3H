from flask import Flask, request, redirect, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(30), unique=True)
    name = db.Column(db.String(200))


def createProduct(code, name):
    product = Product()
    product.code = code
    product.name = name
    db.session.add(product)
    db.session.commit()


def getAllProduct():
    return Product.query.all()


def getProductById(id):
    return Product.query.get(id)


for p in getAllProduct(): print(p.code, p.name)
p1 = getProductById(1)
print('p[id=1]', p.code, p.name)

db.create_all()


@app.route('/')
def index():
    products = getAllProduct()
    return render_template('index.html', products=products)


app.run(debug=True)

# if Product.query.count()==0:
#     createProduct('IP7', 'Iphone 7')
#     createProduct('IP8', 'Iphone 8')
#     createProduct('IPX', 'Iphone X')
#     createProduct('IPXS', 'Iphone XS')
