#Calculate Area of Rectangle Homework 1
def calculate_area_of_rectangle(area):
    return area[0] * area[1]

check_list = [(3,4),(10,3),(5,6),(1,9)]

result = list(map(calculate_area_of_rectangle,check_list))

print(result)