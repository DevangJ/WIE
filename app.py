from flask import Flask, render_template, request
import re
app = Flask(__name__)


@app.route('/first.html', methods=["post","get"] )
def first():
    inputFirst = None
    if request.method == "POST":
        if re.search('[0-9]', request.form['input']):
            inputFirst = (7*(float(request.form['input'])+3))
        else:
            inputFirst = 'Invalid Input'
    return render_template('first.html', input=inputFirst)


@app.route('/second.html', methods=["post","get"] )
def second():
    inputSecond = None
    if request.method == "POST":
        if re.search('[0-9]', request.form['input']):
            inputSecond = (float(request.form['input'])**2)+13
        else:
            inputSecond = 'Invalid Input'
    return render_template('second.html', input=inputSecond)


@app.route('/third.html', methods=["post","get"] )
def third():
    inputThird = None
    if request.method == "POST":
        if re.search('[0-9]', request.form['input']):
            inputThird = (float(request.form['input'])**2)*3
        else:
            inputThird = 'Invalid Input'
    return render_template('third.html', input=inputThird)


@app.route('/fourth.html', methods=["post","get"] )
def fourth():
    inputFourth = None
    if request.method == "POST":
        if re.search('[0-9]', request.form['input']):
            inputFourth = float(request.form['input']) - (10 * (float(request.form['input']) ** 0.5))
        else:
            inputFourth = 'Invalid Input'
    return render_template('fourth.html', input=inputFourth)


@app.route('/fifth.html', methods=["post","get"] )
def fifth():
    inputFifth = None
    if request.method == "POST":
        if re.search('[0-9]', request.form['input']):
            inputFifth = (10*float(request.form['input']))**2
        else:
            inputFifth = 'Invalid Input'
    return render_template('fifth.html', input=inputFifth)


@app.route('/sixth.html', methods=["post","get"] )
def sixth():
    inputSixth = None
    if request.method == "POST":
        if re.search('[0-9]', request.form['input']):
            inputSixth = float(request.form['input'])**2
        else:
            inputSixth = 'Invalid Input'
    return render_template('sixth.html', input=inputSixth)


@app.route('/seventh.html', methods=["post","get"] )
def seventh():
    inputSeventh = None
    if request.method == "POST":
        if re.search('[0-9]', request.form['input']):
            inputSeventh = float(request.form['input'])**2
        else:
            inputSeventh = 'Invalid Input'
    return render_template('seventh.html', input=inputSeventh)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True, threaded=True)
