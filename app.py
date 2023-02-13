from flask import Flask, render_template, request
import requests
app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def index():
    if request.method == 'POST':
        input_text = request.form['text']
        output = predict_genres(input_text)[0]
        print(output)
        print('the rest is')
        confidence_list = output['confidences']
        labels = [ _['label'] for _ in confidence_list if _['confidence'] >= 0.5]
        label_text = ''
        for idx, label in enumerate(labels):
            label_text = label_text + label
            if idx != len(labels) - 1: label_text = label_text + ','
        print(label_text)
        return render_template('result.html', input_text=input_text, output_text=label_text) 
    else:
        return render_template('index.html') 

def predict_genres(input_text):
    response = requests.post("https://abrar-adnan-game-classifier.hf.space/run/predict", json={
	"data": [
		input_text
	]}).json()
    data = response["data"]
    return data


if __name__ == '__main__':
    app.run(debug=True)