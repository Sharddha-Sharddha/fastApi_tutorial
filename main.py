from fastapi import FastAPI
from models import product

app = FastAPI()

@app.get('/')
def greet():
    return {'message' : "Hey! What's up?"}

products = [
    product(id= 1, name= 'table', title= 'side Table', price= 299, quantity=15),
    product(id= 2, name= 'mouse', title= 'gamming mouse', price= 500, quantity=20),
    product(id= 3, name= 'keyboard', title= 'gamming keyboard', price= 450, quantity=20),
    product(id= 4, name= 'pen holder', title= 'wooden pen holder', price= 150, quantity=8)
    ]

@app.get('/products')
def get_all_product():
    return products


@app.get('/products/{id}')
def product_by_id(id : int):
    for product in products:
        if product.id == id:
            return product
    return 'no product'

@app.post('/products')
def add_product(Prod: product):
    products.append(Prod)
    return Prod


@app.put('/products')
def update_product(id : int, prod: product):
    for i in range(len(products)):
        if products[i].id == id:
            products[i]= prod
            return'product updated'

    return 'no update in products'
            
@app.delete('/products')
def delete_product(id : int):
    for i in range(len(products)):
        if products[i].id == id:
            products.pop(i)
            return 'product deleted'
    return 'no product to delete'