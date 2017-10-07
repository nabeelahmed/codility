
def odd_occurency(odd_list):
    """
    A non-empty zero-indexed array A consisting of N integers is given.
    The array contains an odd number of elements, and each element of the array can be paired with another element
    that has the same value, except for one element that is left unpaired.

    """
    if len(odd_list) % 2:
        sorted_list = sorted(odd_list)
        index = 0
        while index < (len(odd_list) - 1):
            if sorted_list[index] == sorted_list[index+1]:
                index += 2
            else:
                return sorted_list[index]
        # return sorted_list[-1]
        return sorted_list[index]
    else:
        return "List has to have an odd number of elements!"

if __name__ == "__main__":
    odd_num = [9, 3, 9, 3, 9, 6, 9, 4, 4, 5, 6, 5, 10, 11, 11, 11, 10, 10, 11, 7]  # size 20
    print odd_occurency(odd_num)  # List has to have an odd number of elements!
    odd_num = [10, 9, 3, 9, 3, 9, 6, 9, 4, 4, 5, 6, 5, 10, 11, 11, 11, 10, 10, 11, 7]  # size 21
    print odd_occurency(odd_num)  # 7
    odd_num = [10, 9, 3, 9, 3, 12, 9, 6, 9, 4, 4, 5, 6, 5, 10, 11, 11, 11, 10, 10, 11, 7, 7]  # size 23
    print odd_occurency(odd_num)  # 12 boundary case
