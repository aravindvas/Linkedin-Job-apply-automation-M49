import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

idown = 150
iup = 10
tw_usr = ""
tw_ps = ""
chr_drvr = "D:\Softwares\chromedriver_win32\chromedriver.exe"

class InternetSpeedTwitterBot:
    def __init__(self, path):
        self.drvr = webdriver.Chrome(executable_path=path)
        self.up = 0
        self.down = 0

    def get_spd (self):
        self.drvr.get(url="https://www.speedtest.net/")
        time.sleep(3)
        gob = self.drvr.find_element_by_css_selector(".start-button a")
        gob.click()
        time.sleep(60)
        self.up = self.drvr.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
        self.down = self.drvr.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span').text

    def tweet(self):
        # time.sleep(3)
        self.drvr.get(url="https://twitter.com/login")
        time.sleep(2)
        em = self.drvr.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[1]/label/div/div[2]/div/input')
        ps = self.drvr.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[2]/label/div/div[2]/div/input')
        em.send_keys(tw_usr)
        ps.send_keys(tw_ps)
        time.sleep(2)
        ps.send_keys(Keys.ENTER)
        time.sleep(5)
        tw_cmps = self.drvr.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div/div/div/div')
        msg = f"Hey Internet Provider, why is my internet speed {self.down}down/{self.up}up when I pay for {idown}down/{iup}up?"
        tw_cmps.send_keys(msg)
        time.sleep(3)
        tbut = self.drvr.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]')
        tbut.click()

        time.sleep(3)
        self.drvr.quit()




bot = InternetSpeedTwitterBot(chr_drvr)
bot.get_spd()
bot.tweet()