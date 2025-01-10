from selene import browser


class HomePage:

    def click_order_header_btn(self):
        browser.element("//div[contains(@class, 'Header_Nav__AGCXC')]/button[contains(@class, "
                        "'Button_Button__ra12g')]").click()

    def click_order_footer_btn(self):
        browser.element("//div[contains(@class, 'Home_FinishButton__1_cWm')]/button").click()

    def click_accept_cookie(self):
        browser.element("#rcc-confirm-button").click()