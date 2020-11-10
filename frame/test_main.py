from frame.main import Main


class TestMain:
    def test_main(self):
        Main().goto_market().goto_search().search()