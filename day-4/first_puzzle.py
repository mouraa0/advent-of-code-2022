def do_contain(arr1, arr2):
    if int(arr1[0]) >= int(arr2[0]) and int(arr1[1]) <= int(arr2[1]):
        return True

    if int(arr2[0]) >= int(arr1[0]) and int(arr2[1]) <= int(arr1[1]):
        return True

    return False


def range_contains_other(line):
    str1, str2 = line.split(',')

    if (do_contain(str1.split('-'), str2.split('-'))):
        return 1

    return 0


def main():
    archive_name = 'day-4/list.txt'
    archive_data = open(archive_name, 'r')
    sum = 0

    while line := archive_data.readline():
        sum += range_contains_other(line.replace('\n', ''))

    archive_data.close()

    print(sum)


main()
