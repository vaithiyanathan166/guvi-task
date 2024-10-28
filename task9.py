from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()

try:
    driver.get("https://www.saucedemo.com/")

    # Input username
    username = driver.find_element(By.ID, "user-name")
    username.send_keys("standard_user")  # corrected username typo

    # Input password
    password = driver.find_element(By.ID, "password")
    password.send_keys("secret_sauce")  # corrected password typo

    # Submit the form by clicking the login button
    login_button = driver.find_element(By.ID, "login-button")
    login_button.click()

    # Fetch the title of the webpage
    title = driver.title
    print("Title of the webpage:", title)

    # Fetch the current URL of the webpage
    current_url = driver.current_url
    print("Current URL of the webpage:", current_url)

finally:
    # Close the browser 
    driver.quit()

from selenium import webdriver
from selenium.webdriver.common.by import By

# Initialize WebDriver 
driver = webdriver.Chrome()

try:
    # Open the target website
    driver.get("https://www.saucedemo.com/")

    # Input username
    username = driver.find_element(By.ID, "user-name")
    username.send_keys("standard_user")  # corrected username typo

    # Input password
    password = driver.find_element(By.ID, "password")
    password.send_keys("secret_sauce")  # corrected password typo

    # Submit the form by clicking the login button
    login_button = driver.find_element(By.ID, "login-button")
    login_button.click()

    # Fetch the entire content 
    page_source = driver.page_source

    # Save the content to a text file
    with open("webpage_task_11.txt", "w", encoding='utf-8') as file:
        file.write(page_source)

    print("Webpage content saved to 'webpage_task_11.txt'.")

finally:
    # Close the browser 
    driver.quit()

