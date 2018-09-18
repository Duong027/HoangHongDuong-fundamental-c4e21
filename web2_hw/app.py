from flask import Flask,render_template,request

import mlab
from post import Post # import tu file Pose


app = Flask(__name__)
mlab.connect() # Connect server va database

@app.route("/",methods = ['GET','POST'])
def register():
    if request.method == "GET":
        return render_template('register.html') # tra ve HTML
    elif request.method == "POST":
        #1 Get form (boc tach form )
        form = request.form
        tdd = form['tendaydu']
        e = form['email']
        tdn = form['tendangnhap']
        mk = form['matkhau']

         

        #2. Add new post

        register = Post(tendaydu = tdd, email = e, tendangnhap = tdn, matkhau = mk)    

        register.save()

     
        return ("Dữ liệu của bạn đã được lưu vào database")


if __name__ == '__main__':
    app.run(debug=True)

# Render dc 1 bien down
# render dc 1 list bai trc dung for
# render dc 1 dict
# render dc 1 list gom nhieu dict

