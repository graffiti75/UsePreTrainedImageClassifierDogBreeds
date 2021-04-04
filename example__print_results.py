from classifier import classifier 
from get_input_args import get_input_args
from os import listdir

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/print_results_hints.py
#                                                                             
# PROGRAMMER: 
# DATE CREATED:
# REVISED DATE: 
# PURPOSE: This is a *hints* file to help guide students in creating the 
#          function print_results that prints the results statistics from the
#          results statistics dictionary (results_stats_dic). It should also
#          allow the user to be able to print out cases of misclassified
#          dogs and cases of misclassified breeds of dog using the Results 
#          dictionary (results_dic).  
#         This function inputs:
#            - The results dictionary as results_dic within print_results 
#             function and results for the function call within main.
#            - The results statistics dictionary as results_stats_dic within 
#             print_results function and results_stats for the function call within main.
#            - The CNN model architecture as model wihtin print_results function
#             and in_arg.arch for the function call within main. 
#            - Prints Incorrectly Classified Dogs as print_incorrect_dogs within
#             print_results function and set as either boolean value True or 
#             False in the function call within main (defaults to False)
#            - Prints Incorrectly Classified Breeds as print_incorrect_breed within
#             print_results function and set as either boolean value True or 
#             False in the function call within main (defaults to False)
#         This function does not output anything other than printing a summary
#         of the final results.
##
# TODO 6: EDIT and ADD code BELOW to do the following that's stated in the 
#       comments below that start with "TODO: 6" for the print_results function.
#       Specifically edit and add code below within the the print_results function. 
#       Notice that this function doesn't return anything because it prints 
#       a summary of the results using results_dic and results_stats_dic
# 
def print_results(results_dic, results_stats_dic, model, 
                  print_incorrect_dogs = False, print_incorrect_breed = False):
    """
    Prints summary results on the classification and then prints incorrectly 
    classified dogs and incorrectly classified dog breeds if user indicates 
    they want those printouts (use non-default values)
    Parameters:
      results_dic - Dictionary with key as image filename and value as a List 
             (index)idx 0 = pet image label (string)
                    idx 1 = classifier label (string)
                    idx 2 = 1/0 (int)  where 1 = match between pet image and 
                            classifer labels and 0 = no match between labels
                    idx 3 = 1/0 (int)  where 1 = pet image 'is-a' dog and 
                            0 = pet Image 'is-NOT-a' dog. 
                    idx 4 = 1/0 (int)  where 1 = Classifier classifies image 
                            'as-a' dog and 0 = Classifier classifies image  
                            'as-NOT-a' dog.
      results_stats_dic - Dictionary that contains the results statistics (either
                   a  percentage or a count) where the key is the statistic's 
                     name (starting with 'pct' for percentage or 'n' for count)
                     and the value is the statistic's value 
      model - Indicates which CNN model architecture will be used by the 
              classifier function to classify the pet images,
              values must be either: resnet alexnet vgg (string)
      print_incorrect_dogs - True prints incorrectly classified dog images and 
                             False doesn't print anything(default) (bool)  
      print_incorrect_breed - True prints incorrectly classified dog breeds and 
                              False doesn't print anything(default) (bool) 
    Returns:
           None - simply printing results.
    """   
    # Prints summary statistics over the run
    print("\n\n*** Results Summary for CNN Model Architecture",model.upper(), 
          "***")
    print("{:20}: {:3d}".format('N Images', results_stats_dic['n_images']))
    print("{:20}: {:3d}".format('N Dog Images', results_stats_dic['n_dogs_img']))

    # TODO: 6a. REPLACE print("") with CODE that prints the text string 
    #          'N Not-Dog Images' and then the number of NOT-dog images 
    #          that's accessed by key 'n_notdogs_img' using dictionary 
    #          results_stats_dic
    #
    # print("")
    print("{:20}: {:3d}".format('N Not-Dog Images', results_stats_dic['n_notdogs_img']))

    # Prints summary statistics (percentages) on Model Run

    ('pct_match', 0.0)
    ('pct_correct_dogs', 0.0)
    ('pct_correct_breed', 0.0)
    ('pct_correct_notdogs', 70.0)

    # Source:
    # https://stackoverflow.com/a/17106842/1354788
    print(" ")
    for key in results_stats_dic:
        # TODO: 6b. REPLACE pass with CODE that prints out all the percentages 
        #           in the results_stats_dic dictionary. Recall that all 
        #           percentages in results_stats_dic have 'keys' that start with 
        #           the letter p. You will need to write a conditional 
        #           statement that determines if the key starts with the letter
        #           'p' and then you want to use a print statement to print 
        #           both the key and the value. Remember the value is accessed 
        #           by results_stats_dic[key]
        #
        if key.startswith('p'):
            print("{:20}: {:3f}".format(key, results_stats_dic[key]))

    # IF print_incorrect_dogs == True AND there were images incorrectly 
    # classified as dogs or vice versa - print out these cases
    if (print_incorrect_dogs and 
        ( (results_stats_dic['n_correct_dogs'] + results_stats_dic['n_correct_notdogs'])
          != results_stats_dic['n_images'] ) 
       ):
        print("\nINCORRECT Dog/NOT Dog Assignments:")

        # process through results dict, printing incorrectly classified dogs
        for key in results_dic:

            # TODO: 6c. REPLACE pass with CODE that prints out the pet label 
            #           and the classifier label from results_dic dictionary    
            #           ONLY when the classifier function (classifier label) 
            #           misclassified dogs specifically: 
            #             pet label is-a-dog and classifier label is-NOT-a-dog 
            #               -OR- 
            #             pet label is-NOT-a-dog and classifier label is-a-dog 
            #          You will need to write a conditional statement that 
            #          determines if the classifier function misclassified dogs
            #          See 'Adjusting Results Dictionary' section in 
            #         'Classifying Labels as Dogs' for details on the 
            #          format of the results_dic dictionary. Remember the value
            #          is accessed by results_dic[key] and the value is a list
            #          so results_dic[key][idx] - where idx represents the 
            #          index value of the list and can have values 0-4.
            #
            # Pet Image Label is a Dog - Classified as NOT-A-DOG -OR- 
            # Pet Image Label is NOT-a-Dog - Classified as a-DOG
            
            # case1 = results_dic[key][3] == 1 and results_dic[key][4] == 0
            # case2 = results_dic[key][3] == 0 and results_dic[key][4] == 1
            # if case1 or case2:
            if ( sum(results_dic[key][3:]) == 1 ):
                print("Real: {:>26} Classifier: {:>30}".format(results_dic[key][0], results_dic[key][1]))

    # IF print_incorrect_breed == True AND there were dogs whose breeds 
    # were incorrectly classified - print out these cases                    
    if (print_incorrect_breed and 
        (results_stats_dic['n_correct_dogs'] != results_stats_dic['n_correct_breed']) 
       ):
        print("\nINCORRECT Dog Breed Assignment:")

        # process through results dict, printing incorrectly classified breeds
        for key in results_dic:

            # Pet Image Label is-a-Dog, classified as-a-dog but is WRONG breed
            if ( sum(results_dic[key][3:]) == 2 and
                results_dic[key][2] == 0 ):
                print("Real: {:>26} Classifier: {:>30}".format(results_dic[key][0],
                                                          results_dic[key][1]))

