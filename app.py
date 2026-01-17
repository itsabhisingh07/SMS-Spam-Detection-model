from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

model = pickle.load(open('model.pkl', 'rb'))
vectorizer = pickle.load(open('vectorizer.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        message = request.form['message']
        
        
        data = [message]
        vect = vectorizer.transform(data).toarray()
        
        
        prediction = model.predict(vect)
        
        result = "Spam" if prediction[0] == 1 else "Not Spam (Ham)"
        
        return render_template('index.html', prediction=result, user_input=message)

if __name__ == '__main__':
    app.run(debug=True)