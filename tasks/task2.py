import json
from task1 import read_game_kills


def report(read_game):
    report_text = ""
    for game_num, game_values in read_game.items():
        players = ", ".join(game_values['players'])
        total_kills = game_values['total_kills']
        kills = game_values['kills']


        report_text += "\n\n%s %s %s\n\n" % ("-"*10, game_num, "-"*10)
        report_text += "Total de abates: \n- %s\n\n" % total_kills
        report_text += "Jogadores na partida: \n- %s\n\n" % players
        report_text += "Rank de eliminações dos Jogadores:\n"
        
        for player_name, kills in sorted(kills.items(), key=lambda kv:(kv[1], kv[0]), reverse=True):
            report_text += "- %s: %s\n" % (player_name, kills)
        
    
    return report_text

    

# read_game = read_game_kills("games.log")
# print(report(read_game))