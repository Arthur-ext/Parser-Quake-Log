import argparse
from tasks.task1 import read_game_kills
from tasks.task2 import report
import json

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
    
    args = arguments.parse_args()
    games = read_game_kills(args.logfile)
    if args.report:
        print(report(games))
    else:
        games_json = json.dumps(games, indent=4)
        print(games_json)
    