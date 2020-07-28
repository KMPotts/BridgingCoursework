from selenium import webdriver
from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest

import blog.views as views

class CVTest(TestCase):


    #Katie checks that the CV page looks right
    def test_view_match(self):
        found = resolve('/cv')
        self.assertEqual(found.func, views.cv)

    #Katie is going on through html
    def test_html_match(self):
        request = HttpRequest()
        response = views.cv(request)
        html = response.content.decode('utf8')
        self.assertIn('<html>', html)
        self.assertIn('</html>', html)

    def test_exists_header(self):
        request = HttpRequest()
        response = views.cv(request)
        html = response.content.decode('utf8')
        self.assertIn('<h1>Katie Potts\' Blog</h1>', html)


    #Katie checks that her personal details are on the site
    def test_contact_details(self):
        request = HttpRequest()
        response = views.cv(request)
        html = response.content.decode('utf8')
        self.assertIn('<h3>Contact Details</h3>', html)

    def test_email(self):
        request = HttpRequest()
        response = views.cv(request)
        html = response.content.decode('utf8')
        self.assertIn('katie.mae108@gmail.com', html)

    def test_linkedin(self):
        request = HttpRequest()
        response = views.cv(request)
        html = response.content.decode('utf8')
        self.assertIn('linkedin.com', html)

    #Katie checks that her achievements are visible on the site
    def test_achievements(self):
        request = HttpRequest()
        response = views.cv(request)
        html = response.content.decode('utf8')
        self.assertIn('<h3>Other Achievements</h3>', html)


    #Katie adds a new achievement
    def test_view_add_achievement(self):
        found = resolve('/cv/new_achievement')
        self.assertEqual(found.func, views.achievement_edit)

    def test_achievements_form(self):
        request = HttpRequest()
        response = views.achievement_edit(request)
        html = response.content.decode('utf8')
        self.assertIn('<form method="POST" class="achievement-form">', html)

    #Katie checks that there is her coding skills listed
    def test_coding_skills(self):
        request = HttpRequest()
        response = views.cv(request)
        html = response.content.decode('utf8')
        self.assertIn('<h3>Coding Skills</h3>', html)

    #Katie adds a new coding skill
    def test_view_add_coding(self):
        found = resolve('/cv/new_coding')
        self.assertEqual(found.func, views.coding_edit)

    def test_coding_form(self):
        request = HttpRequest()
        response = views.coding_edit(request)
        html = response.content.decode('utf8')
        self.assertIn('<form method="POST" class="coding-form">', html)


    #Katie checks her academic record is there
    def test_academic_record(self):
        request = HttpRequest()
        response = views.cv(request)
        html = response.content.decode('utf8')
        self.assertIn('<h3>Academics</h3>', html)

    #Katie adds to her academic record
    def test_view_add_academic(self):
        found = resolve('/cv/new_academic')
        self.assertEqual(found.func, views.academic_edit)

    def test_academics_form(self):
        request = HttpRequest()
        response = views.academic_edit(request)
        html = response.content.decode('utf8')
        self.assertIn('<form method="POST" class="academic-form">', html)

    #Katie checks her interests are there
    def test_interests(self):
        request = HttpRequest()
        response = views.cv(request)
        html = response.content.decode('utf8')
        self.assertIn('<h3>Other Interests</h3>', html)

    #Katie adds a new interest
    def test_view_add_interest(self):
        found = resolve('/cv/new_interest')
        self.assertEqual(found.func, views.interest_edit)

    def test_interests_form(self):
        request = HttpRequest()
        response = views.interest_edit(request)
        html = response.content.decode('utf8')
        self.assertIn('<form method="POST" class="interest-form">', html)

    #Katie edits an achievement

    #Katie deletes an achievement

    #Katie edits a coding skill

    #Katie deletes a coding skill

    #Katie edits a part of her academic record

    #Katie deletes part of her academic record

    #Katie edits an interest

    #Katie deletes an interest

    #Katie adds a new section
