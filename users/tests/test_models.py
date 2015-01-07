from django.test import TestCase
from model_mommy import mommy
from users.models import User


class UserTestModel(TestCase):
    """
        Class to test the model User
    """

    def setUp(self):
        self.user = mommy.prepare(User)

    def test_unicode(self):
        """
        Tests that str(user) takes into account username, first name, and last name.
        """
        self.assertEqual(str(self.user), "")
        self.user.first_name = "FirstName"
        self.assertEqual(str(self.user), "FirstName")
        self.user.last_name = "LastName"
        self.assertEqual(str(self.user), "FirstName LastName")
        self.user.first_name = None
        self.assertEqual(str(self.user), "LastName")
        self.user.username = "mrfirstlast"
        self.assertEqual(str(self.user), "mrfirstlast")
