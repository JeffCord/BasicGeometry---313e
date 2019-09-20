#  File: Geom.py#  Description:#  Student Name: Jeffrey Cordes#  Student UT EID: jec4443#  Partner Name:#  Partner UT EID:#  Course Name: CS 313E#  Unique Number: 50210#  Date Created: Sept. 17, 2019#  Date Last Modified: Sept. 17, 2019import mathclass Point(object):    # constructor    # x and y are floats    def __init__(self, x=0, y=0):        self.x = x        self.y = y    # get distance    # other is a Point object    def dist(self, other):        return math.hypot(self.x - other.x, self.y - other.y)    # get a string representation of a Point object    # takes no arguments    # returns a string    def __str__(self):        return '(' + str(self.x) + ", " + str(self.y) + ")"    # test for equality    # other is a Point object    # returns a Boolean    def __eq__(self, other):        tol = 1.0e-8        return (abs(self.x - other.x) < tol) and (abs(self.y - other.y) < tol)class Circle(object):    # constructor    # x, y, and radius are floats    def __init__(self, radius=1, x=0, y=0):        self.radius = radius        self.center = Point(x, y)    # compute circumference    def circumference(self):        return 2.0 * math.pi * float(self.radius)    # compute area    def area(self):        return math.pi * float(self.radius) * float(self.radius)    # determine if point is strictly inside circle    def point_inside(self, p):        return (self.center.dist(p) < self.radius)    # determine if a circle is strictly inside this circle    def circle_inside(self, c):        return (self.center.dist(c.center) + c.radius) < self.radius    # determine if a circle c overlaps this circle (non-zero area of overlap)    # but neither is completely inside the other    # the only argument c is a Circle object    # returns a boolean    def circle_overlap(self, c):        return self.center.dist(c.center) < (self.radius + c.radius)    # determine the smallest circle that circumscribes a rectangle    # the circle goes through all the vertices of the rectangle    # the only argument, r, is a rectangle object    def circle_circumscribe(self, r):        # TODO check        double_radius = r.ul.dist(r.lr)        radius = double_radius / 2        circle_center_x = r.ul.x + (r.width() / 2)        circle_center_y = r.ul.y - (r.length() / 2)        return Circle(radius, circle_center_x, circle_center_y)    # string representation of a circle    # takes no arguments and returns a string    def __str__(self):        return "Radius: " + str(self.radius) + ", Center: " + str(self.center)    # test for equality of radius    # the only argument, other, is a circle    # returns a boolean    def __eq__(self, other):        tol = 1.0e-8        return ((abs(self.radius - other.radius) < tol))class Rectangle(object):    # constructor    def __init__(self, ul_x=0, ul_y=1, lr_x=1, lr_y=0):        if (ul_x < lr_x) and (ul_y > lr_y):            self.ul = Point(ul_x, ul_y)            self.lr = Point(lr_x, lr_y)        else:            self.ul = Point(0, 1)            self.lr = Point(1, 0)    # determine length of Rectangle (distance along the x axis)    # takes no arguments, returns a float    def length(self):        return abs(self.lr.x - self.ul.x)    # determine width of Rectangle (distance along the y axis)    # takes no arguments, returns a float    def width(self):        return abs(self.ul.y - self.lr.y)    # determine the perimeter    # takes no arguments, returns a float    def perimeter(self):        return (2 * self.length()) + (2 * self.width())    # determine the area    # takes no arguments, returns a float    def area(self):        return self.length() * self.width()    # determine if a point is strictly inside the Rectangle    # takes a point object p as an argument, returns a boolean    def point_inside(self, p):        return (self.ul.x < p.x < self.lr.x) and (self.lr.y < p.y < self.ul.y)    # determine if another Rectangle is strictly inside this Rectangle    # takes a rectangle object r as an argument, returns a boolean    # should return False if self and r are equal    def rectangle_inside(self, r):        return (self.point_inside(r.ul) and self.point_inside(r.lr))    # determine if two Rectangles overlap (non-zero area of overlap)    # takes a rectangle object r as an argument returns a boolean    def rectangle_overlap(self, r):        if (self.ul.x > r.lr.x) or (self.lr.x < r.ul.x):            return False        if (r.lr.y > self.ul.y) or (r.ul.y < self.lr.y):            return False        else:            return True    # determine the smallest rectangle that circumscribes a circle    # sides of the rectangle are tangents to circle c    # takes a circle object c as input and returns a rectangle object    def rectangle_circumscribe(self, c):        ul_x = c.center.x - c.radius        ul_y = c.center.y + c.radius        lr_x = c.center.x + c.radius        lr_y = c.center.y - c.radius        return Rectangle(ul_x, ul_y, lr_x, lr_y)    # give string representation of a rectangle    # takes no arguments, returns a string    def __str__(self):        return "UL: " + str(self.ul) + ", LR: " + str(self.lr)    # determine if two rectangles have the same length and width    # takes a rectangle other as argument and returns a boolean    def __eq__(self, other):        tol = 1.0e-8        return (abs(self.length() - other.length())) < tol and (abs(self.width() - other.width()) < tol)# this program's main methoddef main():    f = open('geom.txt', 'r')# create Point objects P and Q    line_1 = f.readline().split()    line_2 = f.readline().split()    point_p = Point(float(line_1[0]), float(line_1[1]))    point_q = Point(float(line_2[0]), float(line_2[1]))# print the coordinates of the points P and Q    print('Coordinates of P:', point_p)    print('Coordinates of Q:', point_q)# find the distance between the points P and Q    dist_p_q = point_p.dist(point_q)    print('Distance between P and Q:', dist_p_q)# create two Circle objects C and D    line_3 = f.readline().split()    line_4 = f.readline().split()    circ_c = Circle(float(line_3[0]), float(line_3[1]), float(line_3[2]))    circ_d = Circle(float(line_4[0]), float(line_4[1]), float(line_4[2]))# print C and D    print('Circle C:', circ_c)    print('Circle D:', circ_d)# compute the circumference of C    print('Circumference of C:', circ_c.circumference())# compute the area of D    print('Area of D:', circ_d.area())# determine if P is strictly inside C    if circ_c.point_inside(point_p):        print("P is inside C")    else:        print("P is not inside C")# determine if C is strictly inside D    if circ_d.circle_inside(circ_c):        print("C is inside D")    else:        print("C is not inside D")# determine if C and D intersect (non zero area of intersection)    if circ_c.circle_overlap(circ_d):        print("C does intersect D")    else:        print("C does not intersect D")# determine if C and D are equal (have the same radius)    if circ_c.__eq__(circ_d):        print("C is equal to D")    else:        print("C is not equal to D")# create two rectangle objects G and H    line_5 = f.readline().split()    line_6 = f.readline().split()    rect_g = Rectangle(float(line_5[0]), float(line_5[1]), float(line_5[2]), float(line_5[3]))    rect_h = Rectangle(float(line_6[0]), float(line_6[1]), float(line_6[2]), float(line_6[3]))# print the two rectangles G and H    print("Rectangle G:", rect_g)    print("Rectangle H:", rect_h)# determine the length of G (distance along x axis)    length_g = rect_g.length()    print("Length of G:", length_g)# determine the width of H (distance along y axis)    width_h = rect_h.width()    print("Width of H:", width_h)# determine the perimeter of G    perimeter_g = rect_g.perimeter()    print("Perimeter of G:", perimeter_g)# determine the area of H    area_h = rect_h.area()    print("Area of H:", area_h)# determine if point P is strictly inside rectangle G    if rect_g.point_inside(point_p):        print("P is inside G")    else:        print("P is not inside G")# TODO determine if rectangle G is strictly inside rectangle H    if rect_h.rectangle_inside(rect_g):        print("G is inside H")    else:        print("G is not inside H")# TODO determine if rectangles G and H overlap (non-zero area of overlap)    if rect_g.rectangle_overlap(rect_h):        print("G does overlap H")    else:        print("G does not overlap H")# find the smallest circle that circumscribes rectangle G# goes through the four vertices of the rectangle    temp_circle = Circle()    circ_circumscribes_g = temp_circle.circle_circumscribe(rect_g)    print("Circle that circumscribes G:", circ_circumscribes_g)# find the smallest rectangle that circumscribes circle D# all four sides of the rectangle are tangents to the circle    temp_rectangle = Rectangle()    rect_circumscribes_d = temp_rectangle.rectangle_circumscribe(circ_d)    print("Rectangle that circumscribes D:", rect_circumscribes_d)# determine if the two rectangles have the same length and width    if rect_g.__eq__(rect_h):        print("Rectangle G is equal to H")    else:        print("Rectangle G is not equal to H")# close the file geom.txt    f.close()# This line above main is for grading purposes. It will not affect how# your code will run while you develop and test it.# DO NOT REMOVE THE LINE ABOVE MAINif __name__ == "__main__":    main()