import requests
import json
from time import sleep

def get_starters_from_boxscore_api_fixed(game_id):
    url = f"https://site.api.espn.com/apis/site/v2/sports/basketball/wnba/summary?event={game_id}"
    resp = requests.get(url)
    data = resp.json()

    game_data = {
        "game_id": game_id,
        "teams": []
    }

    try:
        for team in data['boxscore']['players']:
            team_name = team['team']['displayName']
            starters = []

            stats_labels = team['statistics'][0]['labels']
            athletes = team['statistics'][0]['athletes']

            for player in athletes:
                if player.get('starter') and player.get('stats'):
                    stat_dict = dict(zip(stats_labels, player['stats']))
                    starters.append({
                        "name": player['athlete']['displayName'],
                        **stat_dict
                    })

            game_data['teams'].append({
                "team": team_name,
                "starters": starters
            })

    except Exception as e:
        print(f"Error parsing game {game_id}: {e}")

    return game_data