from flask import Flask
from flask import render_template


app = Flask(__name__)

@app.route('/')
def root():
    return render_template('signup.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')


if __name__ == "__main__":
    app.run(debug=True)