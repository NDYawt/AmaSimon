# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.

from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///aald.db'

db = SQLAlchemy(app)

# Define the User model

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(50),  nullable=False)
    lastname = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(150), nullable=False)
    role = db.Column(db.String(50), nullable=False)

def create_db():
    with app.app_context():
        db.create_all()



# create the routes
@app.route('/')
def index():
    users = User.query.all()
    return render_template('index.html', users=users)

@app.route('/add-user', methods=['GET','POST'])
def add_user():
    if request.method == 'POST':
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        email = request.form['email']
        role = request.form['role']



        new_user = User(firstname=firstname, lastname=lastname, email=email, role=role)

        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('add_user.html',title='Add a User')

if __name__ == '__main__':
    create_db()
    app.run(port=5001, debug=True)






