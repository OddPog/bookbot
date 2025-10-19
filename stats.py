def count_words(book_text):
    word_count = len(book_text.split())
    return word_count

def count_chars(book_text):
    char_count = {}
    for char in book_text:
        lchar = char.lower()
        if lchar in char_count:
            char_count[lchar] += 1
        else:
            char_count[lchar] = 1
    return char_count

def sort_on(key):
    return key["count"]


def dicto_sortlist(char_dic):
    sorted_list = []
    for char in char_dic:
        sorted_list.append({"char": char, "count": char_dic[char]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list