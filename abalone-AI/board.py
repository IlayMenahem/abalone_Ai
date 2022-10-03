#TODO:
#make a game with gui
#enable game actions 

from multiprocessing.sharedctypes import Value

import numpy as np
import constants as const
import entry

class board:
    '''
    counstracts a new board
    '''
    def __init__(self):
        # none = 0 empty = 1, white = 2, black = 3
        entries = [2]*5+[0]*4
        +[2]*6+[0]*3
        +[1]*2+[2]*3+[1]*2+[0]*2
        +[1]*8+[0]
        +[1]*9
        +[1]*8+[0]
        +[1]*2+[3]*3+[1]*2+[0]*2
        +[3]*6+[0]*3
        +[3]*5+[0]*4
        entries = np.array(entries, dtype='i4')
        np.reshape(entries,(9,9))

    '''
    @param the row
    @returns the length of the row
    '''
    def row_length(row):
        if(row<5):
            return row+5
        else:
            return 13-row
    
    '''
    @param potential move
    @return if that move is legal
    '''
    def legal_moves(self,move):
        pass
    def gen_neighbors(self, row, index):
        res = []
        if(row==0):
            if(index>0):
                res.append((row,index-1))
            if(index<4):
                res.append((row,index+1))
            res.append((row+1,index))
            res.append((row+1,index+1))
        if(row<8):
            if(index>0):
                res.append((row,index-1))
            if(index<4):
                res.append((row,index+1))
            res.append((row-1,index))
            res.append((row-1,index+1))
        else:
            if(index>0):
                res.append((row,index-1))
            if(index<self.row_length(row)-1):
                res.append((row,index+1))
            if(row<4):
                res.append((row+1,index))
                res.append((row+1,index+1))
                if(index>0):
                    res.append((row-1,index-1))
                if(index<self.row_length(row)-1):
                    res.append((row-1,index))
            if(row>4)#todo
                res.append((row-1,index))
                res.append((row-1,index+1))
                if(index>0):
                    res.append((row+1,index-1))
                if(index<self.row_length(row)-1):
                    res.append((row+1,index))
            if(row==4):
                if(index>0):
                    res.append((row+1,index-1))
                if(index<self.row_length(row)-1):
                    res.append((row+1,index))

            