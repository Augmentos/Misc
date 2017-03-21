from selenium import webdriver
from random import randint
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import time
import socket
from timeit import default_timer


#-------------------------------------
no_of_questions = 30
total_time = 30
tests=60
username="sharoonkbabu@karunya.edu.in"
password="idiotsheeba111"
#-------------------------------------

driver = webdriver.Firefox()
driver.get("http://aptitude.karunya.edu/index.php")
assert "Aptitude" in driver.title
print 'Aptitude Website is opened'
element = driver.find_element_by_id("email_id")
element.send_keys(str(username))
element = driver.find_element_by_id("password")
element.send_keys(str(password))
element.send_keys(Keys.RETURN)
print 'Loggin in....'
start = default_timer()
REMOTE_SERVER = "www.google.com"
def is_connected():
  try:

    host = socket.gethostbyname(REMOTE_SERVER) 
    s = socket.create_connection((host, 80), 2)
    return True
  except:
     pass
  return False


def func():
    try:
        
        time.sleep(2)
        driver.get("http://aptitude.karunya.edu/user/test/index.php")
        select = Select(driver.find_element_by_name('no_que'))
        select.select_by_visible_text(str(no_of_questions))
        select = Select(driver.find_element_by_name('tot_time'))
        select.select_by_visible_text(str(total_time))

        element = driver.find_element_by_id("subjects")
        all_options = element.find_elements_by_id("subject-inner")
        for option in all_options:
            option.click()
        time.sleep(2)
        driver.find_element_by_id("next").click()
        time.sleep(3)
        driver.find_element_by_id("next").click()
        time.sleep(2)
        q=0
        print 'Attempting Test'
        while(q<no_of_questions):
            time.sleep(5)
            s="ch"
            choice = s+str(randint(1,5))
            driver.find_element_by_id(choice).click()
            driver.find_element_by_xpath("//a[@data-direc='next']").click()
            time.sleep(2)
            q=q+1

        driver.find_element_by_id("submit-test").click()
        alert = driver.switch_to_alert()
        alert.accept()
        time.sleep(2)
        
        test = "Test"+str(t)+".png"
        
        driver.save_screenshot(test)
        print 'Test finished'
        driver.get("http://aptitude.karunya.edu/user/index.php")

    except:
        if not is_connected():
            print 'Waiting for internet connection'
            time.sleep(5)
            func()
            

    
         
test=0
t=1
while(test<tests):
    func()
    t+=1
    test+=1
    print 'Total time taken'+str(default_timer() - start)
driver.close()

