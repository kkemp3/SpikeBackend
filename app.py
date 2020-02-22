from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost:5432/logins'
SQLALCHEMY_TRACK_MODIFICATIONS = False
CORS(app, supports_credentials=True)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

class LoginInfo(db.Model):
    __tablename__ = "logininfo"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True)
    password = db.Column(db.String(40))

    def __init__(self, username, password):
        self.username = username
        self.password = password
    
    def __repr__(self):
        return '<User %r>' % self.username


@app.route('/')
def index():
    return render_template('index.html')
 
# save username and password to the database
@app.route('/register', methods=['POST'])
def insert():
    if request.method == 'POST':
        content = request.json
        #print(content)
        user = content.get('username')
        pw = content.get('password')
        #print('username: {}'.format(user))
        #print('password: {}'.format(pw))
        entry = LoginInfo(user, pw)
        db.session.add(entry)
        db.session.commit()
        return { "message": "username {entry.username} has been create successfully" }
    else:
        return { "error": "The request was not a post request" }

@app.route('/dologin', methods=['GET', 'POST'])
def getUserAndPw():
    if request.method == 'POST' or request.method == 'GET':
        content = request.json
        user = content.get('username')
        pw = content.get('password')
        print('user login: {}'.format(user))
        print('user password: {}'.format(pw))
        logins = LoginInfo.query.all()
        results = [
            {
                "username": login.username,
                "password": login.password
            } for login in logins
        ]

        for login in logins:
            if (user == login.username and pw == login.password):
                print("Login successful!")
                return { "message": "Success!"}

        print('Login faillure')
        return { "message": "Failure!"}    
    else:
        return {"error": "No POST request received"}






if __name__ == "__main__":
    app.run(debug=True)