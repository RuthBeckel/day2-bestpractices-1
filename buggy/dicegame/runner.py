from .die import Die
from .utils import i_just_throw_an_exception

class GameRunner:

    def __init__(self):
        self.dice = Die.create_dice(5)

    def answer(self):
        total = 0
        for die in self.dice:
            total += die.value # add numbers on dice not number of dices
        return total
    

    @classmethod
    def run(cls):
        # Probably counts wins or something.
        # Great variable name, 10/10.
        wins = 0 # counter in main loop
        looses = 0 # counter in main loop
        n_round = 1 # counter in main loop
        while True:
            runner = cls()
            
            runner.round = n_round # actually unnecessary, just an ugly bug fix
            print("Round {}\n".format(runner.round))

            for die in runner.dice:
                print(die.show())

            guess = input("Sigh. What is your guess?: ")
            guess = int(guess)

            if guess == runner.answer():
                print("Congrats, you can add like a 5 year old...")
                wins +=1 # add to counter
                
            else:
                print("Sorry that's wrong")
                print("The answer is: {}".format(runner.answer()))
                print("Like seriously, how could you mess that up")
                looses += 1 # add to counter
                
            runner.wins = wins # actually unnecessary, just an ugly bug fix
            runner.loses = looses # actually unnecessary, just an ugly bug fix
            print("Wins: {} Loses {}".format(runner.wins, runner.loses))
            
            if n_round == 3:
                if wins == n_round:
                    print("You won... Congrats...")
                    print("The fact it took you so long is pretty sad")
                elif wins > looses:
                    print("You should be able to do better than that.")
                    print("Go and practice. But not with me. Leave me alone!")
                else:
                    print("Serieously, you should go back to primary school.")
                break
            
            n_round += 1 # add to counter

            prompt = input("Would you like to play again?[Y/n]: ")

            if prompt in ['y','Y','']: 
                continue
            elif prompt in ['n','N']: 
                print('Thanks for finally leaving me alone!')
                break
            else:
                i_just_throw_an_exception()
