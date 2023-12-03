import re
from part_numbers import engine_schematic

def get_number_matches(str):
    line_number_matches = []
    number_matches = re.finditer("\d+", str)

    for number_match in number_matches:
        single_number_match = int(number_match.group())
        number_match_start = number_match.start()
        number_match_end = number_match.end()

        line_number_matches.append([single_number_match, number_match_start, number_match_end])
    
    return line_number_matches


def get_gear_ratio(str, gear_index, numbers_arr):
    part_number_count = 0

    top_number_line_arr = numbers_arr[gear_index - 2] if gear_index > 1 else []
    middle_number_line_arr = numbers_arr[gear_index - 1]
    bottom_number_line_arr = numbers_arr[gear_index] if gear_index <= len(numbers_arr) - 1 else []

    gear_matches = re.finditer("\*", str)
    for gear_match in gear_matches:
        gear_index = gear_match.end()
        
        def check_top_number_arr():
            part_number = 1
            num_count = 0
            for number in top_number_line_arr:
                if (number[1] <= gear_index <= number[2] + 1):
                    part_number *= number[0]
                    num_count += 1
            
            part_number = part_number if num_count > 0 else 0
            return [part_number, num_count]
    
        def check_bottom_number_arr():
            part_number = 1
            num_count = 0
            for number in bottom_number_line_arr:
                if (number[1] <= gear_index <= number[2] + 1):
                    part_number *= number[0]
                    num_count += 1
            
            part_number = part_number if num_count > 0 else 0
            return [part_number, num_count]
        
        def check_middle_number_arr_left():
            part_number = 0
            for number in middle_number_line_arr:
                if (number[1] == gear_index):
                    part_number = number[0]
            return part_number
        
        def check_middle_number_arr_right():
            part_number = 0
            for number in middle_number_line_arr:
                if (number[2] + 1 == gear_index):
                    part_number = number[0]
            return part_number
        
        if (check_top_number_arr()[1] == 1 and check_bottom_number_arr()[1] == 1):
            part_number_count += check_top_number_arr()[0] * check_bottom_number_arr()[0]
        elif (check_top_number_arr()[1] == 1 and check_middle_number_arr_left() != 0):
            part_number_count += check_top_number_arr()[0] * check_middle_number_arr_left()
        elif (check_top_number_arr()[1] == 1 and check_middle_number_arr_right() != 0):
            part_number_count += check_top_number_arr()[0] * check_middle_number_arr_right()
        elif (check_bottom_number_arr()[1] == 1 and check_middle_number_arr_left() != 0):
            part_number_count += check_bottom_number_arr()[0] * check_middle_number_arr_left()
        elif (check_bottom_number_arr()[1] == 1 and check_middle_number_arr_right() != 0):
            part_number_count += check_bottom_number_arr()[0] * check_middle_number_arr_right()
        elif (check_middle_number_arr_left() != 0 and check_middle_number_arr_right() != 0):
            part_number_count += check_middle_number_arr_left() * check_middle_number_arr_right()
        elif (check_top_number_arr()[1] == 2):
            part_number_count += check_top_number_arr()[0]
        elif (check_bottom_number_arr()[1] == 2):
            part_number_count += check_bottom_number_arr()[0]
        
    return part_number_count

def get_sum_of_part_numbers(engine_schema):
    engine_schema_line = engine_schema.split("\n")
    sum_of_part_numbers = 0
    gear_line_number = 1
    all_number_matches = []

    for line in engine_schema_line:
        number_matches = get_number_matches(line)
        all_number_matches.append(number_matches)

    for line in engine_schema_line:
        part_numbers = get_gear_ratio(line, gear_line_number, all_number_matches)
        gear_line_number += 1
        sum_of_part_numbers += part_numbers

    return sum_of_part_numbers
        
print(f"The sum of all of the part numbers in the engine schematic {get_sum_of_part_numbers(engine_schematic)}")