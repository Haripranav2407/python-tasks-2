cgpa = float(input("Enter CGPA: "))
attend = int(input("Enter the attendanc percentage: "))
arrear = int(input("Arrears: "))
if cgpa >= 7.0 and attend >=75 and arrear == 0:
    print("ELIGIBLE")
else:
    print("NOT ELIGIBLE")    