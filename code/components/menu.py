# Menu table for selection of file


# -----IMPORTS-----
import os

# -----CODE--------

def menu():
    
    print("\nPlease choose one of these files -- input the number next to the file.\n")
    
    file_names = os.listdir("./input/")
    
    counter = -1
    
    for name in file_names:
        counter = counter + 1
        print(f"\t[{counter}] - {name}")
    
    while True:
        
        choice = input("\nChoice: ")
        
        try:
            choice = int(choice)
            
            if choice > counter or choice < 0:
                print("\nYou need to choose from the numbers of the list.")
                continue
            else:
                return file_names[choice]
        
        except Exception as e:
            print("\nYou need to choose a number from the list")
            continue
            