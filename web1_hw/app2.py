#With render template
#1. Create a flask app
from flask import Flask,render_template

app2 = Flask(__name__)

#2. Create router
@app2.route("/bmi/<int:height>/<int:weight>")
def homepage(height,weight):
    BMI = weight / (height/100 * height/100)
    if BMI< 16:
        cond = 'Severely underweight'
    elif BMI < 18.5:
        cond = 'Underweight'
    elif BMI < 25:
        cond = 'Normal'
    elif BMI < 30:
        cond = 'Overweight'
    else:
        cond = 'Obese'

    return render_template("bmi.html",BMI = BMI,cond = cond)

#3. Run app
print('Running app')
if __name__ == "__main__":
    app2.run(debug=True)