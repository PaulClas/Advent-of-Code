def store_two_list(list1: list, list2: list):
    with open("input.txt", "r") as file:
        for line in file:
            col1, col2 = line.split()
            list1.append(int(col1))
            list2.append(int(col2))


def sort_sum():
    list1 = []
    list2 = []

    store_two_list(list1, list2)

    list1.sort()
    list2.sort()

    list3 = [abs(x - y) for x, y in zip(list1, list2)]

    sum_list_3 = sum(list3)

    print(sum_list_3)


def similarity():
    list1 = []
    list2 = []

    store_two_list(list1, list2)

    total_similarity_score = 0
    for num in list1:
        count_in_list2 = list2.count(num)
        total_similarity_score += num * count_in_list2

    print(total_similarity_score)


if __name__ == "__main__":
    sort_sum()
    similarity()
