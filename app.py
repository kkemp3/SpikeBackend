from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/logininfo'
db = SQLAlchemy(app)

class LoginInfo(db.Model):
    __tablename__ = "logins"
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(), unique=True)
    password = db.Column(db.String())

    def __init__(username, password):
        this.username = username
        this.password = password


@app.route('/')
def index():
    return render_template('index.html')

# Save e-mail to database and send to success page
@app.route('/insert', methods=['POST'])
def insert():
    username = None
    if request.method == 'POST':
        username = request.form['username']
        # Check that email does not already exist (not a great query, but works)
        if not db.session.query(User).filter(User.username == username).count():
            username = User(username)
            db.session.add(usernmae)
            db.session.commit()
            return render_template('success.html')
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)