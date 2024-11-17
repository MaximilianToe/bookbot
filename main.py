def count_line(line):
    return len(line.split())

def count_text(text):
    lines = text.split("\n")
    total =0
    for line in lines:
        total += count_line(line)
    return total

def count_characters(text):
    text = text.lower()
    d = {}
    for c in text:
        if c not in d.keys():
            d[c] = 1
        else:
            d[c] +=1
    return d

def print_report(text_name):
    with open("books/"+text_name) as f:
        file_contents = f.read()
        num_words = count_text(file_contents)
        d = count_characters(file_contents)
        print(f"--- Begin report of books/{text_name} ---", text_name)
        print(f"{num_words} found in the document\n")
        for key, value in d.items():
            print(f"The '{key}' character was found {value} times")
        print("--- End report ---")


def main():
    text_name = "frankenstein.txt"
    print_report(text_name)

if __name__ =="__main__":
    main()
