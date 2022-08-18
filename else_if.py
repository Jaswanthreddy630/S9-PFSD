class Sol:
    def elseid(self,x):
        if x<0:
            print("Negative number")
        elif x>0 & x<10:
            print("Num ranges between 1-9")
        else :
            print("NUM GREATER THAN 9")
x=Sol()
x.elseid(int(input()))