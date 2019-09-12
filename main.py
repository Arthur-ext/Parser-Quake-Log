import argparse
import json
from tasks.task1 import read_game_kills
from tasks.task2 import report
from tasks.save_games import save_games, game_exists


if __name__ == "__main__":
    arguments = argparse.ArgumentParser(description="Parse Quake Log File")
    
    arguments.add_argument("-l", "--logfile",
                            required=True,
                            dest='logfile',
                            metavar='log file',
                            action='store',
                            help="log file path")
    
    arguments.add_argument('-r', '--report',
                            dest='report',
                            action='store_true',
                            help='show game report')
    arguments.add_argument('-s', '--save',
                            dest='save',
                            action='store_true',
                            help='save games in MongoDb')
    
    args = arguments.parse_args()
    games = read_game_kills(args.logfile)
    if args.report:
        print(report(games))
    else:
        games_json = json.dumps(games, indent=4)
        print(games_json)

    if args.save:
        save_games(games)
        
    