from frame.main import Main


class TestMain:
    def test_main(self):
        main = Main().goto_market().goto_search()


def enhance(func):
    print('before')
    func()
    print('after')


def tmp(func):
    def wrapper(*args, **kwargs):
        print('before')
        func(*args, **kwargs)
        print('after')
    return wrapper


@tmp
def a(a1):
    print('a')
    print(a1)


# def a():
#     print('before')
#     print('a')
#     print('after')


def test_a():
    a(20)
