# List to search in
numbers = [2,4,6,8,10]
search_num = 8

print(f"Searching for {search_num} in the list...")

for num in numbers:
    if num == search_num:
        print(f"Found {search_num}!")
        break
    print(f"Checking {num}...")