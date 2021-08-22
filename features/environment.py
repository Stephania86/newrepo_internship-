from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.events import EventFiringWebDriver
#from app.application import Application
#from support.logger import logger


# Register for BrowserStack, then grab it from https://www.browserstack.com/accounts/settings
bs_user = 'stephaniapetitho_9WoegK'
bs_pw = 'LDebVjbzduLFRFRYf7aU'


def browser_init(context):
    """
    :param context: Behave context
    """
    #context.driver = webdriver.Chrome("C:\\Users\\HP\\Desktop\\newrepo_internship-\\chromedriver.exe")
    #context.browser = webdriver.Safari()
    #context.browser = webdriver.Firefox("C:\\Users\\HP\\Desktop\\newrepo_internship-\\geckodriver.exe")
    ### HEADLESS MODE ####
    # options = webdriver.ChromeOptions()
    # options.add_argument('--headless')
    # context.driver = webdriver.Chrome(chrome_options=options)


### for browerstack ###
    desired_cap = {
         'browser': 'Firefox',
         'browser_version': '91',
         'os': 'Windows',
         'os_version': '10',
         #'name': test_name
    }
    url = f'http://{bs_user}:{bs_pw}@hub-cloud.browserstack.com/wd/hub'
    context.driver = webdriver.Remote(url, desired_capabilities=desired_cap)

    context.driver.maximize_window()
    context.driver.implicitly_wait(4)

def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    browser_init(context)


def before_step(context, step):
    print('\nStarted step: ', step)


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)


def after_scenario(context, feature):
    context.driver.delete_all_cookies()
    context.driver.quit()
