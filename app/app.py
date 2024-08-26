from flask import Flask
from flask import render_template


app = Flask(__name__)



@app.route('/')
def home():
    return render_template('home.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/courses')
def courses():
    return render_template('courses.html')


if __name__=='__main__':
    app.run(debug=True)