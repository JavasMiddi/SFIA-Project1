import unittest
import time
from flask import url_for
from urllib.request import urlopen
from os import getenv
from flask_testing import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from application import app, db, bcrypt
from application.models import Customer, Order

# Set test variables for test admin user
test_admin_first_name = "admin"
test_admin_last_name = "admin"
test_admin_email = "admin@email.com"
test_admin_password = "admin2020"
test_admin_ticketNo= "3"

class TestBase(LiveServerTestCase):

    def create_app(self):
        app.config['SQLALCHEMY_DATABASE_URI'] = str(getenv('TEST_DATABASE'))
        app.config['SECRET_KEY'] = getenv('SKEY')
        return app

    def setUp(self):
        """Setup the test driver and create test users"""
        print("--------------------------NEXT-TEST----------------------------------------------")
        chrome_options = Options()
        chrome_options.binary_location = "/usr/bin/chromium-browser"
        chrome_options.add_argument("--headless")
        self.driver = webdriver.Chrome(executable_path="/home/javasmiddleton12/SFIA-Project1/chromedriver", chrome_options=chrome_options)
        self.driver.get("http://localhost:5000")
        db.session.commit()
        db.drop_all()
        db.create_all()

    def tearDown(self):
        self.driver.quit()
        print("--------------------------END-OF-TEST----------------------------------------------\n\n\n-------------------------UNIT-AND-SELENIUM-TESTS----------------------------------------------")

    def test_server_is_up_and_running(self):
        response = urlopen("http://localhost:5000")
        self.assertEqual(response.code, 200)

class TestRegistration(TestBase):
    def test_login_reg_button(self):
        """
        Test that the register button on the login page directs correctly
        """
        # Click register menu link
        self.driver.find_element_by_xpath("/html/body/div/center/a[4]").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("/html/body/center/div/form/div[4]/button").click()
        time.sleep(1)
        
        assert url_for('register') in self.driver.current_url

    def test_registration(self):
        """
        Test that a user can create an account using the registration form
        if all fields are filled out correctly, and that they will be 
        redirected to the login page
        """
        # Click register menu link
        self.driver.find_element_by_xpath("/html/body/div/center/a[5]").click()
        time.sleep(1)

        # Fill in registration form
        self.driver.find_element_by_xpath('//*[@id="email"]').send_keys(test_admin_email)
        self.driver.find_element_by_xpath('//*[@id="first_name"]').send_keys(
            test_admin_first_name)
        self.driver.find_element_by_xpath('//*[@id="last_name"]').send_keys(
            test_admin_last_name)
        self.driver.find_element_by_xpath('//*[@id="password"]').send_keys(
            test_admin_password)
        self.driver.find_element_by_xpath('//*[@id="confirm_password"]').send_keys(
            test_admin_password)
        self.driver.find_element_by_xpath('//*[@id="submit"]').click()
        time.sleep(1)

        assert url_for('register') in self.driver.current_url
    
class TestLogin(TestBase):
    def test_login(self):
        """
        Test that a user can log into an account using the login form
        if all fields are filled out correctly, and that they will be 
        redirected to the home page
        """
        # Click login menu link
        self.driver.find_element_by_xpath("/html/body/div/center/a[4]").click()
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="email"]').send_keys(test_admin_email)
        self.driver.find_element_by_xpath('//*[@id="password"]').send_keys(
            test_admin_password)
        self.driver.find_element_by_xpath('//*[@id="submit"]').click()
        time.sleep(1)
        # Assert that browser redirects to home page
        assert url_for('home') in self.driver.current_url

    def test_order(self):
        """
        Test access to order page - can view account page
        """
        self.driver.find_element_by_xpath("/html/body/div/center/a[4]").click()
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="email"]').send_keys(test_admin_email)
        self.driver.find_element_by_xpath('//*[@id="password"]').send_keys(
            test_admin_password)
        self.driver.find_element_by_xpath('//*[@id="submit"]').click()
        time.sleep(1)
        assert url_for('home') in self.driver.current_url

        self.driver.find_element_by_xpath("/html/body/div[1]/center/a[4]").click()
        assert url_for('account') in self.driver.current_url

    def test_add_order(self):     
        """
        Test to add order
        """
        self.driver.find_element_by_xpath("/html/body/div/center/a[4]").click()
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="email"]').send_keys(test_admin_email)
        self.driver.find_element_by_xpath('//*[@id="password"]').send_keys(
            test_admin_password)
        self.driver.find_element_by_xpath('//*[@id="submit"]').click()
        assert url_for('home') in self.driver.current_url
        
        self.driver.find_element_by_xpath("/html/body/div/center/a[3]").click()
        
        # Fill in order form
        self.driver.find_element_by_xpath('//*[@id="first_name"]').send_keys(test_admin_first_name)
        self.driver.find_element_by_xpath('//*[@id="last_name"]').send_keys(test_admin_last_name)
        self.driver.find_element_by_xpath('//*[@id="email"]').send_keys(test_admin_email)
        self.driver.find_element_by_xpath('//*[@id="confirm_email"]').send_keys(test_admin_email)
        self.driver.find_element_by_xpath('//*[@id="tickets"]').send_keys(test_admin_ticketNo)
        self.driver.find_element_by_xpath('//*[@id="submit"]').click()
        assert url_for('account_orders') in self.driver.current_url

if __name__ == '__main__':
    unittest.main(port=5000)
