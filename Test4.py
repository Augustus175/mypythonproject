# coding=utf-8
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time


def main():
    url = 'http://www.eastmoney.com/'
    # driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get(url)
    a = driver.find_element_by_xpath("/html/body/div[3]/div[5]/div/ul[1]/li[1]/a[1]/strong").click()
    # 选择财富网的财经专栏，点击进去
    print(driver.current_url)  # 打印当前的url
    hand = driver.window_handles  # 获取当前的所有句柄
    print(hand)  # 打印当前的所有句柄
    driver.switch_to_window(hand[1])  # 转换窗口至最高的句柄
    result_url = driver.current_url  # 获取当前句柄之后的url
    print(driver.current_url)  # 打印当前句柄之后的url
    time.sleep(3)
    a = driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div[6]/ul/li[1]/a").click()
    # 获取经济时评那个链接button
    time.sleep(3)
    hand = driver.window_handles
    print(hand)
    driver.switch_to_window(hand[2])
    result_url = driver.current_url
    print(result_url)
    time.sleep(3)


if __name__ == '__main__':
    main()
