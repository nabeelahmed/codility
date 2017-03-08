"""
Results:

$ python 2.longest_zeroseq.py
12
(24, 12) {'count': 12, 'index': 24}
"""


def zero_count(A):
    count = 0
    result = 0
    for index, elem in enumerate(A):
        if elem == 0:
            count += 1
        else:
            # if current is high then the repvious update
            if count > result:
                result = count
            count = 0
    print result

def zero_count_i(A):
    count = 0
    result = (0,0)  # for keeping the index and count i.e. (index, count)
    result_dict = {}
    for index, elem in enumerate(A):
        if elem == 0:
            count += 1
        else:
            if count > result[1]:
                result = ((index - count), count)
                result_dict = {'index': (index - count), 'count': count}
            count = 0
    print result, result_dict

if __name__ == "__main__":
    A = [1, 1,1,1,1,0,0,0,0,0,0,0,1,1,1,1,0,0,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,0,0,1,1,1,1,0,0,0,0,1,0,1,1]
    zero_count(A)
    zero_count_i(A)
