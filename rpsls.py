#! usr/bin/python3

import random

def main():
#______________________________________________________________________
    #make a class to define a player & play objects
    class Player:

        def __init__(self):
            self.moves = [0,1,2]
                        #[r,p,s]
            self.wingame = 0 #--> count how many player won
            
            #make a matrix of win & lose graph
            self.win_matrix = [[0,1],[1,2],[2,0]]        

        def win(self):
            self.wingame += 1

        def play(self):
            return random.choice(self.moves)

#_________________________________________________
    class Rpsls_Player(Player):
        def __init__(self):
            Player.__init__(self)
            
            #make a matrix of win & lose graph
            self.win_matrix = [[0, 1], [0, 3], [1, 2], [1, 4], [2, 3]
                            , [2, 0], [3, 4], [3, 1], [4, 0], [4, 2]]
                     #[0,1,2,3,4,] mean --> [Rock, Paper, Scissors, Lizard, Spock]
                     #[i,j] mean <i> win <j>

#_____________________________________________________________________


    def game(a,b):
        p = [a.play(),b.play()]
        if p[0] == p[1]:
            pass 

        elif p in a.win_matrix:
            a.win()

        else:
            b.win()


#__________________________________________________________________

    #normal game
    a = Player()
    b = Player()

    while True:
        if (a.wingame == 100) or (b.wingame == 100):
            break
        game(a,b)
    print("normal game:\na wins: {}\nb wins: {}\n\n".format(a.wingame,b.wingame))

#_____________________________________________
    #rpsls game
    a2=Rpsls_Player()
    b2=Rpsls_Player()
    
    while True:
        if (a2.wingame == 100) or (b2.wingame == 100):
            break

        game(a2,b2)
    print("rpsls game:\na2 wins: {}\nb2 wins: {}".format(a2.wingame,b2.wingame))



if __name__=='__main__':
    main()
