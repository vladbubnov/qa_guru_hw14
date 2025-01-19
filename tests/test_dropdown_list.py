import os

import allure
import pytest

from pages.home_page import HomePage
from utils.data_utils import load_test_data_from_csv

csv_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../data/dropdown_data.csv"))
test_data = load_test_data_from_csv(csv_path)


@allure.tag('web')
@allure.feature("Заказ самоката")
@allure.story("Заказ самоката")
@allure.severity(allure.severity_level.CRITICAL)
@allure.label("owner", "Vladislav Bubnov")
@allure.description("Тест проверяет редирект на форму заказа самоката при нажатии кнопки 'Заказать' в футере")
@allure.link("https://qa-scooter.praktikum-services.ru/", name="Testing")
@pytest.mark.parametrize("dropdown_id, expected_dropdown_text, expected_dropdown_value_text", test_data)
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
