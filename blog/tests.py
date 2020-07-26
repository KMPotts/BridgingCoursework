from selenium import webdriver
from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest

from blog.views import cv

class CVTest(TestCase):


    #Katie checks that the CV page looks right
    def test_view_match(self):
        found = resolve('/cv')
        self.assertEqual(found.func, cv)

    #Katie is going on through html
    def test_html_match(self):
        request = HttpRequest()
        response = cv(request)
        html = response.content.decode('utf8')
        self.assertIn('<html>', html)
        self.assertIn('</html>', html)

    def test_exists_header(self):
        request = HttpRequest()
        response = cv(request)
        html = response.content.decode('utf8')
        self.assertIn('<h1>Katie Potts\' Blog</h1>', html)


    #Katie checks that her personal details are on the site
    def test_contact_details(self):
        request = HttpRequest()
        response = cv(request)
        html = response.content.decode('utf8')
        self.assertIn('<h3>Contact Details</h3>', html)

    def test_email(self):
        request = HttpRequest()
        response = cv(request)
        html = response.content.decode('utf8')
        self.assertIn('katie.mae108@gmail.com', html)

    def test_linkedin(self):
        request = HttpRequest()
        response = cv(request)
        html = response.content.decode('utf8')
        self.assertIn('linkedin.com', html)

    #Katie checks that her achievements are visible on the site

    #Katie adds a new achievement
    def test_achievements(self):
        request = HttpRequest()
        response = cv(request)
        html = response.content.decode('utf8')
        self.assertIn('<h3>Achievements</h3>', html)



    #Katie checks that there is her coding skills listed
    def test_coding_skills(self):
        request = HttpRequest()
        response = cv(request)
        html = response.content.decode('utf8')
        self.assertIn('<h3>Coding Skills</h3>', html)

    #Katie adds a new coding skill


    #Katie checks her academic record is there
    def test_academic_record(self):
        request = HttpRequest()
        response = cv(request)
        html = response.content.decode('utf8')
        self.assertIn('<h3>Academics</h3>', html)

    #Katie adds to her academic record

    #Katie checks her interests are there

    #Katie adds a new interest
    def test_interests(self):
        request = HttpRequest()
        response = cv(request)
        html = response.content.decode('utf8')
        self.assertIn('<h3>Other Interests</h3>', html)

    #Katie edits an achievement

    #Katie deletes an achievement

    #Katie edits a coding skill

    #Katie deletes a coding skill

    #Katie edits a part of her academic record

    #Katie deletes part of her academic record

    #Katie edits an interest

    #Katie deletes an interest

    #Katie adds a new section
