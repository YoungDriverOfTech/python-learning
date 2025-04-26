try:
    result = 1 / 0
except ZeroDivisionError:
    print("division by zero error happened")
except:
    print("catch other errors")
