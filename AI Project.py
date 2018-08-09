"""
AI OTHELLO Project
Amanda Truong, Courtney Higgins, Anna Khachaturova

"""
import numpy as np
import random

#BLACK = 8, WHITE = 0
BLACK = 8
WHITE = 0
EMPTY = 1


#////////////////////////////main code////////////////////////////////////////////#
def findBestMove(color):
    currentboard,free = makeRandomBoard()
    print("Current score, (Black , White):")    
    print(scoreCounter(currentboard))
    print("\nPlayer: ")
    if(color == BLACK):
        print("BLACK : 8\n")
    else:print("WHITE : 0\n")
    
    print("Open Space coordinates")  
    print(free)

    #all sizes should be 3
    firstscores, firstmovetables, firstmovesremainders = allscores(currentboard,free,color)
    print("checking first move options:")
    for i in range(3):
        print("------------------------------")
        print(firstmovetables[i])
        print(firstscores[i])
        print(firstmovesremainders[i])
    print("------------------------------")    

    bestOpponents = []
    lastEmptySlot = []
  ####opponent's turn
    if(color == WHITE):
        
        #these should be two elements.  blackfree should only contain one element
        black1score, black1tables, black1free = allscores(firstmovetables[0],firstmovesremainders[0],BLACK)
        black2score, black2tables, black2free = allscores(firstmovetables[1],firstmovesremainders[1],BLACK)
        black3score, black3tables, black3free = allscores(firstmovetables[2],firstmovesremainders[2],BLACK)
        
        #best boards for black with all options
        bestOpponents.append(black1tables[maxscore(BLACK,black1score)])
        bestOpponents.append(black2tables[maxscore(BLACK,black2score)])
        bestOpponents.append(black3tables[maxscore(BLACK,black3score)])
        
        lastEmptySlot.append(black1free[maxscore(BLACK,black1score)])
        lastEmptySlot.append(black2free[maxscore(BLACK,black2score)])
        lastEmptySlot.append(black3free[maxscore(BLACK,black3score)])
        
    else: #color == BLACK
        
        white1score, white1tables, white1free = allscores(firstmovetables[0],firstmovesremainders[0],WHITE)
        white2score, white2tables, white2free = allscores(firstmovetables[1],firstmovesremainders[0],WHITE)
        white3score, white3tables, white3free = allscores(firstmovetables[2],firstmovesremainders[0],WHITE)
        
        #best boards for white with all options
        
        bestOpponents.append(white1tables[maxscore(WHITE,white1score)])
        bestOpponents.append(white2tables[maxscore(WHITE,white2score)])
        bestOpponents.append(white3tables[maxscore(WHITE,white3score)])
        
        lastEmptySlot.append(white1free[maxscore(WHITE,white1score)])
        lastEmptySlot.append(white2free[maxscore(WHITE,white2score)])
        lastEmptySlot.append(white3free[maxscore(WHITE,white3score)])
        
    print("Opponent's best turn:")    
    for i in range(3):
        print("------------------------------")
        print(bestOpponents[i])
        print(scoreCounter(bestOpponents[i]))
        print(lastEmptySlot[i])
    print("------------------------------")     
    
    #player's final turn
    
    finalscores = []
    finaltables = []
    
    final1score,finaltable1,blank = allscores(bestOpponents[0],lastEmptySlot[0],color) 
    final2score,finaltable2,blank = allscores(bestOpponents[1],lastEmptySlot[1],color) 
    final3score,finaltable3,blank = allscores(bestOpponents[2],lastEmptySlot[2],color) 
        
    finalscores.append(final1score[0])
    finalscores.append(final2score[0])
    finalscores.append(final3score[0])
    
    finaltables.append(finaltable1[0])
    finaltables.append(finaltable2[0])
    finaltables.append(finaltable3[0])

    print("Final Move!")
    for i in range(3):
        print("------------------------------")
        print(finaltables[i])
        print(finalscores[i])
    print("------------------------------") 
    
    index = maxscore(color,finalscores)
    bestpoint = free[index]
    bestscore = finalscores[index]
    print("best first moves is at:")
    print(bestpoint)
    print(currentboard)
    print("score:")
    print(bestscore)
    if(color == WHITE):
        if(bestscore[0]>bestscore[1]):
            print("Unfortunately it is still not enough to beat the opponent...")
        elif(bestscore[0]==bestscore[1]):
            print("This is enough to tie with the opponent.")
        else: print("Congratulations, you can win this way!!!")  
    else:    
        if(bestscore[1]>bestscore[0]):
            print("Unfortunately it is still not enough to beat the opponent...")
        elif(bestscore[1]==bestscore[0]):
            print("This is enough to tie with the opponent.")
        else: print("Congratulations, you can win this way!!!")  
    
