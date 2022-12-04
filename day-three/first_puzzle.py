import string


def get_common_item(str1, str2):
    arr2_set = set(str2)
    for item in str1:
        if item in arr2_set:
            return item


def get_item_priority(item):
    priority_list = list(string.ascii_lowercase) + list(string.ascii_uppercase)

    return priority_list.index(item) + 1


def get_priority_by_line(line):
    common_item = get_common_item(
        line[0:int(len(line)/2)], line[int(len(line)/2):])

    return get_item_priority(common_item)


def main():
    archive_name = 'day-three/list.txt'
    archive_data = open(archive_name, 'r')

    sum = 0

    while line := archive_data.readline():
        sum += get_priority_by_line(line.replace('\n', ''))

    archive_data.close()

    print(sum)


main()
