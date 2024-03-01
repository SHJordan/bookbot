def count_words(text):
    """Counts the number of words in a string."""

    words = text.split()
    return len(words)

def main():
    """Reads the contents of 'frankenstein.txt', counts the words, and prints the result."""

    with open("books/frankenstein.txt") as f:
        book_contents = f.read()

    word_count = count_words(book_contents)
    print("Number of words in the book:", word_count)

if __name__ == "__main__":
    main()
