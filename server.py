


from flask import Flask, render_template, request, redirect, session, flash
from mysqlconnection import connectToMySQL    # import the function that will return an instance of a connection
import re

from flask_bcrypt import Bcrypt        

app = Flask(__name__)
app.secret_key = "secretstuff"
bcrypt = Bcrypt(app)     # we are creating an object called bcrypt, 
                         # which is made by invoking the function Bcrypt with our app as an argument



@app.route('/')
def index():

    # get customer names and number of leads
    mysql = connectToMySQL("lead_gen_business")
    table1 = mysql.query_db("SELECT COUNT(leads.leads_id) as countLeads, CONCAT(clients.first_name, ' ', clients.last_name) as fullName FROM leads JOIN sites ON leads.site_id = sites.site_id JOIN clients ON sites.client_id = clients.client_id GROUP BY fullName;")
















    return render_template("index.html", tableLeads = table1)






if __name__ == "__main__":
    app.run(debug=True)
