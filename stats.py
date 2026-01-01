def word_counter(book_text):
    words_list = book_text.split()
    return len(words_list)

def char_counter(words_list):
    char_dict = {}
    for word in words_list:
        word = word.lower()
        for char in word:
            if char in char_dict:
                char_dict[char] += 1
            else:
                char_dict[char] = 1
    return char_dict

def sort_on(item):
    return item['num']

def sorted_dict(chars_nums):
    char_list = []
    
    for k, v in chars_nums.items():
        new_dict = {
            "char": k,
            "num": v
        }
        
        char_list.append(new_dict)
    char_list.sort(reverse=True, key=sort_on)


    return char_list
