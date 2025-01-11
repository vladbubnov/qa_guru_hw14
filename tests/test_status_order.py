import allure


@allure.tag('web')
@allure.feature("Заказ самоката")
@allure.story("Заказ самоката")
@allure.severity(allure.severity_level.CRITICAL)
@allure.label("owner", "Vladislav Bubnov")
@allure.description("Тест заказ самоката")
@allure.link("https://qa-scooter.praktikum-services.ru/", name="Testing")
def test_status_order(browser_management):
    pass
