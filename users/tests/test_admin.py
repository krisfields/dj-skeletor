from django.test import TestCase
from model_mommy import mommy
from users.models import User
from users.admin import UserAdmin
from django.contrib.admin.sites import AdminSite


class UserAdminTestModelAdmin(TestCase):

    """
    Class to test the adminModel UserAdmin
    """

    def setUp(self):
        self.user_admin = UserAdmin(User, AdminSite())
        self.user = mommy.prepare(User)

    def test_email_image(self):
        """
        Tests that image and email displays if object has image, else just
        email.
        """
        self.assertEqual(self.user_admin.email_image(self.user), self.user.email)
        self.user.image = "ui/shop_image.jpg"
        self.user.save()
        self.assertEqual(self.user_admin.email_image(self.user),
                         u'<img width="100px" src="%s"><br />%s' % (self.user.image.url, self.user.email))
