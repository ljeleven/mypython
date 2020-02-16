#__author:"longjin"
#date:  2018/7/28
from selenium import webdriver
#create a new firefox session
chromedriver = 'C:/Program Files (x86)/Google/Chrome/Application/chromedriver'
driver = webdriver.Chrome(chromedriver)
driver.implicitly_wait(30)
driver.maximize_window()

#navigate to the application home page
driver.get('https://www.baidu.com/')

#get the search textbox
search_field = driver.find_element_by_name('wd')
search_field.clear()

#enter search keyword and submit
search_field.send_keys('phones')
search_field.submit()

#get all the anchor elemens which have producr names displayed
#currently on result page using find_element_by_xpath method
products = driver.find_elements_by_xpath("//h3[@class='t']/a")


#get the number of anchor elements found
print('found'+str(len(products))+'products:')

#iterate through each anchor element and print the text that is
#name of the product
for product in products:
    print(product.text)

#close the browser window
driver.quit()
