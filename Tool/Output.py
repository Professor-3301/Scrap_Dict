from Logo import *

def save(output_data):
    # Specify the file path where you want to save the text file
    file_path = "./output.txt"

    try:
    # Open the file in write mode and write the data
    
        with open(file_path, 'a') as file:
            file.write(output_data)
    
        print(f"Data has been saved to {file_path}")

    except Exception as e:
        print(f"An error occurred while saving the data to {file_path}: {str(e)}")

def Save_All(choice,result):
    file_path = input("Enter the path to File(Including File Name) :")
    if choice == '2':
        save(print_normal_logo())
        save("\n\n\nScraped Links\n-------------\n")
        save(result)
        
