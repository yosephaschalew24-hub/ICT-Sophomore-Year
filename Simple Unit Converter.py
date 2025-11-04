def Temp_Conversion(Reading,Type):
    if Type == "C2F":
        result = round((Reading * 9/5) + 32 , 2)
        print(f"{Reading}º C is equal to {result}º F.")
    elif Type == "F2C":
        result = round((Reading - 32) * 5/9 , 2)
        print(f"{Reading}º F is equal to {result}º C.")
    else:
        print("Please input a valid conversion type.")
        
Reading = float(input("Please enter your temperature reading:"))
Type = input("Please input your desired conversion type, either C2F or F2C.")
Temp_Conversion(Reading,Type)
    

