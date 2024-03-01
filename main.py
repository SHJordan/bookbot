def count_letters(text):
  """Counts the number of times each character appears in a string, ignoring case."""

  letter_counts = {}
  for char in text.lower():  # Convert to lowercase before iterating
    if char.isalpha():  # Only count letters
      if char in letter_counts:
        letter_counts[char] += 1
      else:
        letter_counts[char] = 1
  return letter_counts

def main():
    """Reads the contents of 'frankenstein.txt', counts letters, and prints results."""

    with open("books/frankenstein.txt") as f:
        book_contents = f.read()

    letter_counts = count_letters(book_contents)
    print("Character counts:")
    for char, count in letter_counts.items():
        print(f"{char}: {count}")

if __name__ == "__main__":
    main()
