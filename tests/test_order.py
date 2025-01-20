import allure

from data import users
from pages.home_page import HomePage
from pages.order_page import OrderPage


@allure.tag('web')
@allure.feature("Заказ самоката")
@allure.story("Заказ самоката")
@allure.severity(allure.severity_level.CRITICAL)
@allure.label("owner", "Vladislav Bubnov")
@allure.description("Проверка заполнения полей")
@allure.link("https://qa-scooter.praktikum-services.ru/", name="Testing")
def test_order(remote_run):
    order_page = OrderPage()
    user = users.user

    with allure.step("Открываем страницу заказа"):
        order_page.open(remote_run)

    with allure.step("Создаем заказ"):
        order_page.create_order(user.first_name, user.last_name, user.address, user.station, user.phone_number,
                                user.date_delivery, user.rent_period, user.bike_colour)

    with allure.step("Проверяем данные заказа'"):
        order_page.should_user_with(user.first_name, user.last_name, user.address, user.station, user.phone_number,
                                    user.date_delivery, user.rent_period, user.bike_colour)


@allure.tag('web')
@allure.feature("Заказ самоката")
@allure.story("Заказ самоката")
@allure.severity(allure.severity_level.CRITICAL)
@allure.label("owner", "Vladislav Bubnov")
@allure.description("Тест проверяет редирект на форму заказа самоката при нажатии кнопки 'Заказать' в хедере")
@allure.link("https://qa-scooter.praktikum-services.ru/", name="Testing")
def test_order_btn_on_header(remote_run):
    home_page = HomePage()

    with allure.step("Открываем домашнюю страницу"):
        home_page.open(remote_run)

    with allure.step("Нажимаем на кнопку 'Заказать' в хедере"):
        home_page.click_order_header_btn()
        home_page.should_redirect_to_order()


@allure.tag('web')
@allure.feature("Заказ самоката")
@allure.story("Заказ самоката")
@allure.severity(allure.severity_level.CRITICAL)
@allure.label("owner", "Vladislav Bubnov")
@allure.description("Тест проверяет редирект на форму заказа самоката при нажатии кнопки 'Заказать' в футере")
@allure.link("https://qa-scooter.praktikum-services.ru/", name="Testing")
def test_order_btn_on_footer(remote_run):
    home_page = HomePage()

    with allure.step("Открываем домашнюю страницу"):
        home_page.open(remote_run)

    with allure.step("Закрываем сообщение и использовании кук"):
        home_page.click_accept_cookie()

    with allure.step("Нажимаем на кнопку 'Заказать' в футере"):
        home_page.click_order_footer_btn()
        home_page.should_redirect_to_order()
