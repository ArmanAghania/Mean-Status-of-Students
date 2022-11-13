import statistics

print("Student A")
name_A = input("Name: ")
scoreA = float(input("Math Score? "))
scoreB = float(input("Science Score? "))
scoreC = float(input("Literature Score? "))

a = [scoreA, scoreB, scoreC]

m = round(statistics.mean(a), 2)

if m >= 17:
    print(name_A, "Your Average is: ", m, "- Great")
elif m < 17 and m >= 12:
    print(name_A, "Your Average is: ", m, "- Average")
else:
    print(name_A, "Your Average is: ", m, "- Failed")



