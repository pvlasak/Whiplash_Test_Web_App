from sqlalchemy import desc

from forms import LoginForm, UserRegistrationForm, TestRegistrationForm, ResultForm, SampleRegistrationForm
from app import app, db, login_manager
from models import *
from flask import render_template, redirect, url_for, flash, request
from flask_login import current_user, login_user, logout_user, login_required


@app.route('/')
def index():
    return render_template("index.html")


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        flash("User is authenticated!Redirecting to database...")
        return redirect(url_for('profile'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user:
            if user.check_password(form.password.data):
                login_user(user, remember=form.remember_me.data)
                flash("Login Successful!")
                return redirect(url_for('profile'))
            else:
                flash("Wrong Password - Try Again!")
        else:
            flash("That User Does Not Exists!")
    return render_template('login.html', title='Sign In', form=form)


@app.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    flash("You have been logged out. Thanks.")
    return redirect(url_for('login'))


@app.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    all_tests = Test.query.all()
    samples = Sample.query.all()
    pulses = Pulse.query.all()
    return render_template('profile.html', template_tests=all_tests, template_samples=samples,
                           template_pulses=pulses)


@app.route('/user_register', methods=['GET', 'POST'])
def user_register():
    form = UserRegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
    return render_template('user_register.html', title='Register', form=form)


@app.route('/sample_register', methods=['GET', 'POST'])
@login_required
def sample_register():
    form = SampleRegistrationForm()
    if form.validate_on_submit():
        sample = Sample(oem=form.OEM.data, program=form.Program.data, seat_row=form.Seat_Row.data,
                        seat_type=form.Seat_Type.data)
        db.session.add(sample)
        db.session.commit()
        flash('Sample for {} OEM in {} program has been registered'.format(sample.oem, sample.program))
        return redirect(url_for('profile'))
    return render_template('sample_register.html', title='Register Sample', form=form)


@app.route('/test_register/<int:sample_id>', methods=['GET', 'POST'])
@login_required
def test_register(sample_id):
    form = TestRegistrationForm()
    sample = Sample.query.get(sample_id)
    if Test.query.count() == 0:
        sequence_id = 1
    else:
        last_id = Test.query.order_by(desc(Test.id)).first().id
        sequence_id = last_id + 1
    if form.validate_on_submit():
        pulse = Pulse.query.filter_by(severity=form.Pulse.data).first()
        test_data = Test(id=sequence_id, label=form.label.data, pulse_id=pulse.id, sample_id=sample.id)
        result = Result(id=sequence_id, NIC=0, Nkm=0, rebound_velocity=0,
                        Fx_upper_neck=0, Fz_upper_neck=0,
                        T1_acceleration=0, time_head_contact=0, test_id=test_data.id)
        db.session.add_all([result, test_data])
        db.session.commit()
        flash('Test registered successfully!')
        return redirect(url_for('test', id=sequence_id, _external=True, _scheme='http'))
    return render_template('test_register.html', title='Register', form=form)


@app.route('/test/<int:id>', methods=['GET', 'POST'])
@login_required
def test(id):
    test_data = Test.query.get(id)
    result_data = Result.query.get(id)
    pulse_data = Pulse.query.get(Test.query.get(id).pulse_id)
    return render_template('result.html', template_test=test_data, template_result=result_data,
                           template_pulse=pulse_data)


@app.route('/update/<int:id>', methods=['GET', 'POST'])
@login_required
def update(id):
    form = ResultForm()
    result_to_update = Result.query.get_or_404(id)
    test_data = Test.query.get(id)
    if request.method == "POST":
        result_to_update.NIC = request.form['NIC']
        result_to_update.Nkm = request.form['Nkm']
        result_to_update.rebound_velocity = request.form['rebound_velocity']
        result_to_update.Fx_upper_neck = request.form['Fx_upper_neck']
        result_to_update.Fz_upper_neck = request.form['Fz_upper_neck']
        result_to_update.T1_acceleration = request.form['T1_acceleration']
        result_to_update.time_head_contact = request.form['time_head_contact']
        try:
            db.session.commit()
            flash("Result data updated successfully!")
            return redirect(url_for('test', id=id, _external=True, _scheme='http'))
        except:
            flash("Error! Looks like there is a problem.")
            return render_template("update.html", form=form, update_variable=result_to_update,
                                   label_variable=test_data.label)
    else:
        return render_template("update.html", form=form, update_variable=result_to_update,
                               label_variable=test_data.label)


@app.route('/delete_test/<int:id>', methods=['GET', 'POST'])
@login_required
def delete_test(id):
    test_to_delete = Test.query.get_or_404(id)
    try:
        db.session.delete(test_to_delete)
        db.session.commit()
        flash("Test record deleted successfully!")
        all_tests = Test.query.all()
        samples = Sample.query.all()
        pulses = Pulse.query.all()
        return render_template('profile.html', template_tests=all_tests, template_samples=samples,
                               template_pulses=pulses)
    except:
        flash("There was a problem deleting test record.")
        all_tests = Test.query.all()
        samples = Sample.query.all()
        pulses = Pulse.query.all()
        return render_template('profile.html', template_tests=all_tests, template_samples=samples,
                               template_pulses=pulses)
