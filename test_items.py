from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_add_to_basket_button_is_present(browser):
    browser.get(link)
    
    add_to_basket_button = browser.find_elements(By.CSS_SELECTOR, "button.btn-add-to-basket")
    
    assert len(add_to_basket_button) > 0, "Add to basket button is not present on the page"
    
    assert add_to_basket_button[0].is_displayed(), "Add to basket button is not visible"
    assert add_to_basket_button[0].is_enabled(), "Add to basket button is not enabled"