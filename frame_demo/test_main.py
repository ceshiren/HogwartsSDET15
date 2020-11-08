from frame.main import Main


class Test_main:
    def test_main(self):
        main = Main().goto_search()
        main.search()
