#!/usr/bin/env python
import os
from multiprocessing.dummy import Pool

import requests

base_url = 'http://stats.nba.com/stats'

HEADERS = {
    'user-agent': ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) '
                   'AppleWebKit/537.36 (KHTML, like Gecko) '
                   'Chrome/45.0.2454.101 Safari/537.36'),
}

DATA_FOLDER = '../TEMP/nba/threads' # type: str


def main():
    if not os.path.exists(DATA_FOLDER):
        os.makedirs(DATA_FOLDER, exist_ok=True)
    player_args = []
    get_players(player_args)
    pool = Pool(25)
    pool.map(get_player, player_args)


def get_players(player_args):
    endpoint = '/commonallplayers'
    params = {'leagueid': '00', 'season': '2016-17', 'isonlycurrentseason': '1'}
    url = '{}{}'.format(base_url, endpoint)
    print('Getting all players...')
    resp = requests.get(url, headers=HEADERS, params=params)
    data = resp.json()
    player_args.extend(
        [(item[0], item[2]) for item in data['resultSets'][0]['rowSet']])


def get_player(args):
    player_id, player_name = args
    endpoint = '/commonplayerinfo'
    params = {'playerid': player_id}
    url = base_url + endpoint
    print('Getting player', player_name)
    resp = requests.get(url, headers=HEADERS, params=params)
    print(resp)
    data = resp.text
    file_name = player_name.replace(" ", "_") + '.json'
    file_path = os.path.join(DATA_FOLDER, file_name)
    with open(file_path, 'w') as file:
        file.write(data)


if __name__ == '__main__':
    main()
