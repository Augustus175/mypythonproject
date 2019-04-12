# coding=utf-8
import time
from splinter import Browser
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


def login_mail(url):
    # browser = Browser()

    # driver = webdriver.Chrome()

    # browser = webdriver.Chrome("C:/Program Files (x86)/Google/Chrome/Application/chromedriver.exe")

    browser = webdriver.Chrome(ChromeDriverManager().install())
    # browser = Browser('chrome')
    # login 163 email websize
    browser.get(url)
    # wait web element loading
    # fill in account and password
    # html= browser.find_element_by_xpath(url)
    # browser.find_element_by_id('account-box').fill('columbia7312@163.com')
    # browser.find_element_by_id('password').fill('123456')
    # browser.find_element_by_id('password').fill('123456')
    browser.find_element_by_id("kw").send_keys(u"四大名著")
    browser.find_element_by_id("su").click()
    # click the button of login
    browser.find_element_by_id('dologin').click()
    time.sleep(5)
    # close the window of brower
    browser.quit()


if __name__ == '__main__':
    # mail_addr = 'http://reg.163.com/'
    # mail_addr = "https://m.reg.163.com/login.html?curl=https%3A%2F%2Fm.reg.163.com%2F%23%2Femail"
    mail_addr = "http://www.baidu.com/"
    login_mail(mail_addr)
