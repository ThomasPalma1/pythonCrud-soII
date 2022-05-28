from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://user:senha@localhost/crudpython'
db = SQLAlchemy(app)


class Employee(db.Model):
    __tablename__ = 'employee'
    _id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50))

    def __init__(self, nome):
        self.nome = nome


db.create_all()


@app.route("/")
@app.route("/index")
def index():
    return "<h1>it's working!</h1>"


if __name__ == "__main__":
    app.run(debug=True)
