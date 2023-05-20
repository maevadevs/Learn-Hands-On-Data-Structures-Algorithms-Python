"""Define the features of a 2D Point."""

# Import modules
from math import sqrt


# Define Class
class Point:
    """Represent a 2D Point object."""

    # The methods are defined here in the body one after the other
    def __init__(self, x: float = 0, y: float = 0) -> None:
        """The instance constructor of the Point class.

        Args:
            - `x` (`float`, optional): The value of the X-Coordinate. Defaults to 0.
            - `y` (`float`, optional): The value of the Y-Coordinate. Defaults to 0.
        """
        self.x_coord: float = x
        self.y_coord: float = y

    def __str__(self) -> str:
        """Returns the string representation of the Point.

        Returns:
            - `str`: The string representation of the Point.
        """
        return f"Point({self.x_coord}, {self.y_coord})"

    def summary(self) -> str:
        """Prints a summary about the point instance.

        Returns:
            - `str`: The summary about the point.

        It just calls and returns str(point).
        """
        return str(self)

    def get_x(self) -> float:
        """Return the value on the X-axis.

        Returns:
            - `float`: The X-coordinate of the point.
        """
        return self.x_coord

    def get_y(self) -> float:
        """Return the value on the Y-axis.

        Returns:
            - `float`: The Y-coordinate of the point.
        """
        return self.y_coord

    def shift(self, x_inc: float = 0, y_inc: float = 0) -> None:
        """Adjust or shift the value on the X-Coordinate or the Y-coordinate.

        Args:
            - `x_inc` (`float`, optional): Value to shift the X-coordinate by. Defaults to 0.
            - `y_inc` (`float`, optional): Value to shift the Y-coordinate by. Defaults to 0.
        """
        self.x_coord += x_inc
        self.y_coord += y_inc

    def distance(self, other_pt: "Point") -> float:
        """Calculate the Eucludian distance (shortest distance) between 2 points.

        Args:
            - `other_pt` (`Point`): The other distant point.

        Returns:
            - `float`: The lenght of the distance between the points.
        """
        x_diff: float = self.x_coord - other_pt.x_coord
        y_diff: float = self.y_coord - other_pt.y_coord
        return sqrt(x_diff**2 + y_diff**2)

    def echo(self) -> str:
        """Return a string representation of the Point object

        Returns:
            - `str`: A string representation of the Point object
        """
        return f"A point object: ({self.x_coord}, {self.y_coord})"
