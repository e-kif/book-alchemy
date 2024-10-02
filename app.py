import os
from flask import Flask, render_template, request, redirect
from data_models import db, Authors, Books

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data/library.sqlite'
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:////{os.path.join(os.getcwd(), "data", "library.sqlite")}'

db.init_app(app)
#
# with app.app_context():
#     db.create_all()


@app.route('/add_author', methods=['GET', 'POST'])
def add_author():
    if request.method == 'GET':
        status = request.args.get('status')
        warning = request.args.get('warning')
        return render_template('add_author.html', status=status, warning=warning)
    if request.method == 'POST':
        name = request.form.get('name').strip()
        birth_date = request.form.get('birth_date').strip()
        date_of_death = request.form.get('date_of_death').strip()
        status = 'failure'
        if name and birth_date:
            author = Authors(
                name=name,
                birth_date=birth_date,
                date_of_death=date_of_death)
            db.session.add(author)
            db.session.commit()
            status = 'success'
        else:
            status += '&warning=Author name and birthdate are required fields'
        return redirect(f'/add_author?status={status}', 302)


@app.route('/add_book', methods=['GET', 'POST'])
def add_book():
    if request.method == 'GET':
        status = request.args.get('status')
        warning = request.args.get('warning')
        authors = db.session.query(Authors).all()
        return render_template('add_book.html', status=status, warning=warning, authors=authors)
    if request.method == 'POST':
        name = request.form.get('name').strip()
        birth_date = request.form.get('birth_date').strip()
        date_of_death = request.form.get('date_of_death').strip()
        status = 'failure'
        if name and birth_date:
            author = Authors(
                name=name,
                birth_date=birth_date,
                date_of_death=date_of_death)
            db.session.add(author)
            db.session.commit()
            status = 'success'
        else:
            status += '&warning=Author name and birthdate are required fields'
        return redirect(f'/add_author?status={status}', 302)


@app.route('/', methods=['GET'])
def home_page():
    return render_template('home.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
