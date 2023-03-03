#This is Sort the arrays with bubble method in python:-
def sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

arr = [2, 3, 5, 7, 8, 4]
result = sort(arr)
for i in range(len(arr)):
    print(arr[i])

'''
Advantages:-
Bubble sort  is easy to understand and implement.
It is not require any additional memory space.
It is adatablility to different of data.

Disadvantage:-
Bubble sort has time complaexity of O(n^2) which makes it very slow.
It is not efficient for large data set
It is not stable sort algorithm, becouse element in same key value may not maintain
'''