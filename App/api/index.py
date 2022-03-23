from flask import Blueprint, redirect

index_blue = Blueprint('index_blue', __name__)

@index_blue.route('/', methods=['GET'])
def index():
    return redirect('/index.html')