from flask import Flask, render_template, redirect, request
import pymysql
import yaml
#  import modules

#db = yaml.load(open("config.yaml"))
#connection = pymysql.connect(host = 'mysqlhost', user = 'mysqluser' , password = 'mysqlpaaword' , db = 'mysqldb')
connection = pymysql.connect(host = "database-2.cyodqo0jmk7h.us-east-1.rds.amazonaws.com", user = "rama" , password = "rama1234" , db = "ramaDB")


app = Flask(__name__)
# intiantiate an obj to module

# add route to when request is made 
# render template , save html files in templates folder , using render u can call
@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        # fetch the form data and store into database
        userdetails = request.form
        # get all the details on login for mfrom broser
        email = userdetails['email']
        print(email)
        # stores name field in name variable
        password = userdetails['password']
        cur = connection.cursor() 

        query = cur.execute("select * from employee where email=%s",(email))
        print(query)
        if query == 0:
            # establish a connection to the cursor
            cur.execute("insert into employee (email, password) values (%s, %s)",(email, password))
            #insert form values into databse
            connection.commit()
            cur.close()
            return 'updated in table'
        return 'username already exists'
    return render_template('index.html')
    

#@app.route('/users')
#def users():
#    cur = connection.cursor() 
        # establish a connection to the cursor
#    cur.execute("Select * from employee")
         #fetch values from databse
#    userdetails = cur.fetchall()
#    return render_template('user.html')
#    cur.close()

if __name__ == '__main__':
    app.run(host="0.0.0.0", port="6000", debug=True)

# run the application


