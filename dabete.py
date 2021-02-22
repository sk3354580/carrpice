from flask import Flask,render_template,request
import pickle
import sklearn
app = Flask(__name__)
model = pickle.load(open('diabetes3.pkl','rb'))
@app.route('/' , methods=['GET'])
def home():
    return render_template('diabe.html')
@app.route('/sugar', methods=['POST'])
def sugar():
    if request.method == 'POST':
        Pregnancies = int(request.form['Pregnancies'])
        Glucose = int(request.form['Glucose'])
        BloodPressure = int(request.form['BloodPressure'])
        Age = int(request.form['Age'])
        prediction = model.predict([[Pregnancies, Glucose, BloodPressure, Age]])
        if prediction==1:
            return render_template('diabe.html',prediction_text='Diabetes_Positive'.format(prediction))
        else:
            return render_template('diabe.html',prediction_text='Diabetes_Negative'.format(prediction))
    else:
        return render_template('diabe.html')
if __name__ == "__main__":
    app.run(debug=True)
