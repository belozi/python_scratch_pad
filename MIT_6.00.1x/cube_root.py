# The code in week 2 lectur e3 of the MITx 6.00.1x to find the cube root
# of a given number does not work due to syntax and symantic errors.
# Here is how I fixed it. :)

x = int(raw_input("Enter an integer: "))
for ans in range(0, abs(x)+1):
    if ans**3 ==abs(x):
        if x < 0:
            ans = -ans
        print('Cube root of ' + str(x) + ' is: '+ str(ans))
        break
    if abs(ans) == (abs(x)):
        print(str(x) + ' is not a perfect cube')
        continue
    
    
    