#----------------------------------------------------------------------------------------------------
# METHODS FROM OTHER LESSONS
#----------------------------------------------------------------------------------------------------

def calculates_results_stats(results_dic):
    """
    Calculates statistics of the results of the program run using classifier's model 
    architecture to classifying pet images. Then puts the results statistics in a 
    dictionary (results_stats_dic) so that it's returned for printing as to help
    the user to determine the 'best' model for classifying images. Note that 
    the statistics calculated as the results are either percentages or counts.
    Parameters:
      results_dic - Dictionary with key as image filename and value as a List 
             (index)idx 0 = pet image label (string)
                    idx 1 = classifier label (string)
                    idx 2 = 1/0 (int)  where 1 = match between pet image and 
                            classifer labels and 0 = no match between labels
                    idx 3 = 1/0 (int)  where 1 = pet image 'is-a' dog and 
                            0 = pet Image 'is-NOT-a' dog. 
                    idx 4 = 1/0 (int)  where 1 = Classifier classifies image 
                            'as-a' dog and 0 = Classifier classifies image  
                            'as-NOT-a' dog.
    Returns:
     results_stats_dic - Dictionary that contains the results statistics (either
                    a percentage or a count) where the key is the statistic's 
                     name (starting with 'pct' for percentage or 'n' for count)
                     and the value is the statistic's value. See comments above
                     and the classroom Item XX Calculating Results for details
                     on how to calculate the counts and statistics.
    """        
    # Creates empty dictionary for results_stats_dic
    results_stats_dic = dict()
    
    # Sets all counters to initial values of zero so that they can 
    # be incremented while processing through the images in results_dic 
    results_stats_dic['n_dogs_img'] = 0
    results_stats_dic['n_match'] = 0
    results_stats_dic['n_correct_dogs'] = 0
    results_stats_dic['n_correct_notdogs'] = 0
    results_stats_dic['n_correct_breed'] = 0
    
    # process through the results dictionary
    for key in results_dic:
         
        # Labels Match Exactly
        if results_dic[key][2] == 1:
            results_stats_dic['n_match'] += 1

        # TODO: 5a. REPLACE pass with CODE that counts how many pet images of
        #           dogs had their breed correctly classified. This happens 
        #           when the pet image label indicates the image is-a-dog AND 
        #           the pet image label and the classifier label match. You 
        #           will need to write a conditional statement that determines
        #           when the dog breed is correctly classified and then 
        #           increments 'n_correct_breed' by 1. Recall 'n_correct_breed' 
        #           is a key in the results_stats_dic dictionary with it's value 
        #           representing the number of correctly classified dog breeds.
        #           
        # Pet Image Label is a Dog AND Labels match- counts Correct Breed
        if results_dic[key][3] == 1 and results_dic[key][2] == 1:
            results_stats_dic['n_correct_breed'] += 1
        
        # Pet Image Label is a Dog - counts number of dog images
        if results_dic[key][3] == 1:
            results_stats_dic['n_dogs_img'] += 1
            
            # Classifier classifies image as Dog (& pet image is a dog)
            # counts number of correct dog classifications
            if results_dic[key][4] == 1:
                results_stats_dic['n_correct_dogs'] += 1

        # TODO: 5b. REPLACE pass with CODE that counts how many pet images 
        #           that are NOT dogs were correctly classified. This happens 
        #           when the pet image label indicates the image is-NOT-a-dog 
        #           AND the classifier label indicates the images is-NOT-a-dog.
        #           You will need to write a conditional statement that 
        #           determines when the classifier label indicates the image 
        #           is-NOT-a-dog and then increments 'n_correct_notdogs' by 1. 
        #           Recall the 'else:' above 'pass' already indicates that the 
        #           pet image label indicates the image is-NOT-a-dog and 
        #          'n_correct_notdogs' is a key in the results_stats_dic dictionary 
        #           with it's value representing the number of correctly 
        #           classified NOT-a-dog images.
        #           
        # Pet Image Label is NOT a Dog
        else:
            # Classifier classifies image as NOT a Dog(& pet image isn't a dog)
            # counts number of correct NOT dog clasifications.
            if results_dic[key][2] == 1 and results_dic[key][3] == 0 and results_dic[key][4] == 0:
                results_stats_dic['n_correct_notdogs'] += 1


    # Calculates run statistics (counts & percentages) below that are calculated
    # using the counters from above.

    # calculates number of total images
    results_stats_dic['n_images'] = len(results_dic)

    # calculates number of not-a-dog images using - images & dog images counts
    results_stats_dic['n_notdogs_img'] = (results_stats_dic['n_images'] - 
                                      results_stats_dic['n_dogs_img']) 

    # TODO: 5c. REPLACE zero(0.0) with CODE that calculates the % of correctly
    #           matched images. Recall that this can be calculated by the
    #           number of correctly matched images ('n_match') divided by the 
    #           number of images('n_images'). This result will need to be 
    #           multiplied by 100.0 to provide the percentage.
    #    
    # Calculates % correct for matches
    results_stats_dic['pct_match'] = (results_stats_dic['n_match'] / results_stats_dic['n_images']) * 100

    # TODO: 5d. REPLACE zero(0.0) with CODE that calculates the % of correctly
    #           classified dog images. Recall that this can be calculated by 
    #           the number of correctly classified dog images('n_correct_dogs')
    #           divided by the number of dog images('n_dogs_img'). This result 
    #           will need to be multiplied by 100.0 to provide the percentage.
    #    
    # Calculates % correct dogs
    results_stats_dic['pct_correct_dogs'] = (results_stats_dic['n_correct_dogs'] / results_stats_dic['n_dogs_img']) * 100

    # TODO: 5e. REPLACE zero(0.0) with CODE that calculates the % of correctly
    #           classified breeds of dogs. Recall that this can be calculated 
    #           by the number of correctly classified breeds of dog('n_correct_breed') 
    #           divided by the number of dog images('n_dogs_img'). This result 
    #           will need to be multiplied by 100.0 to provide the percentage.
    #    
    # Calculates % correct breed of dog
    results_stats_dic['pct_correct_breed'] = (results_stats_dic['n_correct_breed'] / results_stats_dic['n_dogs_img']) * 100

    # Calculates % correct not-a-dog images
    # Uses conditional statement for when no 'not a dog' images were submitted 
    if results_stats_dic['n_notdogs_img'] > 0:
        results_stats_dic['pct_correct_notdogs'] = (results_stats_dic['n_correct_notdogs'] /
                                                   results_stats_dic['n_notdogs_img']) * 100.0
    else:
        results_stats_dic['pct_correct_notdogs'] = 0.0

        
    # TODO 5f. REPLACE None with the results_stats_dic dictionary that you 
    # created with this function 
    return results_stats_dic

