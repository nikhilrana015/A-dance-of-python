from selenium import webdriver

# time for pausing between navigation
import time

def submit_assignment(username, password):
    # Using Chrome to access web
    driver = webdriver.Chrome(executable_path="C:\\Users\\hp\\OneDrive\\Desktop\\chromedriver_win32\\chromedriver.exe")
    time.sleep(5)

    # Open the website
    driver.get('https://linkedin.com/')
    time.sleep(5)

    # Locate id and password
    id_box = driver.find_element_by_name('session_key')
    pass_box = driver.find_element_by_name('session_password')

    # Send login information
    id_box.send_keys(username)
    pass_box.send_keys(password)

    i=400
    
    login = driver.find_element_by_xpath('//button[normalize-space()="Sign in"]')
    login.click()

    driver.get('https://www.linkedin.com/in/rajatmw1999/')
    connection = driver.find_element_by_xpath('//span[normalize-space()="More"]')
    connection.click()
    time.sleep(2)
    connect = driver.find_element_by_xpath('//span[normalize-space()="Connect"]')
    connect.click()
    print("reached")
    connect = driver.find_element_by_xpath('//span[normalize-space()="Connect"]')
    connect.click()
    connect = driver.find_element_by_xpath('//span[normalize-space()="Send"]')
    connect.click()
    # contact = driver.find_element_by_xpath('//a[normalize-space()="Contact info"]')
    # contact.click()
    
    

    time.sleep(5)

    while i<100000:
        tweetbox = driver.find_element_by_class_name('public-DraftStyleDefault-block')
        mt  = "I made a python bot! Yay!!!! @TIME " + str(i) + str(i*23)
        tweetbox.send_keys(mt)
        time.sleep(2)
        login = driver.find_element_by_xpath('//span[normalize-space()="Tweet"]')
        login.click()
        i=i+1
        print("Tweet number " , i+1 , " is done")
        time.sleep(2)

    time.sleep(5)
    return

if __name__ == "__main__":
	submit_assignment('eganinjahattori@gmail.com', 'Eganinja@2021')

# I have developed some out-of-the-box software projects using #mern, #python, #DevOps. Looking for a SDE internship at a reputed company. #hiringmanagers pls hve a look @Apple @Microsoft @Twitter @netflix @Facebook @Paytm @Google @hackerrank 
# https://github.com/rajatmw1999 