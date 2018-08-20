"""
Author: Erik Djamgarian

A little python script that asks the user for a url input (full url) and opens a Chrome webbrowser with the url input.

"""


import os
from selenium import webdriver

# pass the file path to a variable
chromedriver = "/usr/local/bin/chromedriver"
#using os module to compile path with driver?
#os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(chromedriver)
url = input("Please type in your url > ")
driver.get(f"{url}")
# driver.quit()
