import argparse

if __name__ == "__main__":
    arguments = argparse.ArgumentParser(description="Parse Quake Log File")
    
    arguments.add_argument("-l", "--logfile",
                            required=True,
                            dest='logfile',
                            metavar='log file',
                            help="log file path")
    
    args = arguments.parse_args()
    print(args.logfile)
    