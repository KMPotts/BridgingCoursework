from selenium import webdriver
from django.test import TestCase
from blog.views import cv

browser = webdriver.Firefox(executable_path='./geckodriver.exe')

class CVTest(TestCase):
    #Katie goes to see if her CV on her site is up to date
    def openPage(self):
        browser.get('http://127.0.0.1:8000/cv')

    #Katie checks that the CV page looks right
    def checkSiteMatch(self):
        found = resolve('/cv')
        self.assertEqual(found, cv)

    #Katie checks that her personal details are on the site

    #Katie checks that her achievements are visible on the site

    #Katie adds a new achievement

    #Katie checks that there is her coding skills listed

    #Katie adds a new coding skill

    #Katie checks her academic record is there

    #Katie adds to her academic record

    #Katie checks her interests are there

    #Katie adds a new interest

    #Katie edits an achievement

    #Katie deletes an achievement

    #Katie edits a coding skill

    #Katie deletes a coding skill

    #Katie edits a part of her academic record

    #Katie deletes part of her academic record

    #Katie edits an interest

    #Katie deletes an interest

    #Katie adds a new section
