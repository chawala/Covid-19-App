from enum import unique
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from send_email import send_email
from sqlalchemy.sql import func


app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:1987Bernice@localhost/Temperature_collector'
db=SQLAlchemy(app)

class Data(db.Model):
    __tablename__="data"
    id=db.Column(db.Integer, primary_key=True)
    email_=db.Column(db.String(120),unique=True)
    temperature_=db.Column(db.Integer)

    def __init__(self,email_, temperature_):
        self.email_=email_
        self.temperature_=temperature_
     
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/success", methods=['POST'])
def success():
    if request.method=='POST':
        
        email=request.form["email_name"]
        temperature=request.form["temperature_name"]
        
        
        if db.session.query(Data).filter(Data.email_==email).count()==0:
            data1=Data(email,temperature)
            db.session.add(data1)
            db.session.commit()
            average_temperature=db.session.query(func.avg(Data.temperature_)).scalar()
            average_temperature=round(average_temperature,1)
            count=db.session.query(Data.temperature_).count()
            send_email(email, temperature,average_temperature,count)
            #print(average_height)
            return render_template("success.html")
        return render_template('index.html', 
        text="Seems like we have got something from that email address already!")

if __name__ == '__main__':
    app.debug=True
    app.run()