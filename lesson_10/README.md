# Проект по автоматизации тестирования с Allure (Skypro)

Этот проект содержит автотесты для учебных стендов: магазина SauceDemo и медленного калькулятора. В проекте реализована
отчетность Allure, разметка шагов и аннотация типов.

## Структура проекта в папке lesson_10

- `pages.py` — описание страниц (Page Object) для магазина SauceDemo.
- `test_saucedemo.py` — тесты функционала магазина.
- `calculator_page.py` — описание страницы калькулятора.
- `test_calculator.py` — тесты калькулятора с задержкой.

## Используемые технологии

- Python 3.x
- Selenium WebDriver
- Pytest
- Allure Framework (allure-pytest)

## Как запустить тесты для формирования отчета

1. Убедитесь, что у вас установлены зависимости:
   ```bash
   pip install selenium pytest allure-pytest

2. Запустите тесты из папки lesson_10, указав директорию для сохранения результатов Allure:
      ```bash
   pytest --alluredir=allure-results

Как просмотреть сформированный отчет
Для генерации и открытия отчета в браузере используйте команду:

```bash
allure serve allure-results


