# Code Dojo 38
This is my worked example from the 38th meeting of the London Code Dojo. Feel free to play around with it. 

The tests can be run from the command-line with:

	python -m doctest rock-paper-scissors.py

The source of the kata is the ancient game of Rock-Paper-Scissors, or 'Roshambo', which originated in ancient China as 'shoushili' and then was exported to Japan as 'sansukimi-ken' and later 'kitsune-ken': a variation which uses both hands. More can be found of its history [here](https://en.wikipedia.org/wiki/Rock-paper-scissors#History).
You can find out more about the London Code Dojo at our [homepage](http://www.meetup.com/London-Code-Dojo/).

## Kata: Rock-Paper-Scissors
Two players make signs using one hand simultaneously - usually on calling 'three, two, one, go!'
The signs can be:
* Rock - represented by a closed fist
* Paper - represented by the hand held open
* Scissors - represented by the first and second fingers being held apart in a 'V' to show the open blades of the scissors

The match is decided based upon the simple rules:
* Two of the same sign results in a draw
* Rock blunts Scissors (Rock wins)
* Scissors cuts Paper (Scissors wins)
* Paper envelops Rock (Paper wins)

The constraints are as follows:
The all-powerful project Architect has declared that the team must use OOP, and has decided on the following design:
* The program will have three classes: 'Rock', 'Paper' and 'Scissors'
* All classes will inherit from a superclass of 'Thing'
* All classes will have a method 'beats' that takes an object of type 'Thing' or of one of its subclasses, and returns True, False or None if the instance beats the thing passed in 

Example: (Python syntax)
* Rock().beats(Paper()) would return False
* Rock().beats(Rock()) would return None

## Object Calisthenics
For the second pomodoro an additional set of constraints is put into play: No conditionals. This means no 'if' statements, no switch, no ternary operator etc.

## The Lizard-Spock expansion
For the third pomodoro an additional requirement is brought into play: we add the 'Lizard' and 'Spock' gestures. This works as follows:
	"It's very simple. Scissors cuts paper. Paper covers rock. Rock crushes lizard. Lizard poisons Spock. Spock smashes scissors. Scissors decapitates lizard. Lizard eats paper. Paper disproves Spock. Spock vaporizes rock. And as it always has, rock crushes scissors."
![Lizard-Spock Expansion](https://upload.wikimedia.org/wikipedia/commons/thumb/a/ad/Pierre_ciseaux_feuille_l%C3%A9zard_spock_aligned.svg/768px-Pierre_ciseaux_feuille_l%C3%A9zard_spock_aligned.svg.png "Rock-Paper-Scissors-Lizard-Spock")

# License
The code samples are licensed under the CC-SA-NC-4.0 license, as shown in the [LICENSE](/LICENSE) file.
