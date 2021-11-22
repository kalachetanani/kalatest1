from Base import Initiatedriver

def test_invalid_data():
    driver=Initiatedriver.startbrowser()
    driver.find_element_by_name("fld_password").send_keys("abcd")
    driver.close()

