from lib import goRestLib
import pytest
import yaml
from yaml import Loader
import argparse


def pytest_addoption(parser):
    parser.addoption("--token", action="store", default=None, required=False)

@pytest.fixture(scope="session")
#Environment file with scenario information
def env():
    with open("env.yml", "r") as f:
        test_data = yaml.load(f,Loader=Loader)
        yield test_data
    f.close()


@pytest.fixture(scope="session")
#Get token as passed via command line. Can be passed as a secret in CI/CD job so to not expose the token
def token(pytestconfig):
    yield pytestconfig.getoption("token")


@pytest.fixture(scope="session")
def restLib(token):
#Initialize go rest lib with or withtout token
    if token:
        lib = goRestLib(token=token)
    else: 
        lib=goRestLib(token=None)
    yield lib

@pytest.fixture(scope="function",autouse=True)
def tests_fixtures(request):
#Print fixtures used by each test
    fixtures = request.fixturenames
    print(fixtures)

@pytest.fixture(scope="function",autouse=True)
def tests_to_run(token,request):
#Skip tests that require authentication (marked with auth) when token is missing
    markers = request.node.get_closest_marker('auth')
    print(markers)
    if markers and not token:
        pytest.skip(reason="Cannot run tests that require authentication without token!")
    



if __name__ == "__main__":
    pass
   

    