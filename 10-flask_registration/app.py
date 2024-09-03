from flask import Flask
from flask import render_template, redirect, url_for, flash

from forms import SignupForm


app = Flask(__name__)
app.config['SECRET_KEY'] = 'my_secret_key'  

@app.route('/')
def root():
    return render_template('index.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignupForm()
    if form.validate_on_submit():
        '''
        inputs = request.form if request.method == 'POST' else request.args 
        username = inputs.get('username')
        email = inputs.get('email')
        password = inputs.get('password')
        '''
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('Panel'))
    return render_template('signup.html', form=form)


@app.route('/panel')
def Panel():
    return render_template('panel.html')
if __name__ == "__main__":
    app.run(debug=True)