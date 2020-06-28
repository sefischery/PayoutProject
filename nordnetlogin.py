import requests
from datetime import datetime
from datetime import date

#based on
#https://helmstedt.dk/2019/09/hiv-dine-transaktioner-ud-af-det-nye-nordnet/
class NordNet():
    def __init__(self, username,password):
        self.username = username
        self.password = password
        self.accounts = {
            "Frie midler: Nordnet": "1",

        }

    def login(self):
        # Start date (start of period for transactions) and date today used for extraction of transactions
        startdate = '2013-01-01'
        today = date.today()
        enddate = datetime.strftime(today, '%Y-%m-%d')

        print(self.username)
        print(self.password)
        manualdataexists = True
        manualdata = """
        Id;Bogføringsdag;Handelsdag;Valørdag;Transaktionstype;Værdipapirer;Instrumenttyp;ISIN;Antal;Kurs;Rente;Afgifter;Beløb;Valuta;Indkøbsværdi;Resultat;Totalt antal;Saldo;Vekslingskurs;Transaktionstekst;Makuleringsdato;Verifikations-/Notanummer;Depot
        ;30-09-2013;30-09-2013;30-09-2013;KØBT;Obligationer 3,5%;Obligationer;;72000;;;;-69.891,54;DKK;;;;;;;;;;Frie midler: Finansbanken
        """
        cookies = {}

        # A variable to store transactions before saving to csv
        transactions = ""

        # LOGIN TO NORDNET #

        # First part of cookie setting prior to login
        url = 'https://classic.nordnet.dk/mux/login/start.html?cmpi=start-loggain&state=signin'
        request = requests.get(url)
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
        url = 'https://classic.nordnet.dk/oauth2/authorize?client_id=NEXT&response_type=code&redirect_uri=https://www.nordnet.dk/oauth2/'
        request = requests.get(url, cookies=cookies)
        cookies['NEXT'] = request.history[1].cookies['NEXT']

        # GET TRANSACTION DATA #

        # Payload and url for transaction requests
        payload = {'locale': 'da-DK','from': startdate,'to': enddate}

        url = "https://www.nordnet.dk/mediaapi/transaction/csv/filtered"

        firstaccount = True
        for portfolioname, id in self.accounts.items():
            payload['account_id'] = id
            data = requests.get(url, params=payload, cookies=cookies)
            result = data.content.decode('utf-16')
            result = result.replace('\t', ';')

            result = result.splitlines()

if __name__ == '__main__':
    nordnet = NordNet("X","X!")
    nordnet.login()
    #print("hello world")