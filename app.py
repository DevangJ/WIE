from flask import Flask, render_template, request
import re
app = Flask(__name__)


@app.route('/first', methods=["post","get"] )
def first():
    inputFirst = None
    if request.method == "POST":
        if re.search('[0-9]', request.form['input']):
            inputFirst = float(request.form['input'])**2
        else:
            inputFirst = 'Invalid Input'
    return render_template('first.html', input=inputFirst)


@app.route('/second', methods=["post","get"] )
def second():
    inputSecond = None
    if request.method == "POST":
        if re.search('[0-9]', request.form['input']):
            inputSecond = float(request.form['input']) - (10 * (float(request.form['input']) ** 0.5))
        else:
            inputSecond = 'Invalid Input'
    return render_template('second.html', input=inputSecond)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True, threaded=True)
