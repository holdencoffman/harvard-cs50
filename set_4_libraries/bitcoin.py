# CoinCap API Key: 253af39f58f3cee3e1b60b7762203f79ca89cc69abff59488d4773e868a14fa3

import sys
import requests as rq

def get_coins():
    num_coins = sys.argv[1]
    try:
        num_coins = float(num_coins)
    except ValueError:
        sys.exit('The command line argument for number of bitcoins desired could not be converted to a float.')
    return num_coins

def retrieve_price(api_key):
    payload = {'api_key': api_key}
    bitcoin_url = 'https://rest.coincap.io/v3/assets/bitcoin'
    try:
        response = rq.get(bitcoin_url, params=payload).json()
    except Exception:
        sys.exit('The api call failed.')
    return float(response.get('data').get('priceUsd'))
    # TODO: Having an issue with the handling of the json object that was parsed and assigned to the response variable


def main():
    num_coins = get_coins()
    api_key = '253af39f58f3cee3e1b60b7762203f79ca89cc69abff59488d4773e868a14fa3'
    current_price = retrieve_price(api_key)
    total_price = num_coins * current_price
    print(f'${total_price:,.4f}')

if __name__ == '__main__':
    main()