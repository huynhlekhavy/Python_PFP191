#〖S=1-2〗^2+3^2-…+ n^2
# xen ke + -

def tinhSum(num):
    sum = 0
    for i in range(1, num+1):
        # if(i % 2 == 0):
        #     sum -= i**2
        # else:
        #     sum += i**2
        sum += ((-1)**(i+1))*(i**2)
    print(sum)
tinhSum(10)