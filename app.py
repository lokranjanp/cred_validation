# app.py
from flask import Flask, render_template, request, redirect, url_for, flash
from luhn import luhn_check, generate_luhn_number

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/generate', methods=['GET', 'POST'])
def generate():
    if request.method == 'POST':
        prefix = request.form['prefix']
        length = int(request.form['length'])

        if not prefix.isnumeric():
            flash("Prefix must be numeric value")
            return redirect(url_for('generate'))

        if int(length) < 1:
            flash("Length must be positive integer")
            return redirect(url_for('generate'))

        number = generate_luhn_number(prefix, length)
        return render_template('generate.html', number=number)
    return render_template('generate.html')


@app.route('/validate', methods=['GET', 'POST'])
def validate():
    if request.method == 'POST':
        number = request.form['number']
        is_valid = luhn_check(number)
        return render_template('validate.html', number=number, is_valid=is_valid)
    return render_template('validate.html')


if __name__ == '__main__':
    app.run(debug=True)
