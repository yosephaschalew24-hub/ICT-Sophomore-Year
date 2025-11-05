def Conversion(Reading, Type):
    if Type == "C2F":
        result = round((Reading * 9/5) + 32, 2)
        print(f"{Reading}ºC is equal to {result}ºF.")
    elif Type == "F2C":
        result = round((Reading - 32) * 5/9, 2)
        print(f"{Reading}ºF is equal to {result}ºC.")
    elif Type == "M2F":
        result = round(Reading * 3.28084, 2)
        print(f"{Reading} meters is equal to {result} feet.")
    elif Type == "F2M":
        result = round(Reading / 3.28084, 2)
        print(f"{Reading} feet is equal to {result} meters.")
    else:
        print("Please input a valid conversion type (C2F, F2C, M2F, or F2M).")

Reading = float(input("Please enter your reading (temperature or length): "))
Type = input("Please input your desired conversion type (C2F, F2C, M2F, or F2M): ")
Conversion(Reading, Type)
