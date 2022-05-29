from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://python-crud:123@192.168.0.108/crudpython'
db = SQLAlchemy(app)


class Employee(db.Model):
    __tablename__ = 'employee'
    _id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50))

    def __init__(self, name):
        self.name = name


db.create_all()


@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")


@app.route("/registration")
def registration():
    return render_template("registration.html")


@app.route("/register", methods=['GET', 'POST'])
def register():
    if request.method == "POST":
        name = (request.form.get("name"))

        if name:
            f = Employee(name)
            db.session.add(f)
            db.session.commit()
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
