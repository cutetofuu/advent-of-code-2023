import re
from part_numbers import engine_schematic

def get_symbol_matches(str):
    line_symbol_matches = []
    symbol_matches = re.finditer("[^.a-z0-9]", str)

    for symbol_match in symbol_matches:
        symbol_match_end = symbol_match.end()
        line_symbol_matches.append(symbol_match_end)

    return line_symbol_matches


def get_part_number(str, number_index, symbols_arr):
    part_number_count = 0

    top_symbol_line_arr = symbols_arr[number_index - 2] if number_index > 1 else []
    middle_symbol_line_arr = symbols_arr[number_index - 1]
    bottom_symbol_line_arr = symbols_arr[number_index] if number_index <= len(symbols_arr) - 1 else []

    number_matches = re.finditer("\d+", str)
    for number_match in number_matches:
        single_number_match = int(number_match.group())
        number_match_start = number_match.start()
        number_match_end = number_match.end()

        for symbol_index in top_symbol_line_arr:
            if (number_match_start <= symbol_index <= number_match_end + 1):
                part_number_count += single_number_match
                break

        for symbol_index in bottom_symbol_line_arr:
            if (number_match_start <= symbol_index <= number_match_end + 1):
                part_number_count += single_number_match
                break

        for symbol_index in middle_symbol_line_arr:
            if (number_match_start == symbol_index or number_match_end + 1 == symbol_index):
                part_number_count += single_number_match
                break
        
    return part_number_count

def get_sum_of_part_numbers(engine_schema):
    engine_schema_line = engine_schema.split("\n")
    sum_of_part_numbers = 0
    number_line_number = 1
    all_symbol_matches = []

    for line in engine_schema_line:
        symbol_matches = get_symbol_matches(line)
        all_symbol_matches.append(symbol_matches)

    for line in engine_schema_line:
        part_numbers = get_part_number(line, number_line_number, all_symbol_matches)
        number_line_number += 1
        sum_of_part_numbers += part_numbers

    return sum_of_part_numbers

print(f"The sum of all of the part numbers in the engine schematic {get_sum_of_part_numbers(engine_schematic)}")