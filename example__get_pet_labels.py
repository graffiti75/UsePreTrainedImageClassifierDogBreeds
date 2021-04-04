# Imports only listdir function from OS module 
from os import listdir

def get_pet_label(pet_image):
    # Sets string to lower case letters
    low_pet_image = pet_image.lower()

    # Splits lower case string by _ to break into words 
    word_list_pet_image = low_pet_image.split("_")

    # Create pet_name starting as empty string
    pet_name = ""

    # Loops to check if word in pet name is only alphabetic characters - 
    # if true append word to pet_name separated by trailing space 
    for word in word_list_pet_image:
        if word.isalpha():
            pet_name += word + " "

    # Strip off starting/trailing whitespace characters 
    pet_name = pet_name.strip()

    # Returns resulting pet_name
    return pet_name

def create_dict(image_dir):

    # Retrieve the filenames from folder pet_images/
    # print("--- first_filename_list ---")
    first_filename_list = listdir(image_dir)
    # printList(first_filename_list)

    # Filter file name. We need to add a conditional statement that ignores hidden files (those that start with a dot '.')
    # print("--- filename_list ---")
    filename_list = []
    for idx in range(0, len(first_filename_list), 1):
        if not first_filename_list[idx].startswith('.'):
            filename_list.append(first_filename_list[idx])
    # printList(filename_list)

    # Print 10 of the filenames from folder pet_images/
    print("\nPrints 10 filenames from folder pet_images/")
    for idx in range(0, 10, 1):
        print("{:2d} file: {:>25}".format(idx + 1, filename_list[idx]))

    # Creates empty dictionary named results_dic
    results_dic = dict()

    # Determines number of items in dictionary
    items_in_dic = len(results_dic)
    print("\nEmpty Dictionary results_dic - n items=", items_in_dic)

    # Adds new key-value pairs to dictionary ONLY when key doesn't already exist. 
    # This dictionary's value is a List that contains only one item - the pet image label.
    for idx in range(0, len(filename_list), 1):
        if filename_list[idx] not in results_dic:
            results_dic[filename_list[idx]] = get_pet_label(filename_list[idx])
        else:
            print("** Warning: Key=", filename_list[idx], "already exists in results_dic with value =", results_dic[filename_list[idx]])
    
    return results_dic

def get_pet_labels(image_dir):   
    results_dic = create_dict(image_dir)
    for item in results_dic.items():
        print(item)

def printList(list):
    for idx in range(0, len(list), 1):
        print("{}".format(list[idx]))

#----------------------------------------------------------------------------------------------------

get_pet_labels("pet_images/")
