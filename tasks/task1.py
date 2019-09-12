import re
import collections
# import json

game_regex = re.compile(r".*InitGame.*")

kill_regex = re.compile(r".*Kill:.*:(.*).*killed(.*)by(.*)")

def read_game_kills(file):
    game_count = 1
    read_game = collections.OrderedDict()
    
    with open(file, 'r', encoding='utf-8') as fl:
        for line in fl.readlines():
            if game_regex.match(line): 
                game = "game_%s" % game_count
                
                read_game[game] = {
                    'total_kills': 0,
                    'players': [],
                    'kills': {},
                    'kills_by_means': {}
                }

                game_count += 1

            if kill_regex.match(line):
                insert_value_per_game(line, read_game[game])
                
    # print(json.dumps(read_game, indent=4))
    return read_game

def insert_value_per_game(line, read_game):
    kill = kill_regex.match(line)
    killer = kill.group(1).strip()
    victim = kill.group(2).strip()
    weapon = kill.group(3).strip()
    
    read_game['total_kills'] += 1

    ''' Set Player in list '''
    if killer not in read_game['players'] and killer != "<world>":
        read_game['players'].append(killer)
    
    ''' Set Player in list '''
    if victim not in read_game['players']:
        read_game['players'].append(victim)
    
    ''' Add User Kills '''
    if killer != "<world>":
        if killer not in read_game['kills'].keys():
            read_game['kills'][killer] = 1
        else:
            read_game['kills'][killer] += 1
    
    ''' Deduct user Kills if he dies to the world '''
    if killer == "<world>":
        if victim not in read_game['kills'].keys():
            read_game['kills'][victim] = -1
        else:
            read_game['kills'][victim] -= 1
    
    if weapon not in read_game['kills_by_means']:
        read_game['kills_by_means'][weapon] = 1
    else:
        read_game['kills_by_means'][weapon] += 1
