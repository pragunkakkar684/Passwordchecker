import requests
import hashlib
import sys
import argparse

def request_api_data(query): #gets all the hash passwords starting with same query
    url = f"https://api.pwnedpasswords.com/range/{query}"
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(f"Error fetching: {res.status_code}, check the api and try again")
    return res

def read_res(response): #can be used to read the response
    print(response.text)

def get_password_leaks_count(hashes,hash_to_check):
    hashes = (line.split(":") for line in hashes.text.splitlines()) #splits the response on :
    for h, count in hashes:
        if h == hash_to_check: #check if the tail of given hashed password matches
            return count #returns the count
    return 0

def pwned_api_check(password): #to check if the password exists in API response, hashes the password and calls for the response with first 5 digits and returns the count
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first5_char, tail = sha1password[:5], sha1password[5:]
    res = request_api_data(first5_char)
    return get_password_leaks_count(res,tail)

def main():
    parser  = argparse.ArgumentParser(description="Check your password against a database of over 1.1 million have-i-been-pwned passwords")
    parser.add_argument('--password',type=str,help = "Comma-seperated list of passwords to check",required=False)
    parser.add_argument('--file',type=str,help = "File containing passwords to check",required=False)

    args = parser.parse_args()

    if args.password:
        for password in args.password.split(','):
            count = pwned_api_check(password)
            if count:
                print(f"{password} was found {count} times... you should probably change your password!")
            else:
                print(f"{password} was NOT found. Carry on!")
    elif args.file:
        try:
            with open(args.file,'r') as file:
                passwords = [line.strip() for line in file.readlines()]
                for password in passwords:
                    count = pwned_api_check(password)
                    if count:
                        print(f"{password} was found {count} times... you should probably change your password!")
                    else:
                        print(f"{password} was NOT found. Carry on!")
        except FileNotFoundError:
            print("File not found")
    else:
        print("Error: You must provide either a list of passwords or a file containing passwords.")
        sys.exit(1)


if __name__ == "__main__":
    main()