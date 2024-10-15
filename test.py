def split_list_in_threes(lst):
    # Use a list comprehension to create chunks of size 3
    return [lst[i:i + 3] for i in range(0, len(lst), 3)]

# Example usage
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
chunks = split_list_in_threes(my_list)
print(chunks)