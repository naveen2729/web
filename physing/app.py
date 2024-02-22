from flask import Flask, render_template, request
import joblib
import re

app = Flask(__name__)

# Load the pre-trained machine learning model
model = joblib.load('model.pkl')

def is_phishing(url):
    # Feature extraction (you can enhance this part)
    features = [len(url), len(re.findall(r'\d', url)), len(re.findall(r'\W', url))]
    
    # Predict using the pre-trained model
    prediction = model.predict([features])[0]
    
    return prediction  # 0: Legitimate, 1: Phishing

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/check_phishing', methods=['POST'])
def check_phishing():
    url = request.form['url']
    prediction = is_phishing(url)
    
    return render_template('result.html', url=url, prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)
