import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def check_exercise(driver, exercise='follow_line'):
    e = driver.find_element_by_xpath(f'//div[@class="exercise-card" and @card-id="{exercise}"]')
    e.click()
    e = driver.find_element_by_xpath('//button[@id="launch-button"]')
    e.click()
    try:
        while 1: 
            if "Ready" in e.text: break
    except: pass
    e.send_keys(Keys.ENTER)
    e = driver.find_element_by_xpath('//button[@id="console_button"]')
    e.click()

    time.sleep(2)


def main():
    profile = webdriver.FirefoxProfile()
    profile.set_preference("browser.privatebrowsing.autostart", True)
    driver = webdriver.Firefox(firefox_profile=profile)
    driver.implicitly_wait(0.5)
    driver.get("http://0.0.0.0:8000/")

    try:
        check_exercise(driver, 'follow_road')
    except Exception as e:
        print(e)
    finally:
        driver.quit()


if __name__ == "__main__":
    main()
