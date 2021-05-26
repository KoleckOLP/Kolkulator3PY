from kolreq.kolreq import clear, readchar


def number():
    number = input("#")
    try:
        number = float(number)
    except ValueError:
        print("not a number")
        number()
    return number


def paktc():
    input("press any key to continue")


def Debug():
    print("so far nothing.")


def Add():
    clear()
    print("type the first number")
    num1 = number()
    print("type the second number")
    num2 = number()
    res = num1 + num2
    clear()
    print(f"the result of {num1} + {num2} = {res}")
    paktc()


def Sub():
    clear()
    print("type the first number")
    num1 = number()
    print("type the second number")
    num2 = number()
    res = num1 - num2
    clear()
    print(f"the result of {num1} - {num2} = {res}")
    paktc()


def Multi():
    clear()
    print("type the first number")
    num1 = number()
    print("type the second number")
    num2 = number()
    res = num1 * num2
    clear()
    print(f"the result of {num1} * {num2} = {res}")
    paktc()


def Divi():
    clear()
    print("type the first number")
    num1 = number()
    print("type the second number")
    num2 = number()
    res = num1 / num2
    clear()
    print(f"the result of {num1} / {num2} = {res}")
    paktc()


def Power():
    clear()
    print("type the first number")
    num1 = number()
    print("type the second number")
    num2 = number()
    res = pow(num1, num2)
    clear()
    print(f"the result of {num1} to the power {num2} = {res}")
    paktc()


def Dirp():
    clear()
    print("type percentage you know")
    per1 = number()
    print(f"type the value at {per1}%")
    num1 = number()
    print("Do you know another V = value or P = percentage")
    cmd = readchar("#")
    if(cmd == "v"):
        print("type the value")
        num2 = number()
        per2 = (num2 * per1) / num1
    else:
        print("type the percentage")
        per2 = number()
        num2 = (num1 * per2) / per1

    snum1 = str(num1)
    snum2 = str(num2)
    snum1 = snum1.split(".")
    snum2 = snum2.split(".")
    NumPreDotSpace1 = len(snum2[0]) - len(snum1[0])
    NumPreDotSpace2 = len(snum1[0]) - len(snum2[0])
    NumAftDotSpace1 = len(snum2[1]) - len(snum1[1])
    NumAftDotSpace2 = len(snum1[1]) - len(snum2[1])

    per1 = str(per1) + "%"
    per2 = str(per2) + "%"
    sper1 = per1.split(".")
    sper2 = per2.split(".")
    PerPreDotSpace1 = len(sper2[0]) - len(sper1[0])
    PerPreDotSpace2 = len(sper1[0]) - len(sper2[0])
    PerAftDotSpace1 = len(sper2[1]) - len(sper1[1])
    PerAftDotSpace2 = len(sper1[1]) - len(sper2[1])

    clear()
    print(f"{spa(NumPreDotSpace1)}{num1}{spa(NumAftDotSpace1)}. . . .{spa(PerPreDotSpace1)}{per1}{spa(PerAftDotSpace1)}")
    print(f"{spa(NumPreDotSpace2)}{num2}{spa(NumAftDotSpace2)}. . . .{spa(PerPreDotSpace2)}{per2}{spa(PerAftDotSpace2)}")
    paktc()


def spa(s):
    space = ""
    if(s == 0):
        pass
    else:
        for i in range(0, s):
            space = space + " "
    return space


'''
def Root():

def Quadra():

def Factori():

def RealSize():
'''
