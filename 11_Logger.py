
class Logger:

    def log(self,message,level="info"):
        if level.lower()=="warning":
            print("Warning:",message)
        elif level.lower()=="error":
            print("Error Message :",message)
        else:
            print("Information Message :",message)

L=Logger()
L.log("Your code contains logical error.","warning")
L.log("Your code contains an error.","error")
L.log("Your code is compiled properly.")