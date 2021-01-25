import unittest
from flask import url_for
from flask_testing import TestCase
from InstaPic import create_app
import json

class SettingBase(TestCase):
    def create_app(self):
        return create_app()

    def setUp(self):
        self.username = "test"
        self.passwords = "test"

    def signup(self):
        response = self.client.post(url_for('InstaPic.login'),
                                    follow_redirects=True,
                                    json={
                                        "username": self.username,
                                        "password": self.passwords,
                                    })
        return response

    def regAccount(self):
        response = self.client.post(url_for('InstaPic.registration'),
                                    follow_redirects=True,
                                    json={
                                        "username": self.username,
                                        "password": self.passwords,
                                    })
        return response

    def signout(self):
        response = self.client.post(url_for('InstaPic.logout'),follow_redirects=True)
        return response



class LoginPage(SettingBase):
    def test_signup(self):
        response = self.signup()
        self.assertEqual(response.status_code, 200)

    def test_signup_400(self):
        self.passwords = '123'
        self.client.post('/InstaPic/login', data=dict(username=self.username, password=self.passwords))
        self.assert_template_used('login.html')
        self.assert_context("msg", "Wrong username or password")

    def test_logout(self):
        response = self.signout()
        self.assertEqual(response.status_code, 200)

    def test_registed(self):
        self.passwords = '123'
        self.client.post('/InstaPic/registration', data=dict(username=self.username, password=self.passwords))
        self.assert_template_used('registration.html')
        self.assert_context("msg", "The username has been registered")

    def test_invalidUsername(self):
        self.username = '(*&^%)'
        self.client.post('/InstaPic/registration', data=dict(username=self.username, password=self.passwords))
        self.assert_template_used('registration.html')
        self.assert_context("msg", "Username must only contain characters and numbers")

    def test_regSuccess(self):
        self.username = 'test2'
        response = self.signup()
        self.assertEqual(response.status_code, 200)



if __name__ == '__main__':
    unittest.main()
