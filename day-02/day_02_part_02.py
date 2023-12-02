import re
from games import all_games

def get_game_power(game_str):
    cubes_list = game_str.split(";")
    min_red_cubes, min_green_cubes, min_blue_cubes = 0, 0, 0

    for cubes in cubes_list:
        red_cubes_list = (re.findall("(\d{1,2}) red", cubes))
        current_red_cubes = int(red_cubes_list[0]) if (len(red_cubes_list) > 0) else 0 

        green_cubes_list = (re.findall("(\d{1,2}) green", cubes))
        current_green_cubes = int(green_cubes_list[0]) if (len(green_cubes_list) > 0) else 0

        blue_cubes_list = (re.findall("(\d{1,2}) blue", cubes))
        current_blue_cubes = int(blue_cubes_list[0]) if (len(blue_cubes_list) > 0) else 0

        min_red_cubes = current_red_cubes if (current_red_cubes > min_red_cubes) else min_red_cubes

        min_green_cubes = current_green_cubes if (current_green_cubes > min_green_cubes) else min_green_cubes

        min_blue_cubes = current_blue_cubes if (current_blue_cubes > min_blue_cubes) else min_blue_cubes
        
        cubes_power = min_red_cubes * min_green_cubes * min_blue_cubes

    return cubes_power

def get_games_list(games):
    games_list = games.split("\n")
    total_game_power = 0

    for game in games_list:
        game_power = get_game_power(game)
        total_game_power += game_power

    return total_game_power

print(f"The sum of the power of the games is {get_games_list(all_games)}")

