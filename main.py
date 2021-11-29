from flask import Flask, render_template, redirect, request, session, url_for
from flask_mysqldb import MySQL
import MySQLdb
import MySQLdb.cursors

app = Flask(__name__)

app.secret_key = "1234353234"

app.config["MYSQL_HOST"] = "us-cdbr-east-04.cleardb.com"
app.config["MYSQL_USER"] ="bd92bde2531647"
app.config["MYSQL_PASSWORD"] = "63e698d4"
app.config["MYSQL_DB"] ="heroku_b13a1a4a3678e25"

db = MySQL(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        if "username" in request.form and "password" in request.form:
            username = request.form["username"]
            password = request.form["password"]
            cursor = db.connection.cursor(MySQLdb.cursors.DictCursor)
            cursor.execute("SELECT * FROM heroku_b13a1a4a3678e25.logininfo_db WHERE email=%s AND password=%s",(username, password))
            info = cursor.fetchone()
            if info is not None:
                if info["email"] == username and info["password"] == password:
                    session["loginsuccess"] = True
                    return redirect(url_for("profile"))
            else:
                return redirect(url_for("index"))
    return render_template("login.html")


@app.route('/new', methods=["GET", "POST"])
def new_user():
    if request.method == "POST":
        if "one" in request.form and "two" in request.form and "three" in request.form:
            username = request.form["one"]
            email = request.form["two"]
            password = request.form["three"]
            cursor = db.connection.cursor(MySQLdb.cursors.DictCursor)
            cursor.execute("INSERT INTO heroku_b13a1a4a3678e25.logininfo_db(name, password, email)VALUES(%s,%s,%s)", (username, password, email))
            db.connection.commit()
            return redirect(url_for("index"))
    return render_template("register.html")
    
@app.route('/new/profile')
def profile():
    if session["loginsuccess"] == True:
        return render_template("profile.html")
    
@app.route('/new/contact_form')
def contact_form():
        return render_template("contact_form2.html")
    
@app.route('/new/about_me')
def about_me():
        return render_template("about_me.html")

@app.route('/new/experience')
def experience():
        return render_template("exp_resume.html")
    
@app.route('/new/project_page')
def project_page():
        return render_template("project_page.html")
    
@app.route('/new/logout')
def logout():
    session.pop("loginsuccess", None)
    return redirect(url_for("index"))
    
if __name__=='__main__':
    app.run(debug=True)
    
