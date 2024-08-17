#Linear_Regression.py
import numpy as np
np.set_printoptions(precision=2, suppress=True, floatmode='fixed')
# slope function
def get_y(m, x, b):
    return m*x + b

#function testing
#print(get_y(1, 0, 7) == 7)
#print(get_y(5, 10, 3) == 25)

# takes in m & b and an [x,y] point and returns the distance between the line and the point
def calculate_error(m, b, point):
    x_point = point[0]
    y_point = point[1]

    return abs(get_y(m, x_point, b) - y_point)

#testing data for calculate_error
# this is a line that looks like y = x, so (3, 3) should lie on it. thus, error should be 0:
#print(calculate_error(1, 0, (3, 3)))
# the point (3, 4) should be 1 unit away from the line y = x:
#print(calculate_error(1, 0, (3, 4)))
# the point (3, 3) should be 1 unit away from the line y = x - 1:
#print(calculate_error(1, -1, (3, 3)))

# the point (3, 3) should be 5 units away from the line y = -x + 1:
#print(calculate_error(-1, 1, (3, 3)))

def calculate_all_error(m, b, points):
    errors = 0
    for point in points:
        errors += calculate_error(m, b, point)
    return errors

datapoints = [(1, 1), (3, 3), (5, 5), (-1, -1)]
# every point in this dataset lies upon y=x, so the total error should be zero:
#p#rint(calculate_all_error(1, 0, datapoints))

# every point in this dataset is 1 unit away from y = x + 1, so the total error should be 4:
#print(calculate_all_error(1, 1, datapoints))

# every point in this dataset is 1 unit away from y = x - 1, so the total error should be 4:
#print(calculate_all_error(1, -1, datapoints))

# the points in this dataset are 1, 5, 9, and 3 units away from y = -x + 1, respectively, so total error should be
# 1 + 5 + 9 + 3 = 18
#print(calculate_all_error(-1, 1, datapoints))

possible_ms = np.arange(-10, 10+0.1, 0.1)
#print(possible_ms)
possible_bs = np.arange(-20, 20+0.1, 0.1)
print(possible_bs)