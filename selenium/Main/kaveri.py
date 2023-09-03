from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import secret



# Initialise Username
username = secret.username
password = secret.password

# Navigate Selenium to ChromeDriver
driver = webdriver.Chrome(executable_path='drivers\chromedriver.exe')  # Provide the path to your chromedriver executable

#  Navigate ChromeDriver to Kaveri Online Services
driver.get("https://kaveri.karnataka.gov.in/landing-page")
time.sleep(6)


#initial Login Button
initial_login_button = driver.find_element(By.XPATH, "//button[text()='Login']")
initial_login_button.click()
time.sleep(3)


# Enter Username and Password
username_field = driver.find_element(By.ID, "userName")
username_field.send_keys(username)

password_field = driver.find_element(By.ID, "password")
password_field.send_keys(password)


#enter Captcha
user_input = input("enter Captcha:  ")

captcha_field = driver.find_element(By.ID, "loginCaptchaUserInput1")
captcha_field.send_keys(user_input)


#Click Log in
login_field = driver.find_element(By.XPATH, "/html/body/div[1]/app-root/div/app-landing-page/main[1]/div[2]/div/div[2]/div/div[2]/form/div[4]/button")
login_field.click()

#Enter OTP
otp = int(input("enter OTP:   "))

otp_field = driver.find_element(By.ID, "otp")
otp_field.send_keys(otp) 


#Final Login Button
final_login_field = driver.find_element(By.XPATH, "/html/body/div[1]/app-root/div/app-landing-page/main[1]/div[2]/div/div[2]/div/div[2]/form/div[4]/div[2]/button")
final_login_field.click()






#To Keep the Browser from Closing
input("Press Enter to logout...")

logout_button = driver.find_element(By.XPATH, "/html/body/div[1]/app-root/div/app-kaveri-dashboard/app-header/ul/li[5]/button")
logout_button.click()

input("Press Enter to close browser...")
# Close the browser
driver.quit()

