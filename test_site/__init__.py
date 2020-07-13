from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

#Variable name of the module, running with python, name=main
app=Flask(__name__) 
app.config['SECRET_KEY']='bf784d66e566d2110e930d06c23ec150'
#localhost
#app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:postgres123@localhost/test_site2'#specifying the URI of your database, address where database is stored 
#online application1      
app.config['SQLALCHEMY_DATABASE_URI']='postgres://zvmhjyxgfoyhax:650a295ab02887adaeaacca516faa3fafbee4b9700da9b500cd20c460eb85074@ec2-34-236-215-156.compute-1.amazonaws.com:5432/d4t3kv29qb07kq?sslmode=require' 
db=SQLAlchemy(app)
login_manager = LoginManager(app)

from test_site import routes