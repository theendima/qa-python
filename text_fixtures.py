import pytest

@pytest.fixture
def login_page(browser, browser_context_args):
    print("страница логин")


@pytest.fixture
def user():
    print("Юзверь")
    return "username", "password"


def test_login(login_page, user):
    username, password = user
    assert username == "username"
    assert password == "password"

