class Patron (object):

    BOOKLIMIT = 3
    
    def __init__ (self, name):
        #Sets the number of books to 0 for each patron. Also, sets the name function as name for later use
        """Constructor"""
        self._name = name
        self._numBooks = 0

    def __str__ (self):
        #Shows the name of the patron and how many books that patron has checked out
        text = self._name + " has checked out " + \
               str(self._numBooks) + " books"
        return text

    def getName (self):
        #Returns the name of the patron
        return self._name

    def getNumBooks (self):
        #Returns the number 
        return self._numBooks

    def incBooks (self):
        #Increments the number of books that the patron now has
        if self._numBooks < Patron.BOOKLIMIT:
            self._numBooks += 1
        else:
            return 'Patron has reached his/her book limit'

    def decBooks (self):
        #Decrements the number of books that the patron now has
        if self._numBooks <= 0:
            return 'Patron has no books checked out'
        else:
            self._numBooks -= 1
