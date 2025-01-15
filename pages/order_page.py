from selene import browser, by, be, have


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

    def click_status_btn(self):
        browser.element(by.text("Посмотреть статус")).click()


    def should_user_with(self, first_name, last_name, address, station, phone_number, delivery_date,
                         period_rent, bike_colour):
        (browser.element("//div[contains(@class, 'Track_OrderInfo__2fpDL')]")
            .all("//div[contains(@class, 'Track_Value__15eEX')]")
            .even.should(have.exact_texts(
                first_name,
                last_name,
                address,
                station,
                phone_number,
                delivery_date,
                period_rent,
                bike_colour
            )
        ))
