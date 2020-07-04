import requests
from datetime import datetime
from datetime import date


# based on
# https://helmstedt.dk/2019/09/hiv-dine-transaktioner-ud-af-det-nye-nordnet/
class NordNet():
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.accounts = {
            "Frie midler: Nordnet": "1",

        }
        # Start date (start of period for transactions) and date today used for extraction of transactions
        startdate = '2013-01-01'
        today = date.today()
        enddate = datetime.strftime(today, '%Y-%m-%d')

        print(self.username)
        print(self.password)

    def login(self):
        # LOGIN TO NORDNET #

        # First part of cookie setting prior to login
        # url = 'https://classic.nordnet.dk/mux/login/start.html?cmpi=start-loggain&state=signin'
        url = "https://classic.nordnet.dk/mux/login/start.html"
        request = requests.get(url)
        # print(request.cookies)
        # print(request.cookies['LOL'])
        cookies = dict()
        cookies['LOL'] = request.cookies['LOL']
        cookies['TUX-COOKIE'] = request.cookies['TUX-COOKIE']

        # Second part of cookie setting prior to login
        url = 'https://classic.nordnet.dk/api/2/login/anonymous'
        request = requests.post(url)
        cookies['NOW'] = request.cookies['NOW']

        # Actual login that gets us cookies required for later use
        url = 'https://classic.nordnet.dk/api/2/authentication/basic/login'
        request = requests.post(url, cookies=cookies, data={'username': self.username, 'password': self.password})
        cookies['NOW'] = request.cookies['NOW']
        cookies['xsrf'] = request.cookies['xsrf']

        # Getting a NEXT cookie
        url = 'https://classic.nordnet.dk/oauth2/authorize?client_id=NEXT&response_type=code&redirect_uri=https://www' \
              '.nordnet.dk/oauth2/ '
        request = requests.get(url, cookies=cookies)
        cookies['NEXT'] = request.history[1].cookies['NEXT']


if __name__ == '__main__':
    nordnet = NordNet("", "")
    nordnet.login()
    # print("hello world")
