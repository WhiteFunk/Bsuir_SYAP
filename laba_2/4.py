try:
    numerator = float(input("Input Numerator: "))
    denominator = float(input("Input Denominator: "))

    result = numerator/denominator

    print(result)
except:
    print("Something has gone wrong")
finally:
    print("You finally did it!")