import pytest
from pages.login_page import LoginPage

def test_valid_login(driver):
    login = LoginPage(driver)
    login.enter_email("testuser@example.com")
    login.enter_password("TestPassword123")
    login.tap_login()

    assert login.is_home_screen_displayed(), "Login failed: Home screen not displayed"
