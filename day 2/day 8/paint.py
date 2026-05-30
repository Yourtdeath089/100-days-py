height=int(input("what is the height of the wall??\n"))
width=int(input("what is the width of the wall??\n"))
coverage=int(input("what is the mentioned coverage on the can??\n"))
def calculate(h,w,c):
    cove=h*w/c
    rcover=round(cove)
    print(f"the number of cans you need is {rcover}")
calculate(height,width,coverage)

