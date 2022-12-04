# A - rock, B - paper, C - scissors
# X - rock, Y - paper, Z - scissors

# Points by choice:
# 3 - scissors
# 2 - paper
# 1 - rock

# Points by result:
# 6 - win
# 3 - draw
# 0 - loss

# The score of each game is the sum of the choice points and the result points
# Total score according to the given input

def get_choice_points(players_choice):
    choices_dict = {
        'X': 1,
        'Y': 2,
        'Z': 3,
    }

    return choices_dict.get(players_choice)


def get_result_points(play_line):
    result_dict = {
        'AX': 3,
        'AY': 6,
        'AZ': 0,
        'BX': 0,
        'BY': 3,
        'BZ': 6,
        'CX': 6,
        'CY': 0,
        'CZ': 3,
    }

    return result_dict.get(play_line.replace(' ','')) + get_choice_points(play_line[2])

def main():
    archive_name = 'day-two/list.txt'
    archive_data = open(archive_name, 'r')
    score = 0

    while line := archive_data.readline():
        score += get_result_points(line.replace('\n', ''))
    
    archive_data.close()

    print(score)


main()