def adjust_results4_isadog(results_dic, dogfile):
    """
    Adjusts the results dictionary to determine if classifier correctly 
    classified images 'as a dog' or 'not a dog' especially when not a match. 
    Demonstrates if model architecture correctly classifies dog images even if
    it gets dog breed wrong (not a match).
    Parameters:
      results_dic - Dictionary with 'key' as image filename and 'value' as a 
                    List. Where the list will contain the following items: 
                  index 0 = pet image label (string)
                  index 1 = classifier label (string)
                  index 2 = 1/0 (int)  where 1 = match between pet image
                    and classifer labels and 0 = no match between labels
                ------ where index 3 & index 4 are added by this function -----
                 NEW - index 3 = 1/0 (int)  where 1 = pet image 'is-a' dog and 
                            0 = pet Image 'is-NOT-a' dog. 
                 NEW - index 4 = 1/0 (int)  where 1 = Classifier classifies image 
                            'as-a' dog and 0 = Classifier classifies image  
                            'as-NOT-a' dog.
     dogfile - A text file that contains names of all dogs from the classifier
               function and dog names from the pet image files. This file has 
               one dog name per line dog names are all in lowercase with 
               spaces separating the distinct words of the dog name. Dog names
               from the classifier function can be a string of dog names separated
               by commas when a particular breed of dog has multiple dog names 
               associated with that breed (ex. maltese dog, maltese terrier, 
               maltese) (string - indicates text file's filename)
    Returns:
           None - results_dic is mutable data type so no return needed.
    """           
    # Creates dognames dictionary for quick matching to results_dic labels from
    # real answer & classifier's answer
    dognames_dic = dict()

    # Reads in dognames from file, 1 name per line & automatically closes file
    with open(dogfile, "r") as infile:
        # Reads in dognames from first line in file
        line = infile.readline()

        # Processes each line in file until reaching EOF (end-of-file) by 
        # processing line and adding dognames to dognames_dic with while loop
        while line != "":
            # print("----- line: {}".format(line))

            # TODO: 4a. REPLACE pass with CODE to remove the newline character
            #           from the variable line  
            #
            # Process line by striping newline from line
            line = line.strip('\n')

            # TODO: 4b. REPLACE pass with CODE to check if the dogname(line) 
            #          exists within dognames_dic, then if the dogname(line) 
            #          doesn't exist within dognames_dic then add the dogname(line) 
            #          to dognames_dic as the 'key' with the 'value' of 1. 
            #
            # adds dogname(line) to dogsnames_dic if it doesn't already exist 
            # in the dogsnames_dic dictionary
            if line not in dognames_dic:
                dognames_dic[line] = 1
                # print("----- dognames_dic[{}]: {}".format(line, dognames_dic[line]))

            # Reads in next line in file to be processed with while loop
            # if this line isn't empty (EOF)
            line = infile.readline()

                
    # Add to whether pet labels & classifier labels are dogs by appending
    # two items to end of value(List) in results_dic. 
    # List Index 3 = whether(1) or not(0) Pet Image Label is a dog AND 
    # List Index 4 = whether(1) or not(0) Classifier Label is a dog
    # How - iterate through results_dic if labels are found in dognames_dic
    # then label "is a dog" index3/4=1 otherwise index3/4=0 "not a dog"
    for key in results_dic:

        # Pet Image Label IS of Dog (e.g. found in dognames_dic)
        if results_dic[key][0] in dognames_dic:
            
            # Classifier Label IS image of Dog (e.g. found in dognames_dic)
            # appends (1, 1) because both labels are dogs
            if results_dic[key][1] in dognames_dic:
                results_dic[key].extend((1, 1))
                # ('cat_01.jpg', ['cat', 'lynx', 0])
                # ('Poodle_07927.jpg', ['poodle', 'standard poodle, poodle', 1])

            # TODO: 4c. REPLACE pass BELOW with CODE that adds the following to
            #           results_dic dictionary for the key indicated by the 
            #           variable key - append (1,0) to the value using 
            #           the extend list function. This indicates
            #           the pet label is-a-dog, classifier label is-NOT-a-dog. 
            #                              
            # Classifier Label IS NOT image of dog (e.g. NOT in dognames_dic)
            # appends (1,0) because only pet label is a dog
            else:
                results_dic[key].extend((1, 0))

        # Pet Image Label IS NOT a Dog image (e.g. NOT found in dognames_dic)
        else:
            # TODO: 4d. REPLACE pass BELOW with CODE that adds the following to
            #           results_dic dictionary for the key indicated by the 
            #           variable key - append (0,1) to the value uisng
            #           the extend list function. This indicates
            #           the pet label is-NOT-a-dog, classifier label is-a-dog. 
            #                              
            # Classifier Label IS image of Dog (e.g. found in dognames_dic)
            # appends (0, 1)because only Classifier labe is a dog
            if results_dic[key][1] in dognames_dic:
                results_dic[key].extend((0, 1))

            # TODO: 4e. REPLACE pass BELOW with CODE that adds the following to
            #           results_dic dictionary for the key indicated by the 
            #           variable key - append (0,0) to the value using the 
            #           extend list function. This indicates
            #           the pet label is-NOT-a-dog, classifier label is-NOT-a-dog. 
            #                                              
            # Classifier Label IS NOT image of Dog (e.g. NOT in dognames_dic)
            # appends (0, 0) because both labels aren't dogs
            else:
                results_dic[key].extend((0, 0))

