#!/usr/bin/env python
import os
from typing import Any, Dict
import requests

base_url = 'http://stats.nba.com/stats'  # type: str

HEADERS = {
    'user-agent': ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) '
                   'AppleWebKit/537.36 (KHTML, like Gecko) '
                   'Chrome/45.0.2454.101 Safari/537.36'),
}  # type: Dict[str, str]

DATA_FOLDER = '../TEMP/nba/synch'  # type: str


def main() -> None:
    if not os.path.exists(DATA_FOLDER):
        os.makedirs(DATA_FOLDER, exist_ok=True)
    player_args = []  # type: list
    get_players(player_args)
    for args in player_args:
        get_player(*args)


def get_players(player_args):
    endpoint = '/commonallplayers'  # type str
    # type: Dict[str, str]
    params = {'leagueid': '00', 'season': '2016-17', 'isonlycurrentseason': '1'}
    url = '{}{}'.format(base_url, endpoint)  # type: str
    print('Getting all players...')
    resp = requests.get(url, headers=HEADERS, params=params)
    data = resp.json()  # type: Any
    player_args.extend(
        [(item[0], item[2]) for item in data['resultSets'][0]['rowSet']])


def get_player(player_id, player_name):
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