# creates an array of the scores for the player of color       
def allscores(board, freespaces, color):
    scores = []
    newtables = []
    newspaces = []
    for t in range(len(freespaces)):
        newboard = board.copy()
        newfree = freespaces.copy()
        
        moves = (legalMove(freespaces[t][0],freespaces[t][1],newboard,color))
        bd = (flip(newboard,freespaces[t],moves,color))
        newtables.append(bd)
        scores.append(scoreCounter(bd))
        
        del newfree[t]
        
        newspaces.append(newfree)
    return scores, newtables, newspaces


#Check if the move is working
def legalMove(x,y,board, color):
    flipPoints = []
################################################################
    if(onBoard(x+1,y)) and (board[x+1,y] != color) and (board[x+1,y] != EMPTY):
        i = 2
        while(onBoard(x+i,y)):
            if(board[x+i,y] == EMPTY):
                break
            if(board[x+i,y] == color):
                flipPoints.append((x+i,y))
                #print((x+i,y))
                break
            i+=1
    if(onBoard(x-1,y)) and (board[x-1,y] != color) and (board[x-1,y] != EMPTY):
        i = 2
        while(onBoard(x-i,y)):
            if(board[x-i,y]==EMPTY):
                break
            if(board[x-i,y]==color):
                flipPoints.append((x-i,y))
                #print((x-i,y))
                break
            i+=1    
######################################################################
    if(onBoard(x,y+1)) and (board[x,y+1] != color) and (board[x,y+1] != EMPTY):
        i = 2
        while(onBoard(x,y+i)):
            if(board[x,y+i] == EMPTY):
                break
            if(board[x,y+i] == color):
                flipPoints.append((x,y+i))
                #print((x,y+i))
                break
            i+=1
    if(onBoard(x,y-1)) and (board[x,y-1] != color) and (board[x,y-1] != EMPTY):
        i = 2
        while(onBoard(x,y-i)):
            if(board[x,y-i]==EMPTY):
                break
            if(board[x,y-i]==color):
                flipPoints.append((x,y-i))
                #print((x,y-i))
                break
            i+=1    
##############################################################################################
    if(onBoard(x+1,y+1)) and (board[x+1,y+1] != color) and (board[x+1,y+1] != EMPTY):
        i = 2
        while(onBoard(x+i,y+i)):
            if(board[x+i,y+i] == EMPTY):
                break
            if(board[x+i,y+i] == color):
                flipPoints.append((x+i,y+i))
                #print((x+i,y+i))
                break
            i+=1
    if(onBoard(x-1,y-1)) and (board[x-1,y-1] != color) and (board[x-1,y-1] != EMPTY):
        i = 2
        while(onBoard(x-i,y-i)):
            if(board[x-i,y-i]==EMPTY):
                break
            if(board[x-i,y-i]==color):
                flipPoints.append((x-i,y-i))
                #print((x-i,y-i))
                break
            i+=1    
