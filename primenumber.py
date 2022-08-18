class pm:
    def prime(self):
        x=int(input())
        i=2
        sum=0
        while i<=x:
            if x%i==0:
                sum+=1
            i+=1
        if sum==1:
            print("Prime Number :")
        else :
            print("Not Prime Number :")
obj=pm()
obj.prime()