from django.contrib.auth import get_user_model
from django.test import TestCase #an extension of Python’s TestCase
from django.urls import reverse, resolve

from .forms import CustomUserCreationForm
from .views import SignupPageView

# Create your tests here.

class CustomUserTests(TestCase):
    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            username='partho',
            email='partho007@gmail.com',
            password='testpass123'
        )

        self.assertEqual(user.username, 'partho')
        self.assertEqual(user.email, 'partho007@gmail.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        User = get_user_model()

        admin_user = User.objects.create_superuser(
            username='superadmin',
            email='superadmin@email.com',
            password='testpass123'
        )

        self.assertEqual(admin_user.username, 'superadmin')
        self.assertEqual(admin_user.email, 'superadmin@email.com')
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)


class SignupPageTests(TestCase):

    def setUp(self):
        url = reverse('signup')
        self.response = self.client.get(url)

    def test_signup_template(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, 'signup.html')
        self.assertContains(self.response, 'Sign Up') # 'Sign Up' String is available on signup.html, so it will return true
        self.assertNotContains(
            self.response, 'Hi there! I should not be on the page.') # given string is not available, so it will return true


    '''
    Next we can test that our CustomUserCreationForm is being used and that the page
    resolves to SignupPageView.
    '''
    def test_signup_form(self):
        form = self.response.context.get('form')
        self.assertIsInstance(form, CustomUserCreationForm) #Test that obj is (or is not) an instance of cls
        self.assertContains(self.response, 'csrfmiddlewaretoken')

    '''
    It checks whether, when a user visits the root of our website's domain, they are
    correctly taken to the SignupPageView. The test simply uses Django's resolve() function
    to match the view callable mapped to the '/accounts/signup/' root location to the known
    view function by their names
    '''
    def test_signup_view(self):
        view = resolve('/accounts/signup/')
        self.assertEqual(
            view.func.__name__,
            SignupPageView.as_view().__name__
        )