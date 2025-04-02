def word_count(text):
    return len(text.split())

def char_count(text):
    text = text.lower()
    char_dict = {}

    for i in text:
        if i not in char_dict:
            char_dict[i] = 1      
        else:
            char_dict[i] += 1
    return char_dict

def sort_characters(char_dict):
    sorted_list = []
    for char, count in char_dict.items():
        if char.isalpha():
            sorted_list.append({
                "char": char,
                "count": count
            })
    sorted_list.sort(key=lambda x: x["count"], reverse=True)
    return sorted_list