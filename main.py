def main():
    file_contents = ""
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    return file_contents

print(main())
