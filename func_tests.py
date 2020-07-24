from selenium import webdriver


browser = webdriver.Firefox(executable_path='./geckodriver.exe')
browser.get('http://127.0.0.1:8000/cv')

assert 'Katie' in browser.title
