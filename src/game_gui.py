
import tkinter as tk
from player import Player
from board import Board

class TicTacToeGame(tk.Tk):

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)
        self.title("Tic-Tac-Toe with AI")

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.rowconfigure(0, weight=1)
        container.columnconfigure(0, weight=1)
        self.frames = {}

        screens = (
            (StartPage,"500x280"),
            (SelectModePage, "500x280"),
            (GatherHumanPlayerInfoPage, "500x280"),
            (GameMainScreen, "500x280")
        )
            
        for F, geometry in screens:
            frame = F(container, self)
            self.frames[F] = (frame, geometry)
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, controller):
        frame, geometry = self.frames[controller]
        
        self.geometry(geometry)
        frame.tkraise()

    def get_screen(self, name):
        return self.frames[name][0]


class StartPage(tk.Frame):
    
    def __init__(self, parent, controller):
        super().__init__(parent, bg="red")
        
        lbl_welcome_msg = tk.Label(self, text="Welcome to \nTic-Tac-Toe", font=("Calibri", 10),)       
        btn_start = tk.Button(self, text="Start Game", command=lambda: controller.show_frame(SelectModePage))

        lbl_welcome_msg.pack(pady=10, padx=10)
        btn_start.pack(pady=30)


class SelectModePage(tk.Frame):
    
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        
        lbl_mesg = tk.Label(self, text="Enter your name:")
        btn_PVP = tk.Button(self, text="P vs C", command=lambda: controller.show_frame(GatherHumanPlayerInfoPage))
        btn_PVC = tk.Button(self, text="C vs C", command=self.activate_ai_vs_ai_mode)

        lbl_mesg.pack(pady=10)
        btn_PVP.pack(pady=10)
        btn_PVC.pack()

    def activate_ai_vs_ai_mode(self):

        self.controller.show_frame(GameMainScreen)

class GatherHumanPlayerInfoPage(tk.Frame):
    
    def __init__(self, parent, controller):
        super().__init__(parent)

        self.cont = controller
        self.player_first = tk.BooleanVar(self)

        lbl_enter_name = tk.Label(self, text="Enter player name \nLeave blank for no name:")
        self.ety_name_input = tk.Entry(self)
        self.check_turn_selector = tk.Checkbutton(self, text="Let me take the first turn", variable=self.player_first, onvalue=True, offvalue=False, command=self.update_player_turn)
        btn_ready = tk.Button(self, text="All Set", command=self.lauch_game_main_screen)

        
        lbl_enter_name.pack(pady=10)
        self.ety_name_input.pack(pady=10)
        self.check_turn_selector.pack(pady=10)
        btn_ready.pack()


    def lauch_game_main_screen(self):
        self.cont.get_screen(GameMainScreen).set_player_name(self.ety_name_input.get())
        self.cont.show_frame(GameMainScreen)

    
    def update_player_turn(self):
        if self.player_first.get() is True:
            self.check_turn_selector.select()
        else:
            self.check_turn_selector.deselect()

        self.cont.get_screen(GameMainScreen).update_mode()
        

class GameMainScreen(tk.Frame):
    
    def __init__(self, parent, controller):
        super().__init__(parent)
        
        self.rowconfigure(0, weight=1, minsize=60)
        self.columnconfigure([0, 2], weight=4)
        self.columnconfigure(1, weight=1)
        self.config(bg="light sky blue")

        #Create players
        self.frm_player1 = Player(self)
        self.frm_player2 = Player(self, "X", "Kike", True, True)

        #Center column
        self.frm_center = Board(self, controller, self.frm_player1, self.frm_player2)
        
        #Position widgets in screen
        self.frm_player1.grid(row=0, column=0, sticky="nsew")
        self.frm_player2.grid(row=0, column=2, sticky="nsew")
        self.frm_center.grid(row=0, column=1)
  
    def update_mode(self):
        self.frm_center.update_players_turn()

    def set_player_name(self, name):
        name = name if len(name) > 0 else "No name";
        self.frm_player1.update_name(name)
        self.frm_player1.update_player_type(False)
        

    def get_players(self):
        return self.frm_player1, self.frm_player2

class ResultPage(tk.Frame):
    pass


# class Board(tk.Frame):

#     def __init__(self, parent, controller, player1, player2):
#         super().__init__(parent)
#         self.config(bg="sky blue")
#         self.rowconfigure(0, weight=1)
#         self.rowconfigure(1, weight=1, minsize=40)
#         self.rowconfigure(2, weight=1, minsize=40)
#         self.controller = controller
#         self.player_one = player1
#         self.player_two = player2


#         self.cells = None
#         self.is_game_started = False
        
#         self.populate_board()
#         self.button_text = tk.StringVar()
#         self.button_text.set("Start")
#         self.btn_board = tk.Button(self, textvariable=self.button_text, width=20, command=self.start_game)
#         self.btn_board.grid(row=2, column=0)

#     def start_game(self):
#         self.lbl_status_text = tk.StringVar()
#         self.lbl_status = tk.Label(self, textvariable=self.lbl_status_text, width=20)
#         self.btn_board.grid_remove()
#         self.lbl_status.grid(row=2, column=0)
#         self.is_game_started = True

#         if self.player_one.get_player_turn():
#             self.update_status_label_with(self.player_one.get_player_name())
#         elif self.player_two.get_player_turn():
#             self.update_status_label_with( self.player_two.get_player_name())
#             self.player_two.make_move(self)

#     def update_status_label_with(self, name):
#         self.lbl_status_text.set(f"{name} turn")

#     def update_cell(self, location):
#         row, col = location
        
#         player = self.player_one if self.player_one.get_player_turn() else self.player_two      
#         self.lbl_status_text.set(f"{player.get_player_name()} turn") 
#         self.cells[row][col].config(text=player.get_player_symbol(), state="disabled")
#         self.update_players_turn()

#         if player.is_an_ai_player == False:
#             self.lbl_status_text.set(f"{self.player_two.get_player_name()} turn")
#             self.player_two.make_move(self)
        
#     def evaluate_board(self):
#         pass

#     def update_players_turn(self):
#         self.player_one.update_player_turn()
#         self.player_two.update_player_turn()

#     def set_game_to_start(self):
#         self.is_game_started = True

#     def get_board(self):
#         table = []

#         for row in self.cells:
#             row_list = []
#             for col in row:
#                 text = col['text']
#                 if len(text) == 0:
#                     text = "."
#                 row_list.append(text)
#             table.append(row_list)
#         return table

#     def populate_board(self):
#         self.cells = []
#         self.board = tk.Frame(self, bg="red")

#         self.board.rowconfigure([0, 1, 2], weight=1, minsize=60)
#         self.board.columnconfigure([0, 1, 2], weight=1, minsize=60)

#         for row_index in range(3):
#             local_row = []
#             for col_index in range(3):
#                 btn_cell = tk.Button(self.board, command=lambda i = (row_index, col_index): self.update_cell(i) )
#                 btn_cell.grid(row=row_index, column=col_index, padx=5, pady=5, sticky="nsew")
#                 local_row.append(btn_cell)

#             self.cells.append(local_row)

#         self.board.grid(row=0, column=0, sticky="nsew")

    



        
