import database.conn as connect
import json

def save_games(read_games):
    
    try:
        base = connect.conn_to_database()
        collection = base.games_parsed

        for key, values in read_games.items():
            if not game_exists(key):
                game_insert = {
                    "id_game": key,
                    "game" : values
                }
                collection.insert_one(game_insert)
    finally:
        base.client.close()

def game_exists(game_id):
    try:
        base = connect.conn_to_database()
        collection = base.games_parsed
        result = collection.find_one({"id_game": game_id})
        return result
        # if result:
        #     return True
        # return False
    finally:
        base.client.close()


def jsonfy(obj):
    jsonfy_obj = json.dumps(obj, indent=4)
    return jsonfy_obj
