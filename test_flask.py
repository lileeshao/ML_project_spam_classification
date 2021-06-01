from flask import Flask,render_template,redirect,request,url_for,flash
from algorithm.random import Random
app = Flask(__name__)
print(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('main.html')

@app.route('/algorithm', methods=['GET', 'POST'])
def algorithm():
    return render_template('algorithm.html')

@app.route('/analyst', methods=['GET', 'POST'])
def analyst():
    return render_template('main.html')

@app.route('/result', methods=['GET', 'POST'])
def result():
    if request.method == 'POST':
        user_info = request.values.to_dict()
        text = user_info['email']
        value = 0
        if user_info['alg'] == 'random':
            value = Random(text)
            value = round(value)
        
    return render_template('result.html',text=text, value=value, alg=user_info['alg'])

@app.route('/dataset', methods=['GET', 'POST'])
def dataset():
    return render_template('dataset.html')

@app.route('/team', methods=['GET', 'POST'])
def team():
    return render_template('team.html')


if __name__ == '__main__':
    app.debug = False
    app.run(host='localhost', port=5000)





