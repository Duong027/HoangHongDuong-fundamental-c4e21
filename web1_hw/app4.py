#1. Create a flask app
from flask import Flask

app4 = Flask(__name__)

#2. Create router
@app4.route("/user/<username>")
def Name(username):
    Users = {'huy':{'name':'Nguyen Quang Huy','age':29},'tuananh':{'name':'Huynh Tuan Anh','age':22}}

    if username == 'huy':
        return(str(Users['huy']))
    elif username == 'tuananh':
        return(str(Users['tuananh']))
    else:
        return('Not found')
   

#3. Run app
print('Running app')
if __name__ == "__main__":
    app4.run(debug=True)