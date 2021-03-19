from collections import deque


def max_value_each_subarray(numbers, size):
    # deque to store indices of number for each subarray in descending order by value
    index_deque = deque()

    for i in range(len(numbers)):
        # remove old indices in deque that is outside the current window (subarray)
        while index_deque and index_deque[0] <= i-size:
            index_deque.popleft()

        # make sure deque is stored descendingly
        while index_deque and numbers[i] >= numbers[index_deque[-1]]:
            index_deque.pop()
        index_deque.append(i)

        if i >= size - 1:
            print(numbers[index_deque[0]], end=" ")


numbers = [10, 5, 2, 7, 8, 7]
size = 3
max_value_each_subarray(numbers, 3)
