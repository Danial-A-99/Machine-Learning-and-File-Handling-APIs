
import os
class File_manipulator:

    def __init__(self,file_name):
        self.file_name = file_name

    def set_file_name(self,new_name):
        self.file_name = new_name

    def file_exists(self):
        try:
            open(self.file_name,"r")
            return True
        except FileNotFoundError:
            return False

    def create_file(self):
        if self.file_exists() == False:
            open(self.file_name,"a")
        else:
            print("File Already Exists")

    def delete_file(self):
        if self.file_exists() == True:
            os.remove(self.file_name)
        else:
            print("File Does Not Exist")

    def append_to_file(self,text_to_write):
        if self.file_exists() == True:
            f = open(self.file_name,"a")
            f.write(f"{text_to_write}\n")
        else:
            print("File Cannot Be Written To As It Doesn't Exist")
    
    def overwrite_file(self,text_to_write):
        if self.file_exists() == True:
            f = open(self.file_name,"w")
            f.write(f"{text_to_write}\n")
        else:
            print("File Cannot Be Written To As It Doesn't Exist")

    def clear_file(self):
        if self.file_exists() == True:
            f = open(self.file_name,"w")
            f.write("")
        else:
            print("File Cannot Be Written To As It Doesn't Exist")
    
    def file_contents(self):
        if self.file_exists():
            return str(open(self.file_name,"r").read())
        else:
            return "No File & No Contents"
        
    def display_contents(self):
        print(f"File Contents:\n{self.file_contents()}")