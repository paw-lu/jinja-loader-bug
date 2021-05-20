from jinja_loader_bug import __main__


def test_dummy() -> None:
    assert True


def test_it() -> None:
    output = __main__.test_me()
    assert output == "hi"
