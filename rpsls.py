import random

def main():
    #make a class to define a player & play objects
    class player:
        def __init__(self):
            self.moves=[0,1,2]
                      #[r,p,s,l,s]
            self.wingame=0 #--> count how many player won
            
            #make a matrix of win & lose graph
            self.win_matrix=[[0,1],[1,2],[2,0]]

        def win(self):
            self.wingame += 1
        def play(self):
            return random.choice(self.moves)


    class rpsls_player(player):
        def __init__(self):
            player.__init__(self)
            
            #make a matrix of win & lose graph
            self.win_matrix=[[0, 1], [0, 3], [1, 2], [1, 4], [2, 3]
                            , [2, 0], [3, 4], [3, 1], [4, 0], [4, 2]]



    def game(a,b):
        p=[a.play(),b.play()]
        if p[0]==p[1]:
            pass 
        elif p in win:
            a.win()
        else:
            b.win()


#normal game
    a=player()
    b=player()
    while True:
        if (a.wingame == 100) or (b.wingame == 100):
            break
        game(a,b)
    print("normal game:\na wins: {}\nb wins: {}".format(a.wingame,b.wingame))

    print("\n\n")


#rpsls game
    a2=rpsls_player()
    b2=rpsls_player()
    while True:
        if (a2.wingame == 100) or (b2.wingame == 100):
            break
        game(a2,b2)
    print("rpsls game:\na2 wins: {}\nb2 wins: {}".format(a2.wingame,b2.wingame))

if __name__=='__main__':
    main()
