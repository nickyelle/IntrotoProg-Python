
#----------------------------------------------------------------
# Title: Assignment 8
# Dev:   NDietrich
# Date:  September 3, 2018
# Purpose: Organize the sample code into classes
# Change Log: September 3, 2018 - I have added a class titled ExecuteProgram
# ----------------------------------------------------------------
#--make the class ---
class ExecuteProgram(object): #creating a class
#---Fields---
    objFile = None #File Handle
    strUserInput = None #A string which holds user input

#---Constructors---
    def __init__(self, ProductID = "",ProductName ="",Price =""):
        #add the constrcutor attributes
        self.__ProductID = ProductID #Private attribute
        self.__ProductName = ProductName #Private attribute
        self.__Price = Price #Private attribute

       #--add the properties---
        #ProductID Properties
        @property #getter
        def ProductID(self):
            return self.__ProductID
        @ProductID.setter #(mutator)
        def ProductID(self,Value):
            self.__ProductID = Value

        # ProductName Properties
        @property  # getter
        def ProductName(self):
            return self.__ProductName

        @ProductName.setter  # (mutator)
        def ProductName(self, Value):
            self.__ProductName = Value

        # ProductPrice Properties
        @property  # getter
        def Price(self):
            return self.__Price

        @Price.setter  # (mutator)
        def Price(self, Value):
            self.__Price = Value
    #Methods
    def ToString (self):# return the 3 product data fields
        return self.__ProductID + "," +  self.__ProductName +", " + self.__Price
    def WriteProductUserInput(File):
      try:
        print("Type in a Product Id, Name, and Price you want to add to the file")
        print("(Enter 'Exit' to quit!)")
        while(True):
          strUserInput = input("Enter the Id, Name, and Price (ex. 1,ProductA,9.99): ")
          if(strUserInput.lower() == "exit"): break
          else: File.write(strUserInput + "\n")
      except Exception as e:
        print("Error: " + str(e))

    def ReadAllFileData(File, Message="Contents of File"):
      try:
        print(Message)
        File.seek(0)
        print(File.read())
      except Exception as e:
        print("Error: " + str(e))

#---Use the class ---
try:
  objFile = open("Products.txt", "r+")
  ExecuteProgram.ReadAllFileData(objFile, "Here is the current data:")
  ExecuteProgram.WriteProductUserInput(objFile)
  ExecuteProgram.ReadAllFileData(objFile, "Here is this data was saved:")
except FileNotFoundError as e:
     print("Error: " + str(e) + "\n Please check the file name")
except Exception as e:
    print("Error: " + str(e))
finally:
  if(objFile != None):objFile.close()