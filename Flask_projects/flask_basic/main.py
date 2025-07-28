from flask import Flask, redirect

app = Flask(__name__)

@app.route('/')
def first_contact():
    return redirect("/bbbb", code=301)

@app.route('/aaaa')
def print_hi1():
    return f'마 니 자신있나!'

@app.route('/bbbb')
def print_hi2():
    return f'피가 끓나!'


