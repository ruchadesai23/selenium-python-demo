from pages.login import Login
from testdata.login_page_data import vars
import pytest

def test_valid_login():
    obj = Login()
    obj.launch_website(vars["url"])
    res = obj.user_creds(vars["username"],vars["password"])
    assert res == 1
    
def test_hometitle():
    obj = Login()
    obj.launch_website(vars["url"])
    obj.user_creds(vars["username"],vars["password"])
    res = obj.page_title()
    assert res == 1