def classify_images(images_dir, results_dic, model):
    """
    Creates classifier labels with classifier function, compares pet labels to 
    the classifier labels, and adds the classifier label and the comparison of 
    the labels to the results dictionary using the extend function. Be sure to
    format the classifier labels so that they will match your pet image labels.
    The format will include putting the classifier labels in all lower case 
    letters and strip the leading and trailing whitespace characters from them.
    For example, the Classifier function returns = 'Maltese dog, Maltese terrier, Maltese' 
    so the classifier label = 'maltese dog, maltese terrier, maltese'.
    Recall that dog names from the classifier function can be a string of dog 
    names separated by commas when a particular breed of dog has multiple dog 
    names associated with that breed. For example, you will find pet images of
    a 'dalmatian'(pet label) and it will match to the classifier label 
    'dalmatian, coach dog, carriage dog' if the classifier function correctly 
    classified the pet images of dalmatians.
     PLEASE NOTE: This function uses the classifier() function defined in 
     classifier.py within this function. The proper use of this function is
     in test_classifier.py Please refer to this program prior to using the 
     classifier() function to classify images within this function 
     Parameters: 
      images_dir - The (full) path to the folder of images that are to be
                   classified by the classifier function (string)
      results_dic - Results Dictionary with 'key' as image filename and 'value'
                    as a List. Where the list will contain the following items: 
                  index 0 = pet image label (string)
                --- where index 1 & index 2 are added by this function ---
                  NEW - index 1 = classifier label (string)
                  NEW - index 2 = 1/0 (int)  where 1 = match between pet image
                    and classifer labels and 0 = no match between labels
      model - Indicates which CNN model architecture will be used by the 
              classifier function to classify the pet images,
              values must be either: resnet alexnet vgg (string)
     Returns:
           None - results_dic is mutable data type so no return needed.         
    """
    
    # None 

    filename_list = listdir("pet_images/")
    idx = 0
    for key in results_dic:
        # print("---------------")

        value=results_dic[key]
        # print("\t-----key={}".format(key))
        # print("\t-----value={}".format(value))
        
        path = images_dir + filename_list[idx]
        # print("\t-----path={}".format(path))
        
        model_label = classifier(path, model)
        model_label = model_label.lower()
        model_label = model_label.strip()
        # print("\t-----model_label={}".format(model_label))
        
        truth = 0
        if value in model_label:
            truth = 1

        results_dic[key] = [ value, model_label, truth ]
        # print("\t-----truth={}".format(truth))
        idx = idx + 1

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

def print_dict(dict):
    for item in dict.items():
        print(item)

def main():
    in_arg = get_input_args()
    filename_list = listdir("pet_images/")
    results_dic = dict()
    for idx in range(0, len(filename_list), 1):
        if filename_list[idx] not in results_dic:
            results_dic[filename_list[idx]] = get_pet_label(filename_list[idx])
    classify_images(in_arg.dir, results_dic, in_arg.arch)
    adjust_results4_isadog(results_dic, in_arg.dogfile)
    results_stats_dic = calculates_results_stats(results_dic)
    # print_dict(results_dic_output)
    print_results(results_dic, results_stats_dic, in_arg.arch, True, True)

#----------------------------------------------------------------------------------------------------

main()