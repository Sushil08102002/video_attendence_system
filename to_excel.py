import pandas as pd
import os


class Excel_handle:
    "File used to handle attendance excel file"
    def __init__(self):
        self.df = None # to store dataframe
        self.file_name = "Attendence.xlsx"

    def check_file(self,file_name):
        """Function Used To Check File Present or Not"""
        try: # if file found then this
            files = os.listdir(".")
            # print("files in folder",files) 
            if file_name in files:
                print("File Found")
                return True
            return False # when not found
        except Exception as error: # if file not found with the given name 
            print("Exception While Finding File",error)
            return False

    def read_excel(self,file_name):
        """function used to read excel data"""
        file_present = self.check_file(file_name)
        if file_present: # if file present  read the 
            print("excel file present")
            df = pd.read_excel(file_name,engine="openpyxl",index_col=0)
            self.df = df
            return df
        else: # create file
            print("Creating file")
            pd.DataFrame({"Enrollment Number":[],"Name":[],"Attendance":[]}).to_excel(file_name)
            df = pd.read_excel(file_name)
            self.df = df
            return df

    def check_student(self,df,student_name):
        """Function Used To Check Student Name present or not in df
        args:
            df: df from Excel must contain Names column"""
        students = self.df.Name.values
        if student_name in students:
            return True
        return False
    
    def update_student_status(self,student_name,status):
        """Function Used to Update Student status in excel_file"""
        if type(self.df)!= None: # if not None
            if not self.df.empty:
                df = self.read_excel(self.file_name)
                student_current_status  = self.check_student(df,student_name)
                if student_current_status:
                    student_index = df[df['Name']==student_name].index[0]
                    self.df.iloc[student_index].Attendance = "P"
                    print("Student Status Updated")
                else:
                    self.df = self.df._append({"Name":student_name,"Attendance":status},ignore_index=True)
                    self.df.to_excel(self.file_name)

                    print("student status updated")
                    
            else:
                self.check_file(self.file_name)
                df = self.read_excel(self.file_name)
                self.df = self.df._append({"Name":student_name,"Attendance":status},ignore_index=True)
                self.df.to_excel(self.file_name)
                print("student status updated")


            # raise TypeError("Invalid Function Order Functions Must Be Executed in A Sequence") 









if __name__=="__main__":
    excel= Excel_handle()
    df = excel.read_excel("Attendance.xlsx")
    student_status = excel.check_student(df,"kuch nahi")
    # print(df)
    print("student_status",student_status)
    excel.update_student_status('shubham',"P")

    
       