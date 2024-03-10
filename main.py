def sort_on(dict):
    return dict["count"]

book_to_sort = "books/frankenstein.txt"

with open(book_to_sort) as f:
    file_contents = f.read()

counts = {}
counts_list = []
for letter in file_contents:
    if str(letter).isalpha():
        if counts.get(letter.lower()) != None:
            counts[letter.lower()] = counts[letter.lower()] + 1
        else:
            counts[letter.lower()] = 1

for letter_record in counts:
    counts_list.append({"letter": letter_record, "count": counts[letter_record]})

counts_list.sort(reverse=True, key=sort_on)
print(f"--- Begin report of {book_to_sort} ---")
print(f"{len(file_contents.split())} words found in the document\n\n")
for item in counts_list:
    print(f"The '{item["letter"]}' character was found {item["count"]} times")
print("--- End report ---")