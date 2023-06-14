"""File Contains Dashboard for the Face Recognitions"""
import winsound,sys,os
# TODO List:
# 1. start program 
# 2. add new student
# 3. 


def start_program():
    """Function Used to start face recognition from live camera"""
    print("curr dir",os.getcwd())
    os.system("python reco_from_video.py")

def add_new_student_face():
    """Function Used to add a new student face and then train the models"""
    os.system("python data_collect.py")
    os.system("python train_model_from_image.py")

function_map = {"1":start_program,"2":add_new_student_face}

first_page = """
Hi We Are Glad To Have You Here
Choose from  the following options
1. Start The Program 
2. Add New Student 
--> """

print(first_page,end="")
option_selected= input()
print("You Selected ",option_selected)
if option_selected not in function_map:
    winsound.Beep(1500,300)
    print("Which is Invalid")
    sys.exit() # close the program 
function_map[option_selected]()


