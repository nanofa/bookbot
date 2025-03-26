def get_num_words(text):
    num_words = len(text.split())
    print(f"Found {num_words} total words")
    
def count_letters(text):
    lower_text = text.lower()
    d = {}
    for i in range(0,len(text)):
        if lower_text[i] in d:
            d[lower_text[i]] += 1
        else:
            d[lower_text[i]] = 1   
    return d
    
def split_dic(dict):
    new_list = []
    for key, value in dict.items():
        d_aux = {}
        d_aux["char"] = key
        d_aux["count"] = value
        new_list.append(d_aux)
    return new_list
    

def sort_on(dict):
    return dict["count"]

