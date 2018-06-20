from app.application import Application
from app.call_center import CallCenter
from app.customer import Customer
import pytest
import json
import os.path


fixture = None
target = None


@pytest.fixture
def app(request):
    global fixture
    global target
    browser = request.config.getoption("--browser")
    if target is None:
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), request.config.getoption("--target"))
        with open(config_file) as f:
            target = json.load(f)
    if fixture is None or not fixture.is_valid():
        fixture = Application(browser=browser)
    fixture.session.ensure_login(login=target['login'], password=target['password'])
    return fixture


@pytest.fixture
def call_center(request):
    global fixture
    global target
    browser = request.config.getoption("--browser")
    if target is None:
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), request.config.getoption("--target"))
        with open(config_file) as f:
            target = json.load(f)
    if fixture is None or not fixture.is_valid():
        fixture = CallCenter(browser=browser)
    fixture.session.ensure_login(login=target['login_call_center'], password=target['password_call_center'])
    fixture.session.login_to_test_company()
    return fixture


@pytest.fixture(scope="module")
def customer(request):
    global fixture
    browser = request.config.getoption("--browser")
    fixture = Customer(browser=browser)
    yield fixture
    fixture.destroy()


@pytest.fixture(scope="module", autouse=True)
def stop(request):
    def fin():
        fixture.session.ensure_logout()
        fixture.destroy()
    request.addfinalizer(fin)
    return fixture


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")
    parser.addoption("--target", action="store", default="target.json")