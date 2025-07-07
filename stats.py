def sort_on(item):
    return item["num"]

def get_num_words(path):
    with open(path) as f:
        print(f"Found {len(f.read().split())} total words") 

def numb_of_character(path):
    with open(path) as f:
        dict_all = f.read().lower()
    dict_final = {}
    for char in dict_all:
        if char in dict_final:
            dict_final[char] += 1
        else:
            dict_final[char] = 1
    list = []
    for item in dict_final:
        list.append({"name": item, "num": dict_final[item]})
    list.sort(reverse=True, key=sort_on)
    for i in range(1, len(list)-1):
        print(f"{list[i]["name"]}: {list[i]["num"]}")