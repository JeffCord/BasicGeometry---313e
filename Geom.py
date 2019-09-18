import math


class Point(object):
    # constructor
    # x and y are floats
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    # get distance
    # other is a Point object
    def dist(self, other):
        return math.hypot(self.x - other.x, self.y - other.y)

    # get a string representation of a Point object
    # takes no arguments
    # returns a string
    def __str__(self):
        return '(' + str(self.x) + ", " + str(self.y) + ")"

    # test for equality
    # other is a Point object
    # returns a Boolean
    def __eq__(self, other):
        tol = 1.0e-8
        return ((abs(self.x - other.x) < tol) and (abs(self.y - other.y) < tol))


class Circle(object):
    # constructor
    # x, y, and radius are floats
    def __init__(self, radius=1, x=0, y=0):
        self.radius = radius
        self.center = Point(x, y)

    # compute cirumference
    def circumference(self):
        return 2.0 * math.pi * self.radius

    # compute area
    def area(self):
        return math.pi * self.radius * self.radius

    # determine if point is strictly inside circle
    def point_inside(self, p):
        return (self.center.dist(p) < self.radius)

    # determine if a circle is strictly inside this circle
    def circle_inside(self, c):
        distance = self.center.dist(c.center)
        return (distance + c.radius) < self.radius

    # determine if a circle c overlaps this circle (non-zero area of overlap)
    # but neither is completely inside the other
    # the only argument c is a Circle object
    # returns a boolean
    def circle_overlap(self, c):
        return self.center.dist(c.center) < self.radius + c.radius

    # determine the smallest circle that circumscribes a rectangle
    # the circle goes through all the vertices of the rectangle
    # the only argument, r, is a rectangle object
    def circle_circumscribe(self, r):
        radius_squared = (r.length() / 2) + (r.width() / 2)
        new_radius =  math.sqrt(radius_squared)
        # TODO add return statement (return a circle)

    # string representation of a circle
    # takes no arguments and returns a string
    def __str__(self):
        return "Radius: " + str(self.radius) + ", Center: " + str(self.center)

    # test for equality of radius
    # the only argument, other, is a circle
    # returns a boolean
    def __eq__(self, other):
        tol = 1.0e-8
        # TODO check
        return self.radius == other.radius


class Rectangle(object):
    # constructor
    def __init__(self, ul_x=0, ul_y=1, lr_x=1, lr_y=0):
        if ((ul_x < lr_x) and (ul_y > lr_y)):
            self.ul = Point(ul_x, ul_y)
            self.lr = Point(lr_x, lr_y)
        else:
            self.ul = Point(0, 1)
            self.lr = Point(1, 0)

    # determine length of Rectangle (distance along the x axis)
    # takes no arguments, returns a float
    def length(self):
        # TODO check
        return abs(self.ul.y - self.lr.y)

    # determine width of Rectangle (distance along the y axis)
    # takes no arguments, returns a float
    def width(self):
        # TODO check
        return abs(self.lr.x - self.ul.x)

    # determine the perimeter
    # takes no arguments, returns a float
    def perimeter(self):
        return (2 * self.length()) + (2 * self.width())

    # determine the area
    # takes no arguments, returns a float
    def area(self):
        return self.length() * self.width()

    # determine if a point is strictly inside the Rectangle
    # takes a point object p as an argument, returns a boolean
    def point_inside(self, p):
        return (self.ul.x < p.x < self.lr.x) and (self.lr.y < p.y < self.ul.y)

    # determine if another Rectangle is strictly inside this Rectangle
    # takes a rectangle object r as an argument, returns a boolean
    # should return False if self and r are equal
    def rectangle_inside(self, r):
        # TODO
        print()

    # determine if two Rectangles overlap (non-zero area of overlap)
    # takes a rectangle object r as an argument returns a boolean
    def rectangle_overlap(self, r):
        # TODO
        print()

    # determine the smallest rectangle that circumscribes a circle
    # sides of the rectangle are tangents to circle c
    # takes a circle object c as input and returns a rectangle object
    def rectangle_circumscribe(self, c):
        # TODO
        print()

    # give string representation of a rectangle
    # takes no arguments, returns a string
    def __str__(self):
        return "UL: " + str(self.ul) + ", LR: " + str(self.lr)

    # determine if two rectangles have the same length and width
    # takes a rectangle other as argument and returns a boolean
    def __eq__(self, other):
        return self.length() == other.length() and self.width() == other.width()


def main():
    f = open('geom.txt', 'r')

# create Point objects P and Q
    line_1 = f.readline().split()
    line_2 = f.readline().split()

    point_p = Point(line_1[0], line_1[1])
    point_q = Point(line_2[0], line_2[1])

# print the coordinates of the points P and Q
    print('Coordinates of P:', point_p)
    print('Coordinates of Q:', point_q)

# find the distance between the points P and Q
#     dist_p_q = point_q.dist(point_p)
#
#     print('Distance between P and Q:', dist_p_q)

# create two Circle objects C and D

# print C and D

# compute the circumference of C

# compute the area of D

# determine if P is strictly inside C

# determine if C is strictly inside D

# determine if C and D intersect (non zero area of intersection)

# determine if C and D are equal (have the same radius)

# create two rectangle objects G and H

# print the two rectangles G and H

# determine the length of G (distance along x axis)

# determine the width of H (distance along y axis)

# determine the perimeter of G

# determine the area of H

# determine if point P is strictly inside rectangle G

# determine if rectangle G is strictly inside rectangle H

# determine if rectangles G and H overlap (non-zero area of overlap)

# find the smallest circle that circumscribes rectangle G
# goes through the four vertices of the rectangle

# find the smallest rectangle that circumscribes circle D
# all four sides of the rectangle are tangents to the circle

# determine if the two rectangles have the same length and width

# close the file geom.txt

# This line above main is for grading purposes. It will not affect how
# your code will run while you develop and test it.
# DO NOT REMOVE THE LINE ABOVE MAIN
if __name__ == "__main__":
    main()