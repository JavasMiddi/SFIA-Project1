import unittest
from flask import url_for
from flask_testing import TestCase
from application import app, db, bcrypt
from application.models import Customer, Order, Artist
from os import getenv

class TestBase(TestCase):
	def create_app(self):
		# pass in configurations for test database
		config_name = 'testing'
		app.config.update(SQLALCHEMY_DATABASE_URI=getenv('TEST_DB_URI'),
				SECRET_KEY=getenv('TEST_SECRET_KEY'),
				WTF_CSRF_ENABLED=False,
				DEBUG=True
				)
		return app
	def setUp(self):
		"""
		Will be called before every test
		"""
		# ensure there is no data in the test database when the test starts
		db.session.commit()
		db.drop_all()
		db.create_all()
		# create test admin user
		hashed_pw = bcrypt.generate_password_hash('admin2016')
		admin = Customer(first_name="admin", last_name="admin", email="admin@admin.com", password=hashed_pw)
		# create test non-admin user
		hashed_pw_2 = bcrypt.generate_password_hash('test2016')
		employee = Customer(first_name="test", last_name="user", email="test@user.com", password=hashed_pw_2)
		# save users to database
		db.session.add(admin)
		db.session.add(employee)
		db.session.commit()
	def tearDown(self):
		"""
		Will be called after every test
		"""
		db.session.remove()
		db.drop_all()

class TestViews(TestBase):
	def test_homepage_view(self):
		"""
		Test that homepage is accessible without login
		"""
		response = self.client.get(url_for('home'))
		self.assertEqual(response.status_code, 200)
	def test_about(self):
		response = self.client.get(url_for('about'))
		self.assertEqual(response.status_code, 200)
	def test_login(self):
                response = self.client.get(url_for('login'))
                self.assertEqual(response.status_code, 200)

class TestBuyAccess(TestBase):
    def test_access_buy_page(self):
        """
        Test if you try to access the buy page while logged out
	 """
        with self.client:
            response = self.client.post(url_for('buy'),
                follow_redirects=True)
            self.assertIn(b'Login', response.data)

class TestLogin(TestBase):
	def test_login(self):
		"""
		Test that when I login, I am redirected to the homepage
		"""
		with self.client:
			self.client.get(url_for('login'), data=dict(
			email="admin@admin.com", password="admin2016"), 
			follow_redirects=True)
	def test_account(self):
                with self.client:
                        self.client.get(url_for('account'), follow_redirects=True)

class TestLogout(TestBase):
    def test_logout(self):
        self.client.post(
                url_for('login'), data=dict(email='admin@admin.com',
                    password='admin2016'), follow_redirects=True)
        self.client.post(url_for('account'), follow_redirects=True)
        response = self.client.get(url_for('account'))
        self.assertIn(b'admin',response.data)

class TestAccountDelete(TestBase):
    def test_delete_account(self):
        self.client.post(
                url_for('login'), data=dict(email='admin@admin.com',
                    password='admin2016'), follow_redirects=True)
        self.client.post(url_for('account'), follow_redirects=True)
        self.client.post(url_for('account_delete'), follow_redirects=True)
        response = self.client.get(url_for('login'))
        self.assertIn(b'Login',response.data)

class TestRegistration(TestBase):
    def test_register_account(self):
        self.client.post(
            url_for('register'), data=dict(first_name='firsttest',
                last_name='lasttest', email='test@test.com',
                password='test', confirm_password='test'),
            follow_redirects=True)
        response=self.client.get('login')
        self.assertIn(b'Login',response.data)

