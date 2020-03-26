from flask import Flask
from my_app.product.views import product

app = Flask(__name__)
#import the views
app.register_blueprint(product)

@app.template_filter('mydouble')
def mydouble_filter(n:float):
    return n*2