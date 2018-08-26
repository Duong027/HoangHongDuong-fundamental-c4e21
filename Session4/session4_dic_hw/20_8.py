nhap = input("Nhap text vao day ").lower()

# Counting letter
letter_counts = {}
for letter in nhap:
    letter_counts[letter] = letter_counts.get(letter, 0) + 1

# Sorting in abc order and not print(' ')   

letter_items = list(letter_counts.items())   
letter_items.sort()
print(letter_items[1:])
    