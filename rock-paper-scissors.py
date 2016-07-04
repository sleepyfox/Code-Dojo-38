class Thing():
    pass

class Rock(Thing):
    def beats(self, opponent):
        """Rock is enveloped by Paper
        >>> Rock().beats(Paper())
        False
        
        Rock blunts Scissors
        >>> Rock().beats(Scissors())
        True

        Rock vs Rock is standoff
        >>> Rock().beats(Rock()) is None
        True

        Rock vs. Thing is a invalid game
        >>> Rock().beats(Thing()) is None
        True
        """
        if isinstance(opponent, Rock):
            return None
        elif isinstance(opponent, Scissors):
            return True
        elif isinstance(opponent, Paper):
            return False
        else:
            return None


class Paper(Thing):
    def beats(self, opponent):
        """Paper envelops Rock
        >>> Paper().beats(Rock())
        True
        
        Paper is cut by Scissors
        >>> Paper().beats(Scissors())
        False

        Paper vs Paper is standoff
        >>> Paper().beats(Paper()) is None
        True

        Paper vs. Thing is a invalid game
        >>> Paper().beats(Paper()) is None
        True
        """
        if isinstance(opponent, Rock):
            return True
        elif isinstance(opponent, Scissors):
            return False
        elif isinstance(opponent, Paper):
            return None
        else:
            return None
        
    
class Scissors(Thing):
    def beats(self, opponent):
        """Scissors cut Paper
        >>> Scissors().beats(Paper())
        True
        
        Scissors are blunted by Rock
        >>> Scissors().beats(Rock())
        False

        Scissors vs Scissors is standoff
        >>> Scissors().beats(Scissors()) is None
        True

        Scissors vs. Thing is a invalid game
        >>> Scissors().beats(Thing()) is None
        True
        """
        if isinstance(opponent, Rock):
            return False
        elif isinstance(opponent, Scissors):
            return None
        elif isinstance(opponent, Paper):
            return True
        else:
            return None

        
if __name__ == "__main__":
    import doctest
    doctest.testmod()
