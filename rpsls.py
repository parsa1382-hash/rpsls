import random

def main():
    win=[]

    #make a matrix of win & lose graph
    for i in range(5):
        win.append([i,(i+1)%5])
        win.append([i,(i+3)%5])
        # [i,j] mean <i> win <j>

        
    #make a class to define a player & play objects
    class player:
        def __init__(self):
            self.moves=[0,1,2,3,4]
                      #[r,p,s,l,s]
            self.wingame=0 #--> count how many player won
        def win(self):
            self.wingame += 1
        def play(self):
            return random.choice(self.moves)
        
        
    def game(a,b):
        p=[a.play(),b.play()]
        if p[0]==p[1]:
            pass 
        elif p in win:
            a.win()
        else:
            b.win()
            
            
    #creat two player
    a=player()
    b=player()
    
    #make a game between they
    for i in range(100):
        game(a,b)
       
    print("a wins: {}\nb wins: {}".format(a.wingame,b.wingame))

if __name__=='__main__':
    main()
