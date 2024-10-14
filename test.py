def split_into_pairs(lst):
    # Create pairs using list comprehension
    pairs = [(lst[i], lst[i + 1]) for i in range(0, len(lst) - 1, 2)]
    
    # Check if the list has an odd number of elements
    if len(lst) % 2 != 0:
        # Add the last element as a single pair
        pairs.append((lst[-1],))
    
    return pairs

# Example usage
my_list = [1, 2, 3, 4, 5]
pairs = split_into_pairs(my_list)
i=1
for pair in pairs:
        print(f"{i}. {pair[0]} - {pair[1]}")
        i += 1