
def prime_checker(n):
    d=0
    if n%2==0:
        print ("not a prime number")
    for i in range(2,n):
        if n%i==0:
            d+=1
        if i>=n-1 and d!=0:
            print("not a prime number")
    if d==0:
        print(f"{n} is a prime number")
ni=int(input("what number would you like to guess\n"))
prime_checker(ni)   