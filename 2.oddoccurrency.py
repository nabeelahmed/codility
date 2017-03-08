def odd_occurence(A):
    if not len(A) % 2:
        sorted_A = sorted(A)
        print sorted_A
        index = 0
        while index < len(sorted_A):
            print 'index ---', index
            if sorted_A[index] == sorted_A[index+1]:
                print sorted_A[index]
                print sorted_A[index+1]
                index += 2
            else:
                return sorted_A[index]
    else:
        return "List has to have an odd number of elements!"

if __name__ == "__main__":
    A = [9,3,9,3,9,6,9, 4, 4, 5, 6, 5, 10, 11, 11, 11, 10, 10, 11, 7]
    answer = odd_occurence(A)
    print "The odd occurenece -->", answer
