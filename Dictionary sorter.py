# Dictionary Sorter

def sort_dict_by_key(d, ascending=True):
    return dict(sorted(d.items(), key=lambda item: item[0], reverse=not ascending))

def sort_dict_by_value(d, ascending=True):
    return dict(sorted(d.items(), key=lambda item: item[1], reverse=not ascending))

# Sample dictionary
sample_dict = {
    "apple": 5,
    "banana": 2,
    "cherry": 7,
    "date": 3
}

# Get sorting preferences from user
print("Choose sorting method:")
print("1. Sort by key")
print("2. Sort by value")
choice = input("Enter choice (1/2): ")

print("Choose order:")
print("1. Ascending")
print("2. Descending")
order_choice = input("Enter order (1/2): ")
ascending = True if order_choice == '1' else False

# Sort and display the dictionary
if choice == '1':
    sorted_dict = sort_dict_by_key(sample_dict, ascending=ascending)
elif choice == '2':
    sorted_dict = sort_dict_by_value(sample_dict, ascending=ascending)
else:
    print("Invalid choice! Please select 1 or 2.")
    sorted_dict = None

if sorted_dict is not None:
    print("Sorted dictionary:", sorted_dict)
