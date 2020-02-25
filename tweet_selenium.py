from selenium import webdriver
from getpass import getpass
from time import sleep

user = input('Input username or email : ')
pwd = getpass('Input your password : ')
image_path = input('Specify image path : ')

wd = webdriver.Chrome()
wd.get('https://twitter.com/login')

usr_field = wd.find_element_by_class_name('js-username-field')
usr_field.send_keys(user)
sleep(3)

pwd_field = wd.find_element_by_class_name('js-password-field')
pwd_field.send_keys(pwd)
sleep(3)

login_button = wd.find_element_by_css_selector('button.submit.EdgeButton.EdgeButton--primary.EdgeButtom--medium')
login_button.submit()
sleep(3)

img_field = wd.find_element_by_css_selector('input.file-input.js-tooltip')
img_field.send_keys(image_path)
sleep(3)

txt_field = wd.find_element_by_id('tweet-box-home-timeline')
txt_field.send_keys('Sent from Python')
sleep(3)

tweet_btn = wd.find_element_by_css_selector('button.tweet-action.EdgeButton.EdgeButton--primary.js-tweet-btn')
tweet_btn.click()
