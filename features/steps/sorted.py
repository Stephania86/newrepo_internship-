from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

#User can sort products by average rating

#1st product has rating starts displayed after sorting

#User can click through product pages after sorting is done (1, 2, > buttons under product catalog)

#Url https://gettop.us/shop/?orderby=rating opens page with results sorted by Rating

#intern Work · Stephania86/newrepo_internship-@479d732 · GitHub


@given('Open Gettop Website')
def open_gettop_page(context):
    context.driver.find_element('https://gettop.us/shop/')

@when('Verify User can sort products by average rating')
def verify_user_can(context):
    context.driver.find_element(By.XPATH, '//option[@value="rating"]').click()


@when('Verify 1st product has rating starts displayed after sorting')
def verify_user_can_see(context):
    context.driver.find_element(By.XPATH, "//div[@class='star-rating']")


@when('Verify User can click through product pages after sorting is done (1, 2, > buttons under product catalog)')
def verify_user_can_click(context):
    if len(context.driver.find_elements(By.XPATH, "//div[@class='image-fade_in_back']")) == 1:
        # Click on Size DD
        context.driver.find_element(By.ID, 'size_name_4')
        # Click on 2nd size option
        context.driver.find_element(By.ID, 'native_dropdown_selected_size_name').click()
        sleep(3)
        # Click on add to cart
        context.driver.find_element(By.ID, 'verify_user_can_click').click()


@then('Verify Url https://gettop.us/shop/?orderby=rating opens page with results sorted by Rating')
def verify_user_can_rate(context):
    url = 'https://gettop.us/shop/?orderby=rating'
    current_url = context.driver.current_url
    assert url == current_url, f'expected {url}, but got {current_url}'
