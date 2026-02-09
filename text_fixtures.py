import pytest

@pytest.fixture
def browser():
     pass

@pytest.fixture
def login_page(browser):
    pass

@pytest.fixture
def user():
    return "username","password"

@pytest.fixture
def test_login(login_page, user):
    username, password = user
    assert username == "username"
    assert password == "password"