from flask import Flask, render_template, request

app = Flask(__name__)


num_rows = 1
num_cols = 1

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/patients')
def patients():
    return render_template('patients.html')

@app.route('/result')
def result():
    return render_template('result.html')
    
@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    age = request.form['age']
    print(name)
    return render_template('submit.html', name=name, age=age)

@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        app.num_rows = int(request.form.get('num_rows'))
        app.num_cols = int(request.form.get('num_cols'))
        app.col_names = request.form.getlist('col_name')
        # Do something with the form data
        return render_template('form.html',num_rows=app.num_rows, num_cols= app.num_cols, col_names=app.col_names)
    return render_template('form.html',num_rows=app.num_rows, num_cols= app.num_cols, col_names=app.col_names)

if __name__ == '__main__':
    app.num_cols = 1
    app.num_rows = 1
    app.col_names = {"column name"}
    app.run(port=3030,debug=True)