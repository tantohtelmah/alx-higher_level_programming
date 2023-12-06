#!/usr/bin/python3
""" initialisation"""


class PascalTriangle:
    """Defines a Pascal's triangle by its number of rows."""
    
    def __init__(self, n):
        """Instantiates a PascalTriangle object with n rows."""
        
        self.n = n

    def __iter__(self):
        """Returns an iterator for the 
        PascalTriangle object.
        """
        
        self.current_row = 0
        self.current_col = 0
        self.current_value = 1
        self.current_row_list = [1]
        return self

    def __next__(self):
        """Returns the next value in the 
        PascalTriangle object.
        """
        
        if self.current_row == self.n:
            raise StopIteration
        elif self.current_col == self.current_row:
            self.current_row += 1
            self.current_col = 0
            self.current_value = 1
            self.current_row_list.append(1)
            return self.current_row_list
        else:
            self.current_value = self.current_value * (self.current_row - self.current_col) // (self.current_col + 1)
            self.current_col += 1
            self.current_row_list.append(self.current_value)
            return self.current_value

def pascal_triangle(n):
    """Returns a list of lists of integers representing the 
    Pascal’s triangle of n.
    """
    
    if n <= 0:
        return []
    else:
        pt = PascalTriangle(n)
        return list(pt)
