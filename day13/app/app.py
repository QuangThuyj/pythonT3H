from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/hello', methods=['GET', 'POST'])
def hello():
    data_dict = request.args if request.method == 'GET' else request.form
    name = data_dict['name']
    gender = data_dict['gender']
    salutation = 'Mr' if gender == 'M' else 'Ms'
    return render_template('hello.html', name=name, salutation=salutation)

# @app.route('/hello2', methods=['POST'])
# def hello2():
#     name = request.form['name']
#     gender = request.form['gender']
#     print(name, gender)
#     sex = 'Mr' if gender == 'M' else 'Ms'
#     return render_template('hello.html', name=name, sex=sex)

app.run(debug=True)
