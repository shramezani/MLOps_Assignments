from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length

class CourseForm(FlaskForm):
    course_name = StringField('Course Name', validators=[DataRequired(), Length(max=20)])
    course_description = StringField('Course Description', validators=[DataRequired(), Length(max=100)])
    course_teacher = StringField('Teacher', validators=[DataRequired(), Length(max=20)])
    submit = SubmitField('Add Course')