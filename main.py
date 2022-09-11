from flask.views import MethodView
from wtforms import Form, StringField, SubmitField
from flask import Flask,render_template

app= Flask(__name__)

class HomePage(MethodView):
    def get(self):
        return render_template("index.html")


class BillFormPage(MethodView):
    def get(self):
        bill_form=BillForm()
        return render_template("bill_page.html",bill_form=bill_form)

class ResultPage(MethodView):
    pass

class BillForm(Form):
    amount= StringField("Bill Amount:")
    period = StringField("Bill Period:")

    name1=StringField("Name of the first flatmate:")
    days_to_visit1= StringField("Days of the first flatmate:")

    name2=StringField("Name of the second flatmate:")
    days_to_visit2= StringField("Days of the second flatmate:")

    button =SubmitField("Calculate")

app.add_url_rule('/',view_func=HomePage.as_view('home_page'))
app.add_url_rule('/bill_form',view_func=BillFormPage.as_view('bill_form_page'))

app.run(debug=True)