import os
import json


def main():

    file_name = input("Enter your file name : ")
    confirm_input =input("Do you want to confirm it ? y/n :")
    if confirm_input == "y":
        file_name_temp = file_name.split('.')
        if os.path.exists(file_name) :
            print("The File exists")
            n_file_name = input("Please enter the new name for your file :")
            file_name = n_file_name
            n_file_name_temp = n_file_name.split('.')
            if n_file_name_temp[1] == 'json':
                print('proceeding to next')
                createFile(file_name)
            else:
                print("Sorry wrong file type \n Exiting the program")
                exit()
        else:
            if file_name_temp[1] == 'json':
                print('proceeding to next')
                createFile(file_name)
            else:
                print("Sorry wrong file type \n Exiting the program")
                exit()
    else:
        new_file_name = input("Please Enter new File name :")


def createFile(file_name):
    print("creating file to write data")
    json_obj=[]
    with open(file_name,'w') as jsonFile:
        json.dump(json_obj,jsonFile)
        print("file Created \n getting user data")
        getData(json_obj)

def getData(json_obj):
    print("The existing Data in the file",json_obj)
    print("Enter your key & value below")
    key= input("Enter the key you want to add in the json file")
    value = input("enter the value you want to add for the relative key")
    print('key',key)
    print('value',value)


if __name__ == "__main__":
    main()