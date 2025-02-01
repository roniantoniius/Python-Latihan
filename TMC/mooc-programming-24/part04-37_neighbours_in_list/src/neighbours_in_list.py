# Write your solution here
def longest_series_of_neighbours(lis : list) -> int:
    max_juml = 0
    count = 1
    for i in range(1, len(lis)):
        if abs(lis[i] - lis[i - 1]) == 1:
            count+=1
        else:
            max_juml = max(max_juml, count)
            count = 1
    max_juml = max(max_juml, count)
    return max_juml
if __name__ == "__main__":
    my_list = [1, 2, 5, 7, 6, 5, 6, 3, 4, 1, 0]
    print(longest_series_of_neighbours(my_list))