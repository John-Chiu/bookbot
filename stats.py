def get_num_of_words(text):
    strs = text.split()
    num_words = len(strs)
    return num_words

def num_of_chars(text):
    count = {}
    for ch in text:
        ch = ch.lower()
        if ch not in count:
            count[ch] = 0
        count[ch] += 1
    return count

def sort_dict(dict):
    list_of_dict = []

    for x in dict:
        val = dict[x]
        list_of_dict.append({"char": x, "num": val})

    list_of_dict.sort(reverse=True, key=sort_on)
    return list_of_dict
    
def sort_on(item):
    return item["num"]


def main():
    dict = {"a":2, "1": 10, ".": 3}
    sorted_dict = sort_dict(dict)