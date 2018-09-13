#1. Create a flask app
from flask import Flask,render_template,redirect

app = Flask(__name__)
#2. Create router
@app.route("/about-me")
def homepage():
    return render_template("homepage.html")

@app.route("/school")
def school():
    return redirect("http://techkids.vn",code = 302)
#3. Run app
print('Running app')
if __name__ == "__main__":
    app.run(debug=True)           
