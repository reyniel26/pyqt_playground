"""Sierpinski Triangle"""
import itertools
import math
import random

SIN60 = math.sin(math.pi/3)

class SierpinskiTriangle():
    """Sierpinski Triangle Class"""

    def __init__(self):
        """Initialize Sierpinski Triangle"""
        self.base_x = 0
        self.base_y = 0
        self.range = 2
        self._vertices = [
            (self.base_x, self.base_y),
            (self.base_x+(self.range/2), self.base_y+(SIN60*self.range)),
            (self.base_x+self.range, self.base_y)
            ]

        self._points = []

    def get_random_vertex(self)->tuple:
        """Return random vertex"""
        return self._vertices[random.randint(0,2)]

    def get_random_point(self):
        """Return random coordinates of point"""
        return (random.randint(0, self.range), random.randint(0, self.range))

    def get_valid_random_point(self):
        """Return random point that is inside of the triangle"""
        point = self.get_random_point()
        while not self.is_inside_triangle(point,self._vertices):
            point = self.get_random_point()
        return point

    def get_angle(self,triangle):
        """Get angle based on provided triangle"""
        point_a,point_b,point_c = triangle
        return self.get_angle_by_points(point_a,point_b,point_c)

    def get_angle_by_points(self,point_a,point_b,point_c):
        """Get angle based on provided points"""
        ang = math.degrees(
            math.atan2(point_c[1]-point_b[1], point_c[0]-point_b[0])
            - math.atan2(point_a[1]-point_b[1], point_a[0]-point_b[0])
            )
        return ang + 360 if ang < 0 else round(ang,3)

    def is_60_angle(self,triangle):
        """Return boolean if the angle is 60"""
        return 60 == self.get_angle(triangle)

    def get_area_triangle(self,a, b, c):
        """Get Area of Triangle"""
        ab = (b[0]-a[0],b[1]-a[1])
        ac = (c[0]-a[0],c[1]-a[1])
        cross_prod = (ab[0] * ac[1])-(ab[1] * ac[0])
        return abs(cross_prod)/2

    def is_inside_triangle(self,point,triangle):
        """Return boolean if the point is inside of the triangle"""
        a,b,c = triangle

        triangle_area = self.get_area_triangle(a,b,c)

        area_sum = 0
        for x in itertools.combinations({a,b,c}, 2):
            area_sum = area_sum + self.get_area_triangle(x[0],x[1],point)

        return triangle_area == area_sum

    def get_midway_point(self,point_a,point_b):
        """Return the midway of the two points"""
        return (
            (point_a[0]+point_b[0])/2,
            (point_a[1]+point_b[1])/2
            )

    def generate_triangle(self):
        """Generate Triangle vertices"""
        self._vertices = [
            (self.base_x, self.base_y),
            (self.base_x+(self.range/2), self.base_y+(SIN60*self.range)),
            (self.base_x+self.range, self.base_y)
            ]

    def generate_valid_triangle(self):
        """Generate Valid Triangle vertices"""
        self.generate_triangle()
        while not self.is_60_angle(self._vertices):
            self.generate_triangle()

    def run_chaos_game(self,starting_point,steps):
        """

        # The Chaos Game

        - The algorithm used to create sierpinski triangle
        1. Take three points in a plane to form a triangle.
        2. Randomly select any point inside the triangle and consider that your current position.
        3. Randomly select any one of the three vertex points.
        4. Move half the distance from your current position to the selected vertex.
        5. Plot the current position.
        6. Repeat from step 3.

        """

        point = starting_point
        for x in range(steps):
            point = self.get_midway_point(point,self.get_random_vertex())
            self._points.append(point)

    def get_vertices(self):
        """Get Vertices"""
        return self._vertices

    def get_points(self):
        """Get Points"""
        return self._points