def main():
    """Reads the contents of 'frankenstein.txt' and prints it to the console."""

    with open("books/frankenstein.txt") as f:
        book_contents = f.read()

    print(book_contents)

if __name__ == "__main__":
    main()