##############################################################################################
    if(onBoard(x-1,y+1)) and (board[x-1,y+1] != color) and (board[x-1,y+1] != EMPTY):
        i = 2
        while(onBoard(x-i,y+i)):
            if(board[x-i,y+i] == EMPTY):
                break
            if(board[x-i,y+i] == color):
                flipPoints.append((x-i,y+i))
                #print((x-i,y+i))
                break
            i+=1
    if(onBoard(x+1,y-1)) and (board[x+1,y-1] != color) and (board[x+1,y-1] != EMPTY):
        i = 2
        while(onBoard(x+i,y-i)):
            if(board[x+i,y-i]==EMPTY):
                break
            if(board[x+i,y-i]==color):
                flipPoints.append((x+i,y-i))
                #print((x+i,y-i))
                break
            i+=1
##############################################################################################           
    #outputs points        
    return flipPoints 
   
#Collects the score   
def scoreCounter(board):
    blackCount = 0
    whiteCount = 0
    for x in range(8):
        for y in range(8):
            if(board[x,y] == BLACK):
                blackCount+=1
            if(board[x,y] == WHITE):
                whiteCount+=1
    return blackCount,whiteCount                     
# create random board with three empty spaces     
def makeRandomBoard():
    board = np.random.choice([WHITE,BLACK],[8,8],True,p=[0.5,0.5])
    freespace = []
    for i in range(3):
        x = 4
        y = 4
        while(x == 4 and y == 4) or (x == 4 and y == 5) or (x == 5 and y == 4) or (x == 5 and y == 5):
            x = random.randint(0,7)
            y = random.randint(0,7)        
        board[x,y] = EMPTY
        freespace.append((x,y))
    print(board)
    return board, freespace

#flip pieces of new space
def flip(board, freespace,flipPoints,color):
    newBoard = board
    x=freespace[0]
    y=freespace[1]
    for i in flipPoints:
        # x related
        if(x < i[0] and y == i[1]):     
            for j in range(i[0]-x):
                newBoard[x+j,y] = color
        if(x > i[0] and y == i[1]):     
            for j in range(x-i[0]):
                newBoard[x-j,y] = color    
        # y related
        if(y < i[1] and x == i[0]):     
            for j in range(i[1]-y):
                newBoard[x,y+j] = color
        if(y > i[1] and x == i[0]):     
            for j in range(y-i[1]):
                newBoard[x,y-j] = color
        # slope 1 related 
        if(y < i[1] and x < i[0]):     
            for j in range(i[1]-y):
                newBoard[x+j,y+j] = color
        if(y > i[1] and x > i[0]):     
            for j in range(y-i[1]):
                newBoard[x-j,y-j] = color 
        # slope -1 related
        if(y < i[1] and x > i[0]):     
            for j in range(i[1]-y):
                newBoard[x-j,y+j] = color
        if(y > i[1] and x < i[0]):     
            for j in range(y-i[1]):
                newBoard[x+j,y-j] = color          
    return newBoard  

#returns index of best scenario 
def maxscore(color, scores):
    if(len(scores)==2):
        if(color == WHITE):
            if(scores[0][1]>=scores[1][1]):return 0
            else:return 1
        else:#color == BLACK
            if(scores[0][0]>=scores[1][0]):return 0
            else:return 1
        
        
    elif(len(scores)==3):
        if(color == WHITE):
            if(scores[0][1]>=scores[1][1]):
                if(scores[0][1]>=scores[2][1]):return 0
                else: return 2
            else:
                if(scores[1][1]>=scores[2][1]):return 1
                else: return 2
            
        else:
            if(scores[0][0]>=scores[1][0]):
                if(scores[0][0]>=scores[2][0]):return 0
                else: return 2
            else:
                if(scores[1][0]>=scores[2][0]):return 1
                else: return 2    
#check to see if point is legal
def onBoard(x,y):
    return (x>=0) and (x<8) and (y>=0) and (y<8)

findBestMove(WHITE)