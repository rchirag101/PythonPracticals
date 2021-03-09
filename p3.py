import datetime
# functions scoping


def getDate():
    dt = datetime.datetime.now().date()

    def printDate():
        print("Today's date: " + str(dt))
    printDate()
getDate()


# Recursion
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * (factorial(n - 1))
print("Factorial of 5 :", factorial(5))

# List Mutablity
deptList = ["CE", "IT", "BM", "EC"]
print("Inital List :", deptList)
deptList.append("IC")
print("After Appending :", deptList)
deptList.pop()
deptList.pop()
print("After Popping :", deptList)
