#Triangle or Not Homework 2
def triangle(check):
    if (abs(check[0] + check[1]) > check[2] and abs(check[0] + check[2]) > check[1] and abs(check[1] + check[2]) > check[0]):
        return True
    else:
        return False
check_list = [(3,4,5),(6,8,10),(3,10,7)]
print(list(filter(triangle,check_list)))