from django.test import TestCase


class TemplatePageTests(TestCase):
    def test_home_displays_home_template_at_root(self):
        response = self.client.get("/")

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "gallery/home.html")
        self.assertContains(response, "Discover moments.")

    def test_login_displays_login_template(self):
        response = self.client.get("/login/")

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "gallery/login.html")
        self.assertContains(response, "Welcome Back")
