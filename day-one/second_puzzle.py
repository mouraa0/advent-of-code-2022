# Now, the sum of the top 3 calories holders

def verify_is_top(top_list, sum):
    for i in range(len(top_list)):
        if i == len(top_list) - 1:
            if sum > top_list[i]:
                aux = top_list[i - 1]
                top_list[i - 1] = top_list[i]
                top_list[i - 2] = aux
                top_list[i] = sum

            
            return

        if sum < top_list[i]:
            return
        
        if sum < top_list[i + 1]:
            if i != 0:
                top_list[i - 1] = top_list[i]
            top_list[i] = sum

            return


def print_top_list_sum(top_list):
    sum = 0

    for num in top_list:
        sum += num
    
    print(sum)


def main():
    txt_name = 'day-one/calories_list.txt'
    txt_data = open(txt_name, 'r')
    top_calories_sum = [0, 0, 0]
    calories_sum_aux = 0

    for line in txt_data:
        clean_line = line.replace('\n', '')

        if clean_line == '':
            verify_is_top(top_calories_sum, calories_sum_aux)
            calories_sum_aux = 0

        else:
            calories_sum_aux += int(clean_line)
    
    txt_data.close()
    verify_is_top(top_calories_sum, calories_sum_aux)

    print(top_calories_sum)
    print_top_list_sum(top_calories_sum)


main()