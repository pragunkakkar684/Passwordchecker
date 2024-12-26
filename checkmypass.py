import requests
import hashlib

def request_api_data(query):
    url = f"https://api.pwnedpasswords.com/range/{query}"
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(f"Error fetching: {res.status_code}, check the api and try again")
    return res

def pwned_api_check(password): #to check if the password exists in API response
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    return sha1password

