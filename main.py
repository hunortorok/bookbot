def main():
  book_path = "books/frankenstein.txt"
  text = get_book_text(book_path)
  word_count = get_book_word_count(text)
  char_count = get_char_count(text)
  print_report(book_path, word_count, char_count)

def get_book_text(path):
  with open(path) as f:
    return f.read()

def get_book_word_count(text):
  words = text.split()
  return len(words)

def get_char_count(text):
  lowercase_text = text.lower()
  char_dict = {}
  for char in lowercase_text:
    if char in char_dict:
      char_dict[char] += 1
    else:
      char_dict[char] = 1
  return char_dict

def sort_on(dict):
    return dict["count"]

def print_report(path, word_count, char_count):
  char_count_list = []
  for char in char_count:
    if char.isalpha():
      char_count_list.append({"char": char, "count": char_count[char]})
  char_count_list.sort(reverse=True, key=sort_on)
  print(f"--- Begin report of {path} ---")
  print(f"{word_count} words found in the document")
  print()
  for dict in char_count_list:
    print(f"The '{dict["char"]}' character was found {dict["count"]} times")
  print("--- End report ---")

main()
