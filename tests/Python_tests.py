from datetime import time
from shlex import join

from selene import browser


def test_dark_theme():
    """
    Протестируйте правильность переключения темной темы на сайте
    """
    # Test_1 - dark time
    current_time = time(hour=23)
    # TODO переключите темную тему в зависимости от времени суток (с 22 до 6 часов утра - ночь)
    is_dark_theme = None
    if current_time >= time(22):
        is_dark_theme = True
    elif current_time <= time(6):
        is_dark_theme = True
    else:
        is_dark_theme = False
    assert is_dark_theme is True

    # Test_2 - daytime dark theme
    current_time = time(hour=16)
    dark_theme_enabled = True
    # TODO переключите темную тему в зависимости от времени суток,
    #  но учтите что темная тема может быть включена вручную
    is_dark_theme = None
    if current_time >= time(22):
        is_dark_theme = True
    elif current_time <= time(6):
        is_dark_theme = True
    elif dark_theme_enabled:
        is_dark_theme = True
    else:
        is_dark_theme = False
    assert is_dark_theme is True


def test_find_suitable_user():
    """
    Найдите нужного пользователя по условиям в списке пользователей
    """
    users = [
        {"name": "Oleg", "age": 32},
        {"name": "Sergey", "age": 24},
        {"name": "Stanislav", "age": 15},
        {"name": "Olga", "age": 45},
        {"name": "Maria", "age": 18},
    ]
    # TODO найдите пользователя с именем "Olga"
    # Test_1: Find exact name (single position search)
    suiable_user = None
    first_name_1 = "Olga"
    for user in users:
        if user['name'] == first_name_1:
            suiable_user = user
            print(f"🎊 Look! We have found {user['name']} here!🎊")
            break
        else:
            print(f"Oops, {user['name']} doesn't match 😢")

    assert suiable_user == {"name": "Olga", "age": 45}

    # TODO найдите всех пользователей младше 20 лет
    # Test_2: Find a list by age
    suiable_users = None
    suiable_users = []
    for by_age in users:
        if by_age['age'] <= 20:
            suiable_users.append(by_age)
            print(f"😎 {by_age['name']} is under 20")

    assert suiable_users == [
        {"name": "Stanislav", "age": 15},
        {"name": "Maria", "age": 18},
    ]


# Сделайте функцию, которая будет печатать
# читаемое имя переданной ей функции и значений аргументов.
# Вызовите ее внутри функций, описанных ниже
# Подсказка: Имя функции можно получить с помощью func.__name__
# Например, вызов следующей функции должен преобразовать имя функции
# в более читаемый вариант (заменить символ подчеркивания на пробел,
# сделать буквы заглавными (или первую букву), затем вывести значения всех аргументов этой функции:
# >>> open_browser(browser_name="Chrome")
# "Open Browser [Chrome]"

def convert_to_readable_name(function_name, *args):
    return f'{function_name.__name__.replace("_", " ").title()} [{", ".join(args)}]'


def test_readable_function():
    open_browser(browser_name="Chrome")
    go_to_companyname_homepage(page_url="https://companyname.com")
    find_registration_button_on_login_page(page_url="https://companyname.com/login", button_text="Register")


def open_browser(browser_name):
    browser.config.browser_name = "Chrome"
    actual_result = convert_to_readable_name(open_browser, browser_name)
    print(actual_result)
    assert actual_result == "Open Browser [Chrome]"


def go_to_companyname_homepage(page_url):
    actual_result = convert_to_readable_name(go_to_companyname_homepage, page_url)
    print(actual_result)
    assert actual_result == "Go To Companyname Homepage [https://companyname.com]"


def find_registration_button_on_login_page(page_url, button_text):
    actual_result = convert_to_readable_name(find_registration_button_on_login_page, page_url, button_text)
    print(actual_result)
    assert actual_result == "Find Registration Button On Login Page [https://companyname.com/login, Register]"
