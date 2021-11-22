from selenium.webdriver import Chrome

def startbrowser():
    global driver
    path = "C:\\Softwares\\Python\\EndtoEndframework\\Library\\chromedriver.exe"
    driver = Chrome(executable_path=path)
    driver.get("http://thetestingworld.com/testings")
    driver.maximize_window()
    return driver
