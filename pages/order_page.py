from selene import browser, by, have, be


class OrderPage:

    def open(self, browser_management):
        browser_management.open("/order")

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
        browser.element("//button[contains(@class, 'Button_Button') and contains(@class, "
                        "'Button_Middle') and text()='Заказать']").click()

    def click_confirm_btn(self):
        browser.element(by.text("Да")).click()

    def click_status_btn(self):
        browser.element(by.text("Посмотреть статус")).click()

    def fill_user_information(self, first_name, last_name, address, station, phone_number):
        self.fill_first_name(first_name)
        self.fill_last_name(last_name)
        self.fill_address(address)
        self.fill_station(station)
        self.fill_phone_number(phone_number)

    def fill_order_detail(self, date_delivery, rent_period, bike_colour):
        self.fill_date_delivery(date_delivery)
        self.fill_rent_period(rent_period)
        self.fill_bike_colour(bike_colour)
        self.fill_comment("Тестовый комментарий")

    def create_order(self, first_name, last_name, address, station, phone_number, date_delivery, rent_period,
                     bike_colour):
        self.fill_user_information(first_name, last_name, address, station, phone_number)
        self.click_next_btn()
        self.fill_order_detail(date_delivery, rent_period, bike_colour)
        self.click_order_btn()
        self.click_confirm_btn()
        self.click_status_btn()

    def should_user_with(self, first_name, last_name, address, station, phone_number, delivery_date,
                         period_rent, bike_colour):
        (browser.element("//div[contains(@class, 'Track_OrderInfo')]")
        .all("//div[contains(@class, 'Track_Value')]")
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

    def get_order_number(self):
        return (browser.element("//input[contains(@class, 'Input_Input') and contains(@class, 'Track_Input')]")
                .get_attribute('placeholder'))

    def click_order_status(self):
        browser.element("[placeholder='Введите номер заказа']").click()

    def fill_order_number(self, value):
        browser.element("[placeholder='Введите номер заказа']").type(value)

    def click_go_btn(self):
        browser.element("//button[contains(@class, 'Button_Button') and contains(@class, 'Header_Button')]").click()

    def search_order(self, order_number):
        self.click_order_status()
        self.fill_order_number(order_number)
        self.click_go_btn()

    def should_visible_status_order(self):
        browser.element("//div[contains(@class, 'Track_OrderRoadmap')]").should(be.visible)
