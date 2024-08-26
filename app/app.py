from flask import Flask
from flask import render_template


app = Flask(__name__)

students = [
    {'name': 'John Doe', 'email': 'john.doe@example.com', 'major': 'Computer Science'},
    {'name': 'Jane Smith', 'email': 'jane.smith@example.com', 'major': 'Mathematics'},
    {'name': 'Emily Johnson', 'email': 'emily.johnson@example.com', 'major': 'Physics'}
]

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/profile')
def profile():
    return render_template('profile.html', students = students)

@app.route('/courses')
def courses():
    return render_template('courses.html')


if __name__=='__main__':
    app.run(debug=True)