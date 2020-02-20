from flask import Flask, render_template, request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost:5432/loginfo'
cors = CORS(app, resources={r"/*": {"origins": "*"}})
db = SQLAlchemy(app)

class LoginInfo(db.Model):
    __tablename__ = "logins"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True)
    password = db.Column(db.String(40))

    def __init__(username, password):
        this.username = username
        this.password = password
    
    def __repr__(self):
        return '<User %r>' % self.username


@app.route('/')
def index():
    return render_template('index.html')

# Save e-mail to database and send to success page
@app.route('/register', methods=['POST'])
def insert():
    username = None
    if request.method == 'POST':
        content = request.json
        print(content)
        #print('username' + username)
        # if not db.session.query(User).filter(User.username == username).count():
        #     username = User(username)
        #     db.session.add(usernmae)
        #     db.session.commit()
        return render_template('success.html')
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)