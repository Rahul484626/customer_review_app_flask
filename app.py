from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
from flask import Flask, jsonify, Response,  render_template, request
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/review'
db = SQLAlchemy(app)

# class ReviewForm(Form):
#     name=TextField('firstname')
#     product=TextField('product')
#     review=TextField('review')


class Reviews(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    product = db.Column(db.String(120),  nullable=False)
    review = db.Column(db.String(120),  nullable=False)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/Review", methods= ['GET' , 'POST'])    
def Review():
    if(request.method=='POST'):
        name= request.form.get('name')
        product= request.form.get('product')
        review= request.form.get('review')
        entry= Reviews(name=name, product=product, review=review)
        db.session.add(entry)
        db.session.commit()

    return render_template('index.html')

@app.route("/review/<string:review_slug>", methods=["GET"])
def review_route(review_slug):
    review= Reviews.query.all()
    return render_template('index.html', review=review)

@app.route("/delete/<string:sno>", methods= ['GET', 'POST'])
def delete():
    review= Reviews.query.all()
    db.session.delete(review)
    db.session.commit()
    return render_template('index.html')

if __name__ == '__main__':
   app.run(debug = True)