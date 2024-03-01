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

def generate_report(book_contents):
  """Generates a report summarizing the book's word count and character occurrences."""

  word_count = len(book_contents.split())
  letter_counts = count_letters(book_contents)

  # Convert letter counts to a list of dictionaries for sorting
  sorted_letter_counts = [{"char": char, "count": count} for char, count in letter_counts.items()]
  sorted_letter_counts.sort(key=lambda entry: entry["count"], reverse=True)

  report = f"""--- Begin report of books/frankenstein.txt ---
{word_count} words found in the document
"""

  for entry in sorted_letter_counts[:20]:  # Show top 20 characters
    report += f"The '{entry['char']}' character was found {entry['count']} times\n"

  report += f"--- End report ---\n"

  return report

def main():
    """Reads the contents of 'frankenstein.txt' and generates a report."""

    with open("books/frankenstein.txt") as f:
        book_contents = f.read()

    report = generate_report(book_contents)
    print(report)

if __name__ == "__main__":
    main()
