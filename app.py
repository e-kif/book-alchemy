import os
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from data_models import db, Authors, Books

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data/library.sqlite'
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:////{os.path.join(os.getcwd(), "data", "library.sqlite")}'

db.init_app(app)

# with app.app_context():
#     db.create_all()


@app.route('/add_author', methods=['GET', 'POST'])
def add_author():
    if request.method == 'GET':
        return render_template('add_author.html')


@app.route('/', methods=['GET'])
def home_page():
    return render_template('home.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)