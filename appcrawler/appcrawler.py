class Appium:
    def page_source(self):
        return ""

    def find(self):
        pass

    def action(self):
        pass

    def start(self):
        pass


class Crawler():
    def find_selected_list(self):
        pass

    def sort(self):
        pass


if __name__ == '__main__':
    appium = Appium()
    crawler = Crawler()

    appium.start()


    def recurs():
        source = appium.page_source ()
        sub = crawler.find_selected_list(source)
        elements = crawler.sort()
        for element in elements:
            element.click()
            recurs()
