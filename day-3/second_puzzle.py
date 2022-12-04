import string


def get_common_item(group_arr):
    return set(group_arr[0]) & set(group_arr[1]) & set(group_arr[2])


def get_item_priority(item):
    priority_list = list(string.ascii_lowercase) + list(string.ascii_uppercase)

    return priority_list.index(item) + 1


def get_priority_by_group(group_arr):
    common_item = get_common_item(group_arr).pop()

    return get_item_priority(common_item)


def main():
    archive_name = 'day-3/list.txt'
    archive_data = open(archive_name, 'r')
    group_arr = []
    sum = 0

    while line := archive_data.readline():
        group_arr.append(line.replace('\n', ''))

        if len(group_arr) == 3:
            sum += get_priority_by_group(group_arr)
            group_arr.clear()

    archive_data.close()

    print(sum)


main()
