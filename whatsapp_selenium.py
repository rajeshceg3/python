from selenium import webdriver

wd = webdriver.Chrome()
wd.get('https://web.whatsapp.com/')

name = input('Input Person or Group name : ')
content = input('Type you text : ')
count = int(input('Specify the count : '))

input('Authenticate with QR code and then give input')

user = wd.find_element_by_xpath('//span[@title = "{}"]'.format(name))
user.click()

content_box = wd.find_element_by_class_name('_3u328')

for i in range(count):
    content_box.send_keys(content)
    button = wd.find_element_by_class_name('_3M-N-')
    button.click()
