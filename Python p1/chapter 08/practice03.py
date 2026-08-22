# convert temperatue from fehreinheit to celcius
def celcius(f):
    c = 5 * (f - 32) / 9
    return c


f = int(input("enter temperature in fehreinheit: "))
T_in_C = celcius(f)
print(f"{round(T_in_C,3)} degree celcius")
# round function will give the value 3 digits after "."
