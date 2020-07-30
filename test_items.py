from selenium import webdriver

def test_add_item_to_basket(browser):
    btn_add_to_basket = browser.find_element_by_css_selector(".btn-add-to-basket")
    assert btn_add_to_basket.is_enabled(), "No button"