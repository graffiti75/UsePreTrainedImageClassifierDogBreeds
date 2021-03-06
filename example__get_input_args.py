import argparse

def get_input_args():
    """
    Retrieves and parses the 3 command line arguments provided by the user when
    they run the program from a terminal window. This function uses Python's 
    argparse module to created and defined these 3 command line arguments. If 
    the user fails to provide some or all of the 3 arguments, then the default 
    values are used for the missing arguments. 
    Command Line Arguments:
      1. Image Folder as --dir with default value 'pet_images'
      2. CNN Model Architecture as --arch with default value 'vgg'
      3. Text File with Dog Names as --dogfile with default value 'dognames.txt'
    This function returns these arguments as an ArgumentParser object.
    Parameters:
     None - simply using argparse module to create & store command line arguments
    Returns:
     parse_args() -data structure that stores the command line arguments object  
    """
    # Replace None with parser.parse_args() parsed argument collection that 
    # you created with this function 

    # Creates Argument Parser object named parser
    parser = argparse.ArgumentParser()

    # Argument 1: that's a path to a folder
    parser.add_argument('--dir', type = str, default = 'pet_images/', help = 'Path to the folder of pet images') 
    parser.add_argument('--arch', type = str, default = 'vgg', help = 'CNN Model Architecture Algorythm') 
    parser.add_argument('--dogfile', type = str, default = 'dognames.txt', help = 'Text file with dog names') 

    return parser.parse_args()

args = get_input_args()
print("Argument 1:", args.dir)
print("Argument 2:", args.arch)
print("Argument 3:", args.dogfile)