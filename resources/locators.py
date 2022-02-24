from selenium.webdriver.common.by import By

# Common Strings
config_path = 'config.json'
accept_cookies = "#uc-center-container > div:nth-child(2) > div > div > div > button:nth-child(5)"
invalid_voucher_code = "Es tut uns Leid! Der Gutscheincode ist nicht verfügbar."
anchor_tag = "a"
link_attribute = "href"

# Home Page Locators
perfume_menu = (By.CSS_SELECTOR, "[href='/parfum/']")
makeup_menu = (By.CSS_SELECTOR, "[href='/make-up/']")
makeup_menu_sub_section_links = (By.CSS_SELECTOR, "[href='/make-up/'] + ul a")

# Product Page Locators
list_of_products = (By.XPATH, "//div[contains(@class, 'ProductItemVerticalstyle__ImageContainer')]")

# Product Detail Page Locators
add_to_cart_button = (By.CSS_SELECTOR, "[class^='PDPActionBarstyle__Buttons']>button:last-child")

# Cart Page Locators
cart_icon = (By.XPATH, "//a[@data-track-id='basketIcon']")
cart_quick_overview_close_button = (By.XPATH, "//button[contains(@class, 'CloseButton')]")
voucher_code = (By.ID, "voucherCode")
submit_voucher_button = (By.XPATH, "//button[contains(@class, 'VoucherFormstyle') and @type = 'submit']")
voucher_code_message = (By.XPATH, "//div[contains(@class, 'NotificationInlinestyle__Message')]")
