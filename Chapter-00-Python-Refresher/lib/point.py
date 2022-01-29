from math import sqrt


class Point:
    # The methods are defined here in the body one after the other
    
    def __init__(self, x = 0, y = 0):
        """The constructor of instances for the Point class."""
        self.x_coord = x
        self.y_coord = y
    
    
    def summary(self):
        """Prints a summary about the point instance."""
        return "Point({x}, {y})".format(x = self.x_coord, y = self.y_coord)
    
    
    def get_x(self):
        """Return the value on the X-axis"""
        return self.x_coord
    
    
    def get_y(self):
        """Return the value on the Y-axis"""
        return self.y_coord
    
    
    def shift(self, x_inc = 0, y_inc = 0):
        """Adjust or shift the value on the X-Coordinate or the Y-coordinate"""
        self.x_coord += x_inc
        self.y_coord += y_inc

        
    def distance(self, other_pt):
        """Calculate the Eucludian distance (shortest distance) between 2 points"""
        x_diff = self.x_coord - other_pt.x_coord
        y_diff = self.y_coord - other_pt.y_coord
        return sqrt(x_diff ** 2 + y_diff ** 2)
    
    
    def echo(self):
        """Return a string representation of the Point object"""
        return "A point object: ({}, {})".format(self.x_coord, self.y_coord)