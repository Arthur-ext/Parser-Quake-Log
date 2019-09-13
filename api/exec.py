from flask import Flask, jsonify, request
from flask_pymongo import PyMongo, MongoClient
import conn

app = Flask(__name__)

base = conn.conn_to_database()

@app.route('/', methods=['GET'])
def home():
    res = "access /games - to consult all games<br/>access /games/[game_num] to consult this game"
    return res

@app.route('/games', methods=['GET'])
def get_all_games():
    games = base.games_parsed

    output = []

    for g in games.find():
        output.append({
            'game_id': g['id_game'],
            'game_value': g['game']
        })
    if len(output):
        return jsonify({'result':output})
    else:
        return jsonify({'result': "No games found"})
    

@app.route('/games/<game_id>', methods=['GET'])
def get_game(game_id):
    games = base.games_parsed
    game_id_concat = 'game_%s' % game_id
    # return game_id_concat
    output = []
    
    find_game = games.find_one({"id_game": game_id_concat})
    
    if find_game:
        output = { 'game_value': find_game['game'] }
    else:
        output = "Game not found"

    return jsonify({'result':output})
    

if __name__ == "__main__":
    app.run(debug=True)
    # print(app)