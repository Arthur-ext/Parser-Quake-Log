import os

import pytest

from tasks.task1 import read_game_kills, insert_value_per_game

class TestTask1:

    @pytest.fixture
    def task1_logfile(self):
        logfile = os.path.join(
            os.path.dirname(os.path.abspath(__file__)),
            'fixtures',
            'mock_game.log')
        return logfile
    

    def test_read_game_kills(self, task1_logfile):
        read_game_dict = dict(read_game_kills(task1_logfile))
        
        assert read_game_dict == {
            "game_1": {
                "total_kills": 131,
                "players": [
                    "Dono da Bola",
                    "Isgalamido",
                    "Zeh",
                    "Oootsimo",
                    "Mal",
                    "Assasinu Credi"
                ],
                "kills": {
                    "Dono da Bola": 14,
                    "Zeh": 19,
                    "Mal": 6,
                    "Isgalamido": 17,
                    "Assasinu Credi": 19,
                    "Oootsimo": 22
                },
                "kills_by_means": {
                    "MOD_ROCKET": 37,
                    "MOD_TRIGGER_HURT": 14,
                    "MOD_RAILGUN": 9,
                    "MOD_ROCKET_SPLASH": 60,
                    "MOD_MACHINEGUN": 4,
                    "MOD_SHOTGUN": 4,
                    "MOD_FALLING": 3
                }
            }
        }

    def test_insert_value_per_game(self):
        read_game = {
            'players': [],
            'kills_by_means': {},
            'total_kills': 0,
            'kills': {}
        }
        line = ("20:54 Kill: 1022 2 22: <world> killed Isgalamido by MOD_TRIGGER_HURT")
        insert_value_per_game(line, read_game)

        assert read_game == {
            'total_kills': 1,
            'players': ['Isgalamido'],
            'kills': {
                'Isgalamido': -1
            },
            'kills_by_means': {
                'MOD_TRIGGER_HURT': 1
            }
        }
