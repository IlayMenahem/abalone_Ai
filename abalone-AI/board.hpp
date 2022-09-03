#include <map>
#include <iostream>
#include <cassert>
//add struct (called tuple) of n integers (like a tuple).
//add struct of n tuples (like a tuple).
//ilay3 ata poh?

class board{
    private:
        char spaces [61];
        std::map<int[3], int[6][3]> possibleMoves3;
        std::map<int[2], int[6][2]> possibleMoves2;
        std::map<int[1], int[6][1]> possibleMoves1;

    public:
        board(){
            possibleMoves3[{1,2,3}] = {{0,0,0},{0,0,0},{0,0,0},{0,0,0},{0,0,0},{0,0,0}};
        }

        /**
         * @brief changes to c at index index
         * 
         * @param index 
         * @param c 
         */
        void change(int index, char c){
            spaces[index] = c;
        }

        /**
         * @brief 
         * 
         * @param indices 
         * @return true 
         */
        bool legal_tuple(int indices[]){
            
        }
}