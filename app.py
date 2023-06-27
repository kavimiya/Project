from flask import Flask, request, jsonify,render_template
import pickle
import numpy as np
from sklearn.preprocessing import StandardScaler
#st=StandardScaler()
app = Flask(__name__)

#with open('model.pkl', 'rb') as file:
#    model = pickle.load(file)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    # Render the HTML form for user input
    return render_template('input.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Retrieve the input values from the form
    int_features = [int(x) for x in request.form.values()]
    final_features = np.array(int_features).reshape(-1,1)
    st=StandardScaler()
    final_features=st.fit_transform(final_features)
    '''input_marks = [
        int(request.form['mark1']),
        int(request.form['mark2']),
        float(request.form['mark3'])
    ]'''
    
    final_features=final_features.flatten()
    print(final_features.reshape(1,-1))
    predicted_grade = model.predict(final_features.reshape(1,-1))
    a=[]
    if predicted_grade==0:
        a='Lazy'
        return a
    else :
        a='No Lazy'
        return a
    

    return f'Predicted Result: {a}'

if __name__ == '__main__':
    app.run(debug=True)