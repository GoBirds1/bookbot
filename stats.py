def words_in_string(string):
    return len(string.split())

def characters_in_string(string):
    d = {}
    for chr in string:
        lc = chr.lower()
        if lc not in d.keys():
            d[lc] = 1
        else:
            d[lc] += 1
    return d

def sort_on(dict):
    return dict["num"]

def sort_dict(dct):
    lst = []
    for key in dct:
        t_dct = {"char": key, "num": dct[key]}
        lst.append(t_dct)
    lst.sort(reverse=True, key=sort_on)
    return lst