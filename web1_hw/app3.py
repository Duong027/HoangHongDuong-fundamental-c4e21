#without render template
#1. Create a flask app
from flask import Flask

app3 = Flask(__name__)

#2. Create router
@app3.route("/bmi/<int:height>/<int:weight>")
def homepage(height,weight):
    BMI = weight / (height/100 * height/100)
    print(BMI)
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
    return ("Chi so BMI:" + " "+ str(BMI)+". Ket qua: " + " "+ cond)



#3. Run app
print('Running app')
if __name__ == "__main__":
    app3.run(debug=True)