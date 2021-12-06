import requests
api_url = "https://api.github.com/users"


def validate_get_user_since():
    api_url = "https://api.github.com/users"
    params_dict = {'since': '95592000'}
    response = requests.get(api_url, params=params_dict)
    print (response.json())
    assert response.status_code == 200
    print response.headers
    assert response.headers["Content-Type"] == "application/json; charset=utf-8"

def validate_patch_user_location():
    api_url = "https://api.github.com/user"
    params_dict = {'location': 'earth'}
    response = requests.patch(api_url, params=params_dict)
    print response.headers
    print (response.json())
    #assert response.status_code == 200

validate_get_user_since()
validate_patch_user_location()
