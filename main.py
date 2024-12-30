from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert
import time
# edge_options.add_argument("--disable-notifications")
# edge_options.page_load_strategy = 'eager'

class instagram_bot:
  def __init__(self):
    self.edge_options = webdriver.EdgeOptions()
    self.edge_options.add_experimental_option("detach", True)
    self.edge_options.add_argument("--disable-notifications")
    self.service = Service("C:\webdrivers\msedgedriver.exe")
    self.driver = webdriver.Edge(options=self.edge_options, service=self.service)

  def log_in(self):
    self.driver.get("https://www.instagram.com/#")
    time.sleep(2)
    try:
      allow = self.driver.find_element(By.XPATH, value="/html/body/div[5]/div[1]/div/div[2]/div/div/div/div/div[2]/div/button[1]").click()
    except:
        print("no element found 26")
    try:
      allow = self.driver.find_element(By.XPATH, value="/html/body/div[4]/div[1]/div/div[2]/div/div/div/div/div[2]/div/button[1]")
    except:
      print("no element found")
    try:
      allow = self.driver.find_element(By.XPATH, value="/html/body/div[3]/div[1]/div/div[2]/div/div/div/div/div[2]/div/button[1]").click()
    except:
      print("no element found 31")
    try:
      allow = self.driver.find_element(By.XPATH, value="/html/body/div[4]/div[1]/div/div[2]/div/div/div/div/div[2]/div/button[1]").click()
    except:
      print("no element found 36")


    username = self.driver.find_element(By.XPATH, value="/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div/section/main/article/div[2]/div[1]/div[2]/div/form/div[1]/div[1]/div/label/input").send_keys("szymonbryniak8@gmail.com")
    password = self.driver.find_element(By.XPATH, value="/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div/section/main/article/div[2]/div[1]/div[2]/div/form/div[1]/div[2]/div/label/input").send_keys("Password_12354!")
    time.sleep(2)
    log_in = self.driver.find_element(By.XPATH, value="/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div/section/main/article/div[2]/div[1]/div[2]/div/form/div[1]/div[3]/button").click()
    time.sleep(5)
    # not_now = self.driver.find_element(By.XPATH, value="/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div[1]/div[1]/section/main/div/div/div/div/div").click()
    try:
      not_now = self.driver.switch_to.active_element.find_element(By.XPATH, value="/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div[1]/div[1]/section/main/div/div/div/div/div").click()
    except:
      not_now = self.driver.switch_to.active_element.find_element(By.XPATH, value="/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/button[2]").click()
    try:
      not_now = self.driver.switch_to.active_element.find_element(By.XPATH, value="/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div[1]/div[1]/section/main/div/div/div/div/div").click()
    except:
      print('not now not found')


  def get_followers(self):
    self.driver.get("https://www.instagram.com/maplestory/")
    time.sleep(3)
    followers = self.driver.find_element(By.XPATH, value="/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div[2]/div/div[1]/section/main/div/header/section[3]/ul/li[2]/div/a").click()
    time.sleep(5)
    self.driver.switch_to.active_element
    button_list = self.driver.find_elements(By.TAG_NAME, value="button")
    print(len(button_list))

    # button = self.driver.find_element(By.XPATH, value="/html/body/div[5]/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div[2]/div/div[1]/div/div/div/div[3]/div/button")
    # # self.driver.execute_script("arguments[0].scrollIntoView();", button)
    # WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(button))
    # button.click()
    # time.sleep(3)
    # cancel = self.driver.find_element(By.XPATH, value="/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div/div/button[2]").click()
    for button in range(len(button_list)):

      self.driver.switch_to.active_element
      time.sleep(3)
      try:
        # button = self.driver.find_element(By.XPATH, value="/html/body/div[5]/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div[2]/div/div[1]/div/div/div/div[3]/div/button")
        # button = self.driver.find_element(By.TAG_NAME, value="button")
        button = self.driver.find_element(By.XPATH, value=f"/html/body/div[5]/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div[2]/div/div[{button+1}]/div/div/div/div[3]/div/button")
        # self.driver.execute_script("arguments[0].scrollIntoView();", button)
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(button))
        button.click()
        time.sleep(2)
        self.driver.execute_script("arguments[0].scrollIntoView();", button)
      except:
        print("Button exception")

      time.sleep(2)
      self.driver.switch_to.active_element
      try:
        OK = self.driver.find_element(self.driver.find_element(By.XPATH, value="/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/button[2]")).click()
      except:
        print("OK 1 not found")

      time.sleep(2)
      try:
        OK = self.driver.find_element(self.driver.find_element(By.XPATH, value="/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/button[2]")).click()
      except:
        print('Ok 2 not found')
        time.sleep(2)
      try:
        OK = self.driver.switch_to.active_element.find_element(self.driver.file_detector(By.XPATH, value="/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/button[2]")).click()
      except:
        print('Button exception 3')
      time.sleep(2)
     
      try:
        cancel = self.driver.find_element(By.XPATH, value="/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div/div/button[2]").click()
      except:
        print('cancel not found')
      
      
    # time.sleep(3)
    # for i in range(20):
    #   time.sleep(5)
    #   test_click = self.driver.find_element(By.XPATH, value="/html/body/div[5]/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div[2]/div/div[1]/div/div/div/div[3]/div/button").click()
    #   time.sleep(2)
    #   cancel = self.driver.find_element(By.XPATH, value="/html/body/div [6]/div[1]/div/div[2]/div/div/div/div/div/div/button[2]").click()


bot = instagram_bot()
bot.log_in()
bot.get_followers()
