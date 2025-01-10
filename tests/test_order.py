import allure

from data import users
from pages.order_page import OrderPage


@allure.tag('web')
@allure.feature("Заказ самоката")
@allure.story("Заказ самоката")
@allure.severity(allure.severity_level.CRITICAL)
@allure.label("owner", "Vladislav Bubnov")
@allure.description("Тест заказ самоката")
@allure.link("https://qa-scooter.praktikum-services.ru/", name="Testing")
def test_order_in_header_button(browser_management):
    browser = browser_management
    order_page = OrderPage()
    user = users.user

    with allure.step("Открываем страницу заказа"):
        browser.open("/order")

    with allure.step("Вводим имя"):
        order_page.fill_first_name(user.first_name)

    with allure.step("Вводим фамилию"):
        order_page.fill_last_name(user.last_name)

    with allure.step("Вводим адрес"):
        order_page.fill_address(user.address)

    with allure.step("Выбираем станцию метро"):
        order_page.fill_station(user.station)

    with allure.step("Вводим номер телефона"):
        order_page.fill_phone_number(user.phone_number)

    with allure.step("Нажимаем кнопку 'Далее'"):
        order_page.click_next_btn()

    with allure.step("Выбираем дату доставки"):
        order_page.fill_date_delivery(user.date_delivery)

    with allure.step("Выбираем срок аренды"):
        order_page.fill_rent_period(user.rent_period)

    with allure.step("Выбираем цвет самоката"):
        order_page.fill_bike_colour(user.bike_colour)

    with allure.step("Вводим комментарий для курьера"):
        order_page.fill_comment("Тестовый комментарий")

    with allure.step("Нажимаем кнопку 'Заказать'"):
        order_page.click_order_btn()

    with allure.step("Нажимаем кнопку 'Да' в модальном окне 'Хотите оформить заказ?'"):
        order_page.click_order_btn()