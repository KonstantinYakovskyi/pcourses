import pytest
import requests

STATUS_CODE_200 = 200
EXPECTED_TEXT = "['LICENSE.txt', 'NEWS.txt', 'python.exe', 'python3.dll', 'python36.dll', 'pythonw.exe', " \
                "'vcruntime140.dll']"


@pytest.fixture
def session_setup():
    print('session setup')
    yield requests.Session()


def set_url(url):
    def closure(func):
        func.url = url
        return func

    return closure


@pytest.fixture
def r(request):
    yield requests.get(request.function.url)


@set_url('http://localhost:8080/list?root=C:\Python36')
@pytest.mark.statuscodecheck
def test_check_status_code_is_200(r):
    assert r.status_code == STATUS_CODE_200
    print(r.text)
    print('test_check_status_code_is_200')


@set_url('http://localhost:8080/list?root=C:\Python36')
@pytest.mark.textcheck
def test_check_text(r):
    assert r.text == EXPECTED_TEXT
    print('test_check_text')
