from application import app, db, bcrypt
from flask import render_template, redirect, url_for, request
from application.forms import RegistrationForm, LoginForm, UpdateAccountForm, PurchaseForm
from application.models import Customer, Artist
from flask_login import login_user, current_user, logout_user, login_required

@app.route('/')
@app.route('/home')
def home():
	lineUp = Artist.query.limit(5).all()
	return render_template('home.html', title='Home', artists=lineUp)

@app.route('/about')
def about():
    return render_template('about.html', title='about')
@app.route('/register', methods=['GET', 'POST'])
def register():
	if current_user.is_authenticated:
		return redirect(url_for('home'))
	form = RegistrationForm()
	if form.validate_on_submit():
		hash_pw = bcrypt.generate_password_hash(form.password.data)
		user = Customer(
			first_name=form.first_name.data,
			last_name=form.last_name.data,
			email=form.email.data,
			password=hash_pw
			)
		db.session.add(user)
		db.session.commit()
		return redirect(url_for('login'))

	return render_template('register.html', title='Register', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
	if current_user.is_authenticated:
		return redirect(url_for('home'))
	form = LoginForm()
	if form.validate_on_submit():
		user = Customer.query.filter_by(email=form.email.data).first()
		if user and bcrypt.check_password_hash(user.password, form.password.data):
			login_user(user, remember=form.remember.data)
			next_page = request.args.get('next')
			if next_page:
				return redirect('home')
			else:
				return redirect('home')
	return render_template('login.html', title='Login', form=form)

@app.route('/buy', methods=['GET', 'POST'])
@login_required
def buy():
	form = PurchaseForm()
	return render_template('buy.html', title='Buy', form=form)
			
@app.route('/logout')
@login_required
def logout():
	logout_user()
	return redirect(url_for('login'))

@app.route('/account', methods=['GET', 'POST'])
@login_required
def account():
	form = UpdateAccountForm()
	if form.validate_on_submit():
		current_user.first_name = form.first_name.data
		current_user.last_name = form.last_name.data
		current_user.email = form.email.data
		db.session.commit()
		return redirect(url_for('account'))
	elif request.method == 'GET':
		form.first_name.data = current_user.first_name
		form.last_name.data = current_user.last_name
		form.email.data = current_user.email
	return render_template('account.html', title='Account', form=form)

@app.route("/account/delete", methods=["GET", "POST"])
@login_required
def account_delete():
    user = current_user.id
    account = Customer.query.filter_by(id=user).first()
    logout_user()
    db.session.delete(account)
    db.session.commit()
    return redirect(url_for('login'))
