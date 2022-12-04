# A - rock, B - paper, C - scissors
# X - lose, Y - draw, Z - win

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

def get_determined_result(result_letter):
    determined_result_dict = {
        'X': 'lose',
        'Y': 'draw',
        'Z': 'win',
    }

    return determined_result_dict.get(result_letter)


def get_choice_by_determined_result(choice, result):
    choice_by_determined_result_dict = {
        'A': {
            'lose': 'C',
            'draw': 'A',
            'win': 'B',
        },
        'B': {
            'lose': 'A',
            'draw': 'B',
            'win': 'C',
        },
        'C': {
            'lose': 'B',
            'draw': 'C',
            'win': 'A',
        },
    }

    return choice_by_determined_result_dict.get(choice).get(result)


def get_choice_points(players_choice):
    choice_points_dict = {
        'A': 1,
        'B': 2,
        'C': 3,
    }

    return choice_points_dict.get(players_choice)


def get_results_points(result_str):
    result_points_dict = {
        'lose': 0,
        'draw': 3,
        'win': 6,
    }

    return result_points_dict.get(result_str)


def get_play_score(play_line):
    determined_result = get_determined_result(play_line[2])
    result_points = get_results_points(determined_result)
    choice_points = get_choice_points(get_choice_by_determined_result(play_line[0], determined_result))


    return result_points + choice_points


def main():
    archive_name = 'day-two/list.txt'
    archive_data = open(archive_name, 'r')
    score = 0

    while line := archive_data.readline():
        score += get_play_score(line.replace('\n', ''))

    archive_data.close()

    print(score)


main()
