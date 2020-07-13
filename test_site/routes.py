from flask import render_template, request, redirect, url_for, flash#request will allow us to get variables from html files
from test_site import app, db
from test_site.forms import ProfileForm
from test_site.models import Profile, Response
from flask_login import login_user, current_user, logout_user

@app.route("/")
def login():
    return render_template("login.html")  #python should be able to get the html file and render into the home page    

@app.route("/index", methods=['POST'])
def index():  
    if request.method =='POST':
        password_1=request.form["password"]
        if password_1=="participant2020":
                return render_template("index.html")  
    return render_template("login.html", text="Wrong password, try again." )  


@app.route("/profile", methods=['GET', 'POST'])
def profile():
    if request.method =='POST':
        form = ProfileForm()
        #if form.validate_on_submit():  
        name_1=form.username.data
        language_1=form.language.data
        age_1=form.age.data
        print (name_1, language_1, age_1)
        if db.session.query(Profile).filter(Profile.name_==name_1).count()==0:
            print (name_1, language_1, age_1)
            captured_data=Profile(name_1, age_1, language_1)
            db.session.add(captured_data)
            db.session.commit()
            login_user(captured_data)
            return render_template("questions.html", form=form )
            #return render_template("random.html", form=form )  
        return render_template("profile.html", form=form)

@app.route("/questions", methods=['GET', 'POST'])
def questions():
    if request.method =='POST':
        question_1=request.form["q"]
        time_1=request.form["time"]
        if (time_1==None):
            time_1=1
        user_id=current_user.id
        if (time_1=='20'):
            answer_1=0
        if (time_1!='20'):
            answer_1=request.form["answer"] 
        correct_ans=request.form["correct_ans"]
        if (answer_1==correct_ans):
            status=1
        else:
            status=0
        captured_data=Response(question_1,answer_1,correct_ans, status, time_1,user_id)
        db.session.add(captured_data)
        db.session.commit()
        print(db.session.query(Response).filter(Response.user_id==current_user.id).count())
        if db.session.query(Response).filter(Response.user_id==current_user.id).count()>=50:
            return render_template("success.html")
        return render_template("questions.html")            

@app.route("/success", methods=['GET', 'POST'])
def success():
    if request.method =='POST':
        logout_user()
        return render_template("success.html")