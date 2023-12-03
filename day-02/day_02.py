import re
from games import all_games

cubes_lookup = {"red": 12, "green": 13, "blue": 14}

def get_game_id_value(game_str):
    cubes_list = game_str.split(";")

    for cubes in cubes_list:
        red_cubes_list = (re.findall("(\d{1,2}) red", cubes))
        red_cubes = int(red_cubes_list[0]) if (len(red_cubes_list) > 0) else 0 

        green_cubes_list = (re.findall("(\d{1,2}) green", cubes))
        green_cubes = int(green_cubes_list[0]) if (len(green_cubes_list) > 0) else 0

        blue_cubes_list = (re.findall("(\d{1,2}) blue", cubes))
        blue_cubes = int(blue_cubes_list[0]) if (len(blue_cubes_list) > 0) else 0
       
        if (red_cubes > cubes_lookup["red"]
            or green_cubes > cubes_lookup["green"]
            or blue_cubes > cubes_lookup["blue"]):
            game_id = 0
            return game_id
        
        game_id = int(re.findall("Game (\d{1,3})", cubes_list[0])[0])

    return game_id

def get_sum_of_game_ids(games):
    games_list = games.split("\n")
    total_id_value = 0

    for game in games_list:
        game_id_value = get_game_id_value(game)
        total_id_value += game_id_value

    return total_id_value

print(f"The sum of the ID of the games is {get_sum_of_game_ids(all_games)}")

