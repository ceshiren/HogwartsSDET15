import allure


def handle_black(func):
    def wrapper(*args, **kwargs):
        from frame.base_page import BasePage
        instance: BasePage = args[0]
        try:
            result = func(*args, **kwargs)
            instance.error_num = 0
            return result
        # 捕获黑名单中的元素
        except Exception as e:
            instance.driver.save_screenshot("tmp.png")
            with open("tmp.png", "rb") as f:
                content = f.read()
            allure.attach(content, attachment_type=allure.attachment_type.PNG)
            # 超过最大查找次数
            if instance.error_num > instance.max_num:
                raise e
            instance.error_num += 1
            # 从黑名单中遍历元素，依次进行处理
            for black_ele in instance.black_list:
                ele = instance.driver.find_elements(*black_ele)
                if len(ele) > 0:
                    ele[0].click()
                    # 处理完黑名单后，再次查找原来的元素
                    return wrapper(*args, **kwargs)
            raise e

    return wrapper
