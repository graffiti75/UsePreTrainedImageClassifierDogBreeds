def create_dict():
    # Creates empty dictionary named results_dic
    results_dic = dict()
    results_dic["a"] = ["A", 0, 3]
    results_dic["b"] = ["B", 1, 4]
    results_dic["c"] = ["C", 2, 5]
    
    return results_dic

def print_dict():
    results_dic = create_dict()
    for item in results_dic.items():
        print(item)

print_dict()