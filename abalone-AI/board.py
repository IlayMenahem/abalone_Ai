#TODO:
#make a game with gui


from multiprocessing.sharedctypes import Value

import numpy as np
import constants as const
import entry

class board:
    #to finish
    def __init__(self):
        # none = 0 empty = 1, white = 2, black = 3
        entries = np.full(-1,shape=(9,9), dtype='i4')
        for x in range(9):
            for y in range(9):
                if x < 
        entries = [entry(1)]*11+[entry(0)]*2+[entry(1)]*3+[entry(0)]*29+[entry(1)]*3+[entry(0)]*2+[entry(1)]*11

    def row_length(self, row):
        if(row<5):
            return row+5
        else:
            return 13-row
        
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

            