from selene import browser, by, be


class OrderPage:

    def fill_first_name(self, value):
        browser.element("[placeholder='* Имя']").type(value)


    def fill_last_name(self, value):
        browser.element("[placeholder='* Фамилия']").type(value)

    def fill_address(self, value):
        browser.element("[placeholder='* Адрес: куда привезти заказ']").type(value)

    def fill_station(self, value):
        browser.element("[placeholder='* Станция метро']").click().type(value)
        browser.element(by.text(value)).click()

    def fill_phone_number(self, value):
        browser.element("[placeholder='* Телефон: на него позвонит курьер']").type(value)

    def click_next_btn(self):
        browser.element(by.text("Далее")).click()

    def fill_date_delivery(self, value):
        browser.element("[placeholder='* Когда привезти самокат']").click()
        browser.element(f"//div[contains(@class, 'react-datepicker__day--0{value}')]").click()

    def fill_rent_period(self, value):
        browser.element(by.text("* Срок аренды")).click()
        browser.element(by.text(value)).click()

    def fill_bike_colour(self, value):
        browser.element(f"#{value}").click()

    def fill_comment(self, value):
        browser.element("[placeholder='Комментарий для курьера']").type(value)

    def click_order_btn(self):
        browser.element("//button[contains(@class, 'Button_Button__ra12g') and contains(@class, "
                        "'Button_Middle__1CSJM') and text()='Заказать']").click()

    def click_confirm_btn(self):
        browser.element(by.text("Да")).click()

    def should_visible_status_btn(self):
        browser.element(by.text("Посмотреть статус")).should(be.visible)