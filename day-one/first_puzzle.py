# Calories - find the Elf carrying the most Calories. List containing how much calories each food item a elf is carrying contains. The elves "inventories"
# are separated by a blank line.
# open the list as a archive and go with "readline" until it breaks, then return the highest sum of calories


def main():
    txt_name = 'day-one/calories_list.txt'
    txt_data = open(txt_name, 'r')
    calories_sum_aux = 0
    biggest_calories_amount = 0

    for line in txt_data:
        clean_line = line.replace('\n', '')

        if clean_line == '':
            calories_sum_aux = 0

        else:
            calories_sum_aux += int(clean_line)

            if calories_sum_aux > biggest_calories_amount:
                biggest_calories_amount = calories_sum_aux
    
    txt_data.close()

    print(biggest_calories_amount)


main()
