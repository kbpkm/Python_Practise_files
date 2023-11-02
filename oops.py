class Student:
   def __init__(self,name,house):
        if not name:
         raise ValueError("Missing name")
        if house not in ["Madikonda","Kazipet","Hanamakonda"]:
         raise ValueError("Invalid house")    
        self.Name = name
        self.house = house 
        
   def __str__(self):
     return f"{self.Name} from {self.house}"  

def main():
    student =get_student()
    print(student) 
  
def get_student():
    Name=input("Name: ")
    house=input("House: ")
    return  Student(Name.title(),house.title())

if __name__=="__main__":
    main()   
