
from selenium import webdriver

def test_selenium():
    dr = webdriver.Chrome()
    dr.get("https://www.baidu.com/")