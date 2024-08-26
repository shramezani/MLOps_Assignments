from flask import Flask
from flask import render_template


app = Flask(__name__)

student_list = [
    {'name': 'John Doe', 'email': 'john.doe@example.com', 'major': 'Computer Science'},
    {'name': 'Jane Smith', 'email': 'jane.smith@example.com', 'major': 'Mathematics'},
    {'name': 'Emily Johnson', 'email': 'emily.johnson@example.com', 'major': 'Physics'}
]

course_list = [
    {'name': 'Introduction to Programming', 'description': 'Learn the basics of programming.', 'teacher': 'Dr. Smith'},
    {'name': 'Advanced Mathematics', 'description': 'Deep dive into complex mathematical concepts.', 'teacher': 'Prof. Johnson'},
    {'name': 'Physics Fundamentals', 'description': 'Understand the core principles of physics.', 'teacher': 'Dr. Brown'}
]

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/profile')
def profile():
    return render_template('profile.html', student_list = student_list)

@app.route('/courses')
def courses():
    return render_template('courses.html', course_list = course_list)


if __name__=='__main__':
    app.run(debug=True)