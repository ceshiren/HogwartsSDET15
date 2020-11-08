from selenium.webdriver.common.by import By

from frame.base_page import BasePage


class Proxy:
    def __init__(self, target):
        self.target = target

    def __getattribute__(self, item):
        _black_list = [(By.XPATH, "//*[@resource-id='com.xueqiu.android:id/iv_close']")]
        target = object.__getattribute__(self, "target")
        format_attr = object.__getattribute__(target, item)
        if item in ['find']:
            def wrapper(*args, **kwargs):
                _max_num = 3
                _error_num = 0
                try:
                    result = format_attr(*args, **kwargs)
                    _error_num = 0
                    return result
                except Exception as e:
                    if _error_num > _max_num:
                        raise e
                    _error_num += 1
                    for ele in _black_list:
                        elements = target.driver.find_elements(*ele)
                        if len(elements) > 0:
                            elements[0].click()
                            return format_attr(*args, **kwargs)

                    raise e


            return wrapper
        else:
            return format_attr


def tmp_base_page():
    return Proxy(BasePage())