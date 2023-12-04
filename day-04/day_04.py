from scratchcards import scratchcards, small_scratchcard

def get_card_points(str):
    card_number_sets = str.split(" | ")
    winning_numbers = (card_number_sets[0])[10:].split(" ")
    players_numbers = card_number_sets[1].split()
    num_of_matches = 0

    for number in players_numbers:
        if number in winning_numbers:
            num_of_matches += 1

    points = (2 ** (num_of_matches - 1)) if num_of_matches > 0 else 0
    return points 

def get_sum_of_points(cards):
    cards_list = cards.split("\n")
    sum_of_points = 0

    for card in cards_list:
        single_card_points = get_card_points(card)
        sum_of_points += single_card_points
    
    return sum_of_points

print(f"The sum of all of the part numbers in the engine schematic {get_sum_of_points(scratchcards)}")