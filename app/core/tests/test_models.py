from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):
    def test_create_user_with_email_successful(self):
        email = 'raheel@gmail.com'
        password = 'test123'
        user = get_user_model().objects.create_user(
            email = email,
            password = password
        )
        self.assertEqual(user.email,email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """ Test Normalized Email"""
        email = 'raheel@GMAIL.com'

        user = get_user_model().objects.create_user(
            email,
            'test123'
        )

        self.assertEqual(user.email, email.lower())
    
    def test_email_is_not_blank(self):
        """ checks if the email is """

        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(
                None,
                'test123'
            )
    def test_create_new_super_user(self):
        """ Testing creating a super user"""
        user = get_user_model().objects.create_superuser(
            'rawheel@github.com',
            'test123'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)