class Thing():
    def isBeatenByRock(self):
        return None
    def isBeatenByPaper(self):
        return None
    def isBeatenByScissors(self):
        return None
    def isBeatenByLizard(self):
        return None
    def isBeatenBySpock(self):
        return None

class Rock(Thing):
    def beats(self, opponent):
        """
        Rock is enveloped by Paper
        >>> Rock().beats(Paper())
        False

        Rock blunts Scissors
        >>> Rock().beats(Scissors())
        True

        Rock vs Rock is standoff
        >>> Rock().beats(Rock()) is None
        True

        Rock crushes Lizard
        >>> Rock().beats(Lizard())
        True

        Rock is vapourised by Spock
        >>> Rock().beats(Spock())
        False

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

    def isBeatenByLizard(self):
        return False

    def isBeatenBySpock(self):
        return True

class Paper(Thing):
    def beats(self, opponent):
        """
        Paper envelops Rock
        >>> Paper().beats(Rock())
        True

        Paper is cut by Scissors
        >>> Paper().beats(Scissors())
        False

        Paper vs Paper is standoff
        >>> Paper().beats(Paper()) is None
        True

        Paper is eaten by Lizard
        >>> Paper().beats(Lizard())
        False

        Paper disproves Spock
        >>> Paper().beats(Spock())
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

    def isBeatenByLizard(self):
        return True

    def isBeatenBySpock(self):
        return False

class Scissors(Thing):
    def beats(self, opponent):
        """
        Scissors cut Paper
        >>> Scissors().beats(Paper())
        True

        Scissors are blunted by Rock
        >>> Scissors().beats(Rock())
        False

        Scissors vs Scissors is standoff
        >>> Scissors().beats(Scissors()) is None
        True

        Scissors decapitate Lizard
        >>> Scissors().beats(Lizard())
        True

        Scissors are smashed by Spock
        >>> Scissors().beats(Spock())
        False

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

    def isBeatenByLizard(self):
        return False

    def isBeatenBySpock(self):
        return True


class Lizard(Thing):
    def beats(self, opponent):
        """
        Lizard is crushed by Rock
        >>> Lizard().beats(Rock())
        False

        Lizard eats Paper
        >>> Lizard().beats(Paper())
        True

        Lizard is decapitated by Scissors
        >>> Lizard().beats(Scissors())
        False

        Lizard vs Lizard is a standoff
        >>> Lizard().beats(Lizard()) is None
        True

        Lizard poisons Spock
        >>> Lizard().beats(Spock())
        True

        Lizard vs Thing is an invalid game
        >>> Lizard().beats(Thing()) is None
        True
        """
        return opponent.isBeatenByLizard()

    def isBeatenByRock(self):
        return True

    def isBeatenByPaper(self):
        return False

    def isBeatenByScissors(self):
        return True

    def isBeatenByLizard(self):
        return None

    def isBeatenBySpock(self):
        return False

class Spock(Thing):
    def beats(self, opponent):
        """
        Spock vapourises Rock
        >>> Spock().beats(Rock())
        True

        Spock is disproved by Paper
        >>> Spock().beats(Paper())
        False

        Spock smashes Scissors
        >>> Spock().beats(Scissors())
        True

        Spock is poisoned by Lizard
        >>> Spock().beats(Lizard())
        False

        Spock vs. Spock is a standoff
        >>> Spock().beats(Spock()) is None
        True

        Spock vs. Thing is an invalid game
        >>> Spock().beats(Thing()) is None
        True
        """
        return opponent.isBeatenBySpock()

    def isBeatenByRock(self):
        return False

    def isBeatenByPaper(self):
        return True

    def isBeatenByScissors(self):
        return False

    def isBeatenByLizard(self):
        return True

    def isBeatenBySpock(self):
        return None


if __name__ == "__main__":
    import doctest
    doctest.testmod()
