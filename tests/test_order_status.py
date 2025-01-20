import allure

from data import users
from pages.order_page import OrderPage


@allure.tag('web')
@allure.feature("Статус заказа")
@allure.story("Статус заказа")
@allure.severity(allure.severity_level.CRITICAL)
@allure.label("owner", "Vladislav Bubnov")
@allure.description("Проверка статуса заказа")
@allure.link("https://qa-scooter.praktikum-services.ru/", name="Testing")
def test_order_status(remote_run):
    order_page = OrderPage()
    user = users.user

    with allure.step("Открываем страницу заказа"):
        order_page.open(remote_run)

    with allure.step("Получаем номер заказа"):
        order_page.create_order(user.first_name, user.last_name, user.address, user.station, user.phone_number,
                                user.date_delivery, user.rent_period, user.bike_colour)
        order_number = order_page.get_order_number()

    with allure.step("Поиск по номеру заказа"):
        order_page.search_order(order_number)

    with allure.step("Проверяем данные заказа"):
        order_page.should_user_with(user.first_name, user.last_name, user.address, user.station, user.phone_number,
                                    user.date_delivery, user.rent_period, user.bike_colour)

    with allure.step("Проверяем отображения статуса заказа"):
        order_page.should_visible_status_order()
