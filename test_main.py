import allure
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@allure.feature('Menu Navigation')
@allure.suite('UI Tests')
@allure.title('Test Menu Item Navigation')
@allure.description('Verifies that each menu item on the homepage navigates to the correct page and displays the correct heading.')
@allure.severity(allure.severity_level.CRITICAL)
def test_menu_item(driver):
    with allure.step("Opening the homepage"):
        driver.get("https://tutorialsninja.com/demo/")

    expected_menu_items = ["Desktops", "Laptops & Notebooks", "Components", "Tablets", "Software", "Phones & PDAs", "Cameras", "MP3 Players"]

    with allure.step(f"Clicking on menu item: {expected_menu_items[0]}"):
        menu_items1 = driver.find_element(By.LINK_TEXT, expected_menu_items[0])
        menu_items1.click()

    with allure.step(f"Clicking on menu item: {expected_menu_items[1]}"):
        menu_items2 = driver.find_element(By.LINK_TEXT, expected_menu_items[1])
        menu_items2.click()

    with allure.step(f"Clicking on menu item: {expected_menu_items[2]}"):
        menu_items3 = driver.find_element(By.LINK_TEXT, expected_menu_items[2])
        menu_items3.click()

    with allure.step(f"Clicking on menu item: {expected_menu_items[3]}"):
        menu_items4 = driver.find_element(By.LINK_TEXT, expected_menu_items[3])
        menu_items4.click()

    with allure.step(f"Verifying the page heading for {expected_menu_items[3]}"):
        assert driver.find_element(By.TAG_NAME, 'h2').text == expected_menu_items[3]

    with allure.step(f"Clicking on menu item: {expected_menu_items[4]}"):
        menu_items5 = driver.find_element(By.LINK_TEXT, expected_menu_items[4])
        menu_items5.click()

    with allure.step(f"Verifying the page heading for {expected_menu_items[4]}"):
        assert driver.find_element(By.TAG_NAME, 'h2').text == expected_menu_items[4]

    with allure.step(f"Clicking on menu item: {expected_menu_items[5]}"):
        menu_items6 = driver.find_element(By.LINK_TEXT, expected_menu_items[5])
        menu_items6.click()

    with allure.step(f"Verifying the page heading for {expected_menu_items[5]}"):
        assert driver.find_element(By.TAG_NAME, 'h2').text == expected_menu_items[5]

    with allure.step(f"Clicking on menu item: {expected_menu_items[6]}"):
        menu_items7 = driver.find_element(By.LINK_TEXT, expected_menu_items[6])
        menu_items7.click()

    with allure.step(f"Verifying the page heading for {expected_menu_items[6]}"):
        assert driver.find_element(By.TAG_NAME, 'h2').text == expected_menu_items[6]

    with allure.step(f"Clicking on menu item: {expected_menu_items[7]}"):
        menu_items8 = driver.find_element(By.LINK_TEXT, expected_menu_items[7])
        menu_items8.click()

@pytest.mark.parametrize("menu_locator, submenu_locator, result_text",[
    (
            (By.PARTIAL_LINK_TEXT, 'Desktops'),
            (By.XPATH, '//*[@id="menu"]/div[2]/ul/li[1]/div/div/ul/li[1]/a'),
            'PC'
    ),
    (
            (By.PARTIAL_LINK_TEXT, 'Desktops'),
            (By.XPATH, '//*[@id="menu"]/div[2]/ul/li[1]/div/div/ul/li[2]/a'),
            'Mac'
    ),
    (
            (By.PARTIAL_LINK_TEXT, 'Laptops & Notebooks'),
            (By.XPATH, '//*[@id="menu"]/div[2]/ul/li[2]/div/div/ul/li[1]/a'),
            'Macs'
    ),
    (
            (By.PARTIAL_LINK_TEXT, 'Laptops & Notebooks'),
            (By.XPATH, '//*[@id="menu"]/div[2]/ul/li[2]/div/div/ul/li[2]/a'),
            'Windows'
    )
])

@allure.feature('Navigation Menu')
@allure.suite('Menu Interaction Tests')
@allure.title('Test nested menu functionality for {menu_locator} -> {submenu_locator}')
@allure.description('This test verifies that selecting submenus in the navigation menu displays the correct page content.')
@allure.severity(allure.severity_level.CRITICAL)
def test_nested_menu(driver, menu_locator, submenu_locator, result_text):

    with allure.step("Open the homepage"):
        driver.get("https://tutorialsninja.com/demo/")

    with allure.step(f"Hover over the menu {menu_locator}"):
        menu = driver.find_element(*menu_locator)

    with allure.step(f"Click on the submenu {submenu_locator}"):
        submenu = driver.find_element(*submenu_locator)
        ActionChains(driver).move_to_element(menu).click(submenu).perform()

    with allure.step(f"Check that the result text is '{result_text}'"):
        actual_text = driver.find_element(By.TAG_NAME, 'h2').text
        assert actual_text == result_text, f"Expected: {result_text}, but got: {actual_text}"

@allure.feature('Search Functionality')
@allure.suite('Product Search Tests')
@allure.title('Search for a product and verify the results')
@allure.description('This test searches for a product (MacBook) and verifies that the correct results are displayed.')
@allure.severity(allure.severity_level.CRITICAL)
def test_search_product(driver):

    with allure.step("Open the homepage"):
        driver.get("https://tutorialsninja.com/demo/")

    with allure.step("Locate the search bar and input the product name 'MacBook'"):
        search = driver.find_element(By.NAME, 'search')
        search.send_keys('MacBook')

    with allure.step("Click the search button"):
        button = driver.find_element(By.CSS_SELECTOR, '.btn.btn-default.btn-lg')
        button.click()

    with allure.step("Capture the list of product names displayed"):
        products = driver.find_elements(By.TAG_NAME, 'h4')

    with allure.step("Filter the products to check if all results contain 'MacBook'"):
        new_list = [elem.text for elem in products if 'MacBook' in elem.text]


    with allure.step("Verify that all listed products are relevant to 'MacBook'"):
        assert len(products) == len(new_list), f"Expected all products to be 'MacBook', but got: {new_list}"

@allure.feature('Shopping Cart')
@allure.suite('Cart Management Tests')
@allure.title('Add a product to the cart and verify cart contents')
@allure.description('This test adds a product to the cart and verifies that the cart contains the correct item and reflects the correct quantity.')
@allure.severity(allure.severity_level.CRITICAL)
def test_add_to_cart(driver):

    with allure.step("Open the homepage"):
        driver.get("https://tutorialsninja.com/demo/")

    with allure.step("Add the first product to the cart"):
        product = driver.find_element(By.XPATH, '//*[@id="content"]/div[2]/div[1]/div/div[3]/button[1]')
        product.click()

    with allure.step("Wait for and verify the success message appears"):
        success_message = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located( (By.CSS_SELECTOR, "div.alert.alert-success") )
        )
        assert "Success: You have added" in success_message.text, \
            "The success message was not displayed as expected."

    with allure.step("Verify the cart total updates to show 1 item"):
        WebDriverWait(driver, 10).until(
            EC.text_to_be_present_in_element((By.ID, "cart-total"), "1 item(s)")
        )

    with allure.step("Click the cart button to view its contents"):
        cart_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "cart"))
        )
        cart_button.click()

    with allure.step("Verify the cart contains the 'MacBook' product"):
        cart_contents = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "ul.dropdown-menu.pull-right"))
        )
        assert "MacBook" in cart_contents.text, f"Expected 'MacBook' in cart, but got: {cart_contents.text}"


@allure.feature('Homepage Features')
@allure.suite('Slider Functionality Tests')
@allure.title('Verify the homepage slider functionality')
@allure.description('This test checks that the slider is functional, moves between slides, and can revert back to the original slide.')
@allure.severity(allure.severity_level.NORMAL)
def test_slider_functionality(driver):

    with allure.step("Open the homepage"):
        driver.get("https://tutorialsninja.com/demo/")

    with allure.step("Verify that the slider is displayed"):
        slider = driver.find_element(By.CLASS_NAME, 'swiper-container')
        assert slider.is_displayed(), "Slider is not visible on the page."

    with allure.step("Capture the first slide's image source"):
        first_slide = driver.find_element(By.CSS_SELECTOR, ".swiper-slide-active img")
        first_slide_src = first_slide.get_attribute("src")

    with allure.step("Click on the next arrow to move to the next slide"):
        next_arrow = driver.find_element(By.CLASS_NAME, 'swiper-button-next')
        ActionChains(driver).move_to_element(slider).click(next_arrow).perform()

    with allure.step("Wait until the slider moves to the next slide"):
        WebDriverWait(driver, 10).until_not(
            EC.element_to_be_clickable(first_slide)
        )

    with allure.step("Capture the new slide's image source and verify it changed"):
        new_slide = driver.find_element(By.CSS_SELECTOR, ".swiper-slide-active img")
        new_slide_src = new_slide.get_attribute("src")
        assert first_slide_src != new_slide_src, "Slider did not move to the next image."

    with allure.step("Click on the previous arrow to move back to the first slide"):
        prev_arrow = driver.find_element(By.CLASS_NAME, 'swiper-button-prev')
        prev_arrow.click()

    with allure.step("Wait until the slider returns to the first slide"):
        WebDriverWait(driver, 10).until_not(
            EC.element_to_be_clickable(new_slide)
        )

    with allure.step("Verify that the slider has returned to the first image"):
        reverted_slide_src = driver.find_element(By.CSS_SELECTOR, ".swiper-slide-active img").get_attribute("src")
        assert reverted_slide_src == first_slide_src, "Slider did not return to the first image."

@allure.feature('Wishlist Functionality')
@allure.suite('Product Wishlist Tests')
@allure.title('Add a product to the wishlist and verify its presence')
@allure.description('This test adds a product (MacBook) to the wishlist and verifies that the product is successfully added and listed in the wishlist.')
@allure.severity(allure.severity_level.CRITICAL)
def test_add_to_wishlist(driver, login):

    with allure.step("Open the homepage"):
        driver.get("https://tutorialsninja.com/demo/")

    with allure.step("Locate and click on the 'Add to Wishlist' button for the first product"):
        wishlist_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="content"]/div[2]/div[1]/div/div[3]/button[2]'))
        )
    wishlist_button.click()

    with allure.step("Wait for and verify the success message is displayed"):
        success_message = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "div.alert.alert-success"))
        )
        assert "Success: You have added" in success_message.text, "Wishlist add failed"

    with allure.step("Click on the wishlist link to view the wishlist contents"):
        wishlist_link = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="wishlist-total"]'))
        )
        wishlist_link.click()

    with allure.step("Verify that the 'MacBook' product is in the wishlist"):
        wishlist_contents = WebDriverWait(driver, 15).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="content"]/div[1]/table/tbody/tr/td[2]/a'))
        )
        assert "MacBook" in wishlist_contents.text, "MacBook not found in wishlist"


@pytest.mark.parametrize("button, header, expected_text", [
    (
        (By.XPATH, '/html/body/footer/div/div/div[1]/ul/li[1]/a'),
        (By.XPATH, '//*[@id="content"]/h1'),
        "About Us"
    ),
    (
        (By.XPATH, '/html/body/footer/div/div/div[2]/ul/li[1]/a'),
        (By.XPATH, '//*[@id="content"]/h1'),
        "Contact Us"
    ),
    (
            (By.XPATH, '/html/body/footer/div/div/div[2]/ul/li[2]/a'),
            (By.XPATH, '//*[@id="content"]/h1'),
            "Product Returns"
    ),
    (
            (By.XPATH, "/html/body/footer/div/div/div[3]/ul/li[1]/a"),
            (By.XPATH, '//*[@id="content"]/h1'),
            "Find Your Favorite Brand"
    ),
    (
            (By.XPATH, '/html/body/footer/div/div/div[3]/ul/li[2]/a'),
            (By.XPATH, '//*[@id="content"]/h1'),
            "Purchase a Gift Certificate"
    )
])

@allure.feature('Footer Functionality')
@allure.suite('Footer Navigation Tests')
@allure.title('Verify footer section navigation and content')
@allure.description('This test verifies that clicking a footer button navigates to the correct section and displays the expected header text.')
@allure.severity(allure.severity_level.NORMAL)
def test_footer(driver, button, header, expected_text):

    with allure.step("Open the homepage"):
        driver.get("https://tutorialsninja.com/demo/")

    with allure.step(f"Click on the footer button: {button}"):
        footer_button = driver.find_element(*button)
        footer_button.click()

    with allure.step(f"Verify the footer header text is '{expected_text}'"):
        footer_header_text = driver.find_element(*header).text
        assert footer_header_text == expected_text, f"Expected '{expected_text}' but got '{footer_header_text}'"

