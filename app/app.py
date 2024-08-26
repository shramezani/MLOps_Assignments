from flask import Flask
from flask import render_template, request, redirect, url_for, flash
from forms import CourseForm



app = Flask(__name__)
app.config['SECRET_KEY'] = 'my_secret_key_here'

student_list = {
    1: {'name': 'John Doe', 'email': 'john.doe@example.com', 'major': 'Computer Science'},
    2: {'name': 'Jane Smith', 'email': 'jane.smith@example.com', 'major': 'Mathematics'},
    3: {'name': 'Emily Johnson', 'email': 'emily.johnson@example.com', 'major': 'Physics'}
}

course_list = {
    1: {'name': 'Introduction to Programming', 'description': 'Learn the basics of programming.', 'teacher': 'Dr. Smith'},
    2: {'name': 'Advanced Mathematics', 'description': 'Deep dive into complex mathematical concepts.', 'teacher': 'Prof. Johnson'},
    3: {'name': 'Physics Fundamentals', 'description': 'Understand the core principles of physics.', 'teacher': 'Dr. Brown'}
}

course_id_counter = 4

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/profile')
def profile():
    return render_template('profile.html', student_list = student_list)

@app.route('/courses')
def courses():
    form = CourseForm()
    return render_template('courses.html', course_list = course_list, form=form)


@app.route('/course_detail', methods=['GET'])
@app.route('/courses/<int:course_id>', methods=['GET'])
def course_detail(course_id=None):

    if request.args:
        course_id = request.args.get('course_id')
    else:
        course_id = request.view_args.get('course_id')
    course = course_list.get(int(course_id))
    return render_template('course_detail.html', course = course)


@app.route('/update_student', methods=['POST'])
def update_student():
    student_id = int(request.form['student_id'])
    new_name = request.form['name']
    new_email = request.form['email']
    new_major = request.form['major']

    if student_id in student_list:
        student_list[student_id]['name'] = new_name
        student_list[student_id]['email'] = new_email
        student_list[student_id]['major'] = new_major

    return redirect(url_for('profile'))


@app.route('/add_course', methods=['GET', 'POST'])
def add_course():

    global course_id_counter
    form = CourseForm()
    if form.validate_on_submit():
        global course_list
        course_name = form.course_name.data
        course_description = form.course_description.data
        course_teacher = form.course_teacher.data
        
        course_list[course_id_counter] = {
            'name': course_name,
            'description': course_description,
            'teacher': course_teacher
        }
        course_id_counter += 1
        return redirect(url_for('courses'))

    return render_template('courses.html', course_list=course_list, form=form)

@app.template_filter()
def limit_words(input_str, length = 10):
    words = input_str.split()
    if len(words) > length:
        return ' '.join(words[:length]) + '...'
    return input_str


if __name__=='__main__':
    app.run(debug=True)