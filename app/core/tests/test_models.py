from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """ test1 """
        email = "test@tat.com"
        password = "test123"
        user = get_user_model().objects.create_user(
           email=email,
           password=password
        )
        print("test1 ok")
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normal(self):
        """ norm email"""
        email = "test@TAT.com"
        user = get_user_model().objects.create_user(email, "test123")
        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """ val email"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, "test123")

    def test_create_new_superuser(self):
        """ test for super"""
        user = get_user_model().objects.create_superuser('test@tt.com', 't123')

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
