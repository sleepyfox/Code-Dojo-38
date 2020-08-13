class Thing():
    def isBeatenByRock(self):
        return None
    def isBeatenByPaper(self):
        return None
    def isBeatenByScissors(self):
        return None

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
        return opponent.isBeatenByRock()

    def isBeatenByRock(self):
        return None

    def isBeatenByPaper(self):
        return True

    def isBeatenByScissors(self):
        return False

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
        return opponent.isBeatenByPaper()

    def isBeatenByRock(self):
        return False

    def isBeatenByPaper(self):
        return None

    def isBeatenByScissors(self):
        return True

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
        return opponent.isBeatenByScissors()

    def isBeatenByRock(self):
        return True

    def isBeatenByPaper(self):
        return False

    def isBeatenByScissors(self):
        return None


if __name__ == "__main__":
    import doctest
    doctest.testmod()
