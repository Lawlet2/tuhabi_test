from main import app
from fastapi.testclient import TestClient

client = TestClient(app)

url = "/properties"


def test_get_properties_success():
    """
    Test if get properties endpoint return success status code
    """
    response = client.get(url)
    assert response.status_code == 200


def test_get_properties_list():
    """
    Test if get properties endpoint return a list
    """
    response = client.get(url)
    assert response.status_code == 200
    assert type(response.json()) == list


def test_get_properties_year_param():
    """
    Test if get properties endpoint is successful
    setting the year param
    """
    year_param = {
        "year": 2000
    }
    response = client.get(url, params=year_param)
    assert response.status_code == 200
    assert type(response.json()) == list


def test_get_properties_city_param():
    """
    Test if get properties endpoint is successful
    setting the city param
    """
    city_param = {
        "city": "bogota"
    }
    response = client.get(url, params=city_param)
    assert response.status_code == 200


def test_get_properties_multiple_params():
    """
    Test if get properties endpoint is successful
    setting the multiple params
    """
    params = {
        "year": 2000,
        "city": "bogota"
    }
    response = client.get(url, params=params)
    assert response.status_code == 200


def test_get_properties_invalid_param():
    """
    Test if get properties endpoint is a bad
    request setting an invalid param
    """
    invalid_param = {
        "state": "mexico"
    }
    response = client.get(url, params=invalid_param)
    assert response.status_code == 400


def test_get_properties_error_detail():
    """
    Test if get properties endpoint
    return the detail error response
    """
    invalid_param = {
        "state": "mexico"
    }
    error_detail = {
        "detail": "The state field does not "
                  "exist in db thus this "
                  "parameter is not valid"
    }
    response = client.get(url, params=invalid_param)
    assert response.status_code == 400
    assert response.json() == error_detail
