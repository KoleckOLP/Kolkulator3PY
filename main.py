from call import Add, Sub, Multi, Divi, Power, Dirp, Debug
from kolreq.kolreq import clear, readchar

clear()

print("Kolkulator3PY by KoleckOLP, HorseArmored Inc.")

while(True):
    print("choose one by pressing it's letter\n\n" +
          "A. Addition\n" + 
          "S. Subtraction\n" +
          "M. Multiplication\n" +
          "D. Division\n" +
          "P. Power\n" +
          "R. Root (unimplemented)\n" +
          "Q. Quadratic Equasion (unimplemented)\n" +
          "F. Factorial (unimplemented)\n" +
          "H. Real HDD/Flash space (unimplemented)\n" +
          "N. Direct Proportionality\n" +
          "Q. quit")
    
    cmd = readchar("#")
    if(cmd == "a"): #addition
        Add()
    elif(cmd == "s"):
        Sub()
    elif(cmd == "m"):
        Multi()
    elif(cmd == "d"):
        Divi()
    elif(cmd == "p"):
        Power()
    elif(cmd == "n"):
        Dirp()
    elif(cmd == "q"): #quit
        print("See you later aligator.")
        break 
    elif(cmd == "`"): #debug
        Debug()
    else:
        clear()
        print(f"\"{cmd}\" is not an option.")
