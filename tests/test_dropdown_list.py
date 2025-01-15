import allure
import pytest

from pages.home_page import HomePage


@allure.tag('web')
@allure.feature("Заказ самоката")
@allure.story("Заказ самоката")
@allure.severity(allure.severity_level.CRITICAL)
@allure.label("owner", "Vladislav Bubnov")
@allure.description("Тест проверяет редирект на форму заказа самоката при нажатии кнопки 'Заказать' в футере")
@allure.link("https://qa-scooter.praktikum-services.ru/", name="Testing")
@pytest.mark.parametrize("dropdown_id, expected_dropdown_text, expected_dropdown_value_text", [
    (0, "Сколько это стоит? И как оплатить?", "Сутки — 400 рублей. Оплата курьеру — наличными или картой."),
    (1, "Хочу сразу несколько самокатов! Так можно?", "Пока что у нас так: один заказ — один самокат. Если хотите "
                                                      "покататься с друзьями, можете просто сделать несколько заказов "
                                                      "— один за другим."),
    (2, "Как рассчитывается время аренды?", "Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в "
                                            "течение дня. Отсчёт времени аренды начинается с момента, "
                                            "когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, "
                                            "суточная аренда закончится 9 мая в 20:30."),
    (3, "Можно ли заказать самокат прямо на сегодня?", "Только начиная с завтрашнего дня. Но скоро станем расторопнее."),
    (4, "Можно ли продлить заказ или вернуть самокат раньше?", "Пока что нет! Но если что-то срочное — всегда можно "
                                                               "позвонить в поддержку по красивому номеру 1010."),
    (5, "Вы привозите зарядку вместе с самокатом?", "Самокат приезжает к вам с полной зарядкой. Этого хватает на "
                                                    "восемь суток — даже если будете кататься без передышек и во сне. "
                                                    "Зарядка не понадобится."),
    (6, "Можно ли отменить заказ?", "Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не "
                                    "попросим. Все же свои."),
    (7, "Я жизу за МКАДом, привезёте?", "Да, обязательно. Всем самокатов! И Москве, и Московской области."),
])
def test_dropdown_list(browser_management, dropdown_id, expected_dropdown_text, expected_dropdown_value_text):
    browser = browser_management
    home_page = HomePage()

    with allure.step("Открываем домашнюю страницу"):
        browser.open("/")

    with allure.step("Переход к блоку о важном"):
        home_page.turn_questions_about_important()

    with allure.step("Нажимаем на стрелку дропдауна"):
        home_page.click_dropdown_list(dropdown_id)

    with allure.step("Проверяем текст дропдауна"):
        home_page.should_text_dropdown_list_with(dropdown_id, expected_dropdown_text, expected_dropdown_value_text)