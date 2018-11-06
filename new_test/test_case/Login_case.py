import unittest,sys
sys.path.append("./models")
sys.path.append("./page_object")
from models import myunit, function
from page_object.Login_page import login
from time import sleep


class loginTest(myunit.Mytest):
    def test_login1(self):
        po = login(self.driver)
        sleep(5)
        po.login('admin')


if __name__ == "__main__":
    unittest.main()