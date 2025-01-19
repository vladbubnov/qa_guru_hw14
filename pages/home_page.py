from selene import browser, have, command, be


class HomePage:

    def open(self, browser_management):
        browser_management.open("/")

    def click_order_header_btn(self):
        browser.element("//div[contains(@class, 'Header_Nav')]/button[contains(@class, "
                        "'Button_Button__ra12g')]").click()

    def click_order_footer_btn(self):
        browser.element("//div[contains(@class, 'Home_FinishButton')]/button").click()

    def click_accept_cookie(self):
        browser.element("#rcc-confirm-button").click()

    def click_accept_cookie(self):
        browser.element("#rcc-confirm-button").click()

    def turn_questions_about_important(self):
        element = browser.element("//div[contains(@class, 'Home_FAQ')]")

        # Выполняем прокрутку к элементу
        element.perform(command.js.scroll_into_view)

    def click_dropdown_list(self, dropdown_id):
        browser.element(f"#accordion__heading-{dropdown_id}").click()

    def should_text_dropdown_list_with(self, dropdown_id, expected_dropdown_text, expected_dropdown_value_text):
        browser.element(f"#accordion__heading-{dropdown_id}").should(have.text(expected_dropdown_text))
        browser.element(f"#accordion__panel-{dropdown_id}").should(have.text(expected_dropdown_value_text))

    def should_redirect_to_order(self):
        browser.should(have.url_containing('/order'))
        browser.element("//div[contains(@class, 'Order_Form')]").should(be.visible)
