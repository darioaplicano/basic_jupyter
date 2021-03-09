## This class is the example of the class structure
class Class_Example:

    def __init__(self):
        """This is the constructor of the example class.
        
        """

        ## Any variable or method that contains "self" will be global in the class.
        self.r = 0
        self.s = 0


    def first_method(self, a, b):
        """ All methods of a class must always receive "self" as an attribute.
        
        """

        self.s = a + b
        self.r = a - b
        
        ## Methods may or may not return results
        return [a, b]
    

    def second_method(self):
        
        ## We see the values of r and s
        print(f"Previosly, r={self.r}, s={self.s}")
        a, b = self.first_method(3, 5) # To call a method you must use the term "self"

        ## Now we will see the value of the variables with the new change
        print(f"Now, r={self.r}, s={self.s}")
        