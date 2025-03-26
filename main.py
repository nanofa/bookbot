from stats import get_num_words, count_letters, split_dic, sort_on
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()


def main():
    #fp = "./books/frankenstein.txt"
    print(sys.argv)
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        fp = sys.argv[1]
        texto = get_book_text(fp)
    
        # Optional: count and print number of words
        # get_num_words(texto)

        # Count letters and convert to list of dicts
        count = count_letters(texto)
        final_list = split_dic(count)

        # Sort the list by count (descending)
        final_list.sort(reverse=True, key=sort_on)

        # Print report
        print(f"============ BOOKBOT ============")
        print(f"Analyzing book found at {fp}...")
        print(f"----------- Word Count ----------")
        get_num_words(texto)
        print(f"--------- Character Count -------")
        for item in final_list:
            if item['char'].isalpha():
                print(f"{item['char']}: {item['count']}")


main()