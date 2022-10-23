from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
import os
import time

chrome_driver_path = './ChromeDriver/chromedriver'
service = Service(executable_path=chrome_driver_path)
driver = webdriver.Chrome(service=service)

# First we need to log in - We are doing that with Facebook.
driver.get(url="https://tinder.com/app/recs")
driver.maximize_window()
time.sleep(6)
accept_button = driver.find_element(By.CSS_SELECTOR, "div[class='D(f)--ml'] div:nth-child(1) button:nth-child(1)")
accept_button.click()

log_in_button = driver.find_elements(By.CLASS_NAME, 'l17p5q9z')[1]
log_in_button.click()

time.sleep(2)
facebook_log_in = driver.find_element(By.CSS_SELECTOR, 'button[aria-label="Iniciar sesión con Facebook"]')
facebook_log_in.click()

time.sleep(2)
# We will set a tinder_window and a facebook_window to switch them as we need them.
tinder_window = driver.window_handles[0]
facebook_window = driver.window_handles[1]
# Now, we are going to switch
driver.switch_to.window(facebook_window)
time.sleep(2)
accept_cookies_button = driver.find_element(By.CSS_SELECTOR, 'button[class="_42ft _4jy0 _9xo7 _4jy3 _4jy1 '
                                                             'selected _51sy"]')
accept_cookies_button.click()
time.sleep(2)

fb_email = driver.find_element(By.ID, 'email')
fb_email.send_keys(os.environ["EMAIL"])
fb_pass = driver.find_element(By.ID, 'pass')
fb_pass.send_keys(os.environ["PASSWORD"])
log_fb_button = driver.find_element(By.NAME, 'login')
log_fb_button.click()

driver.switch_to.window(tinder_window)

time.sleep(10)
# Tinder is going to ask us if we allow it to access to our location. We'll allow it
allow = driver.find_element(By.CSS_SELECTOR, 'button[class="button Lts($ls-s) Z(0) CenterAlign Mx(a) Cur(p) Tt(u) '
                                        'Ell Bdrs(100px) Px(24px) Px(20px)--s Py(0) Mih(40px) Pos(r) Ov(h) C(#fff) '
                                        'Bg($c-pink):h::b Bg($c-pink):f::b Bg($c-pink):a::b Trsdu($fast) '
                                        'Trsp($background) Bg($g-ds-background-brand-gradient) '
                                        'button--primary-shadow StyledButton Bxsh($bxsh-btn) Fw($semibold) '
                                        'focus-button-style W(225px) W(a) Mstart(8px)"]')

allow.click()
time.sleep(5)

not_interested = driver.find_element(By.CSS_SELECTOR, 'button[aria-label="No me interesa"]')
not_interested.click()
time.sleep(5)



finished = False
while not finished:
    try:
        not_interested_button = driver.find_element(By.CSS_SELECTOR, "div[class='l17p5q9z']")
    except NoSuchElementException:
        try:
            accept_button = driver.find_element(By.CSS_SELECTOR, "button[class='button Lts($ls-s) Z(0) CenterAlign Mx(a) Cur(p) Tt(u) Bdrs(50%) P(0) Fw($semibold) focus-button-style Bxsh($bxsh-btn) Expand Trstf(e) Trsdu($normal) Wc($transform) Pe(a) Scale(1.1):h Scale(.9):a Bgi($g-ds-background-like):a'] span[class='D(b) Expand']")
        except NoSuchElementException:
            time.sleep(4)
        else:
            accept_button.click()
            time.sleep(1)
    else:
        not_interested_button.click()

