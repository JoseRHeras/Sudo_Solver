import tkinter as tk
import threading
import time

# import tictactoe as tttgame
import minmax as mm

class Player(tk.Frame):

    def __init__(self, parent, symbol="O", name="Kuru", is_player_turn=False, ai_player=False):
        super().__init__(parent)
        
        self.is_an_ai_player = ai_player
        self.is_player_turn = is_player_turn
        self.player_symbol = symbol

        self.rowconfigure([0, 1], weight=1)
        self.columnconfigure(0, weight=1)

        self.var_name = tk.StringVar()
        self.var_name.set(name)

        self.lbl_name = tk.Label(self, textvariable=self.var_name, background="blue", )
        self.lbl_name.grid(row=0, column=0, sticky="nsew")

        self.lbl_symbol = tk.Label(self, text=symbol, font=(25), background='yellow')
        self.lbl_symbol.grid(row=1, column=0, sticky="nsew")


    def make_move(self, board):
        self.main_board = board 
        threading.Thread(target=self.get_best_move_and_update_board).start()
    
    def get_best_move_and_update_board(self):
        time.sleep(1)                                   ### delay on the A.I. output. 
        row, col = mm.get_best_move(self.main_board.get_board(), True)      
        self.main_board.update_cell((row, col))     
  
    def get_player_turn(self):
        return self.is_player_turn

    def get_player_symbol(self):
        return self.player_symbol

    def get_player_name(self):
        return self.var_name.get()

    def update_name(self, new_name):
        self.var_name.set(new_name)

    def update_player_type(self, is_ai_player):
        self.is_an_ai_player = is_ai_player

    def update_player_turn(self):
        self.is_player_turn = not self.is_player_turn