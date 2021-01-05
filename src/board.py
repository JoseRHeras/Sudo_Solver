import tkinter as tk

class Board(tk.Frame):

    def __init__(self, parent, controller, player1, player2):
        super().__init__(parent)
        self.config(bg="sky blue")
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1, minsize=40)
        self.rowconfigure(2, weight=1, minsize=40)
        self.controller = controller
        self.player_one = player1
        self.player_two = player2


        self.cells = None
        self.is_game_started = False
        
        self.populate_board()
        self.button_text = tk.StringVar()
        self.button_text.set("Start")
        self.btn_board = tk.Button(self, textvariable=self.button_text, width=20, command=self.start_game)
        self.btn_board.grid(row=2, column=0)

    def start_game(self):
        self.lbl_status_text = tk.StringVar()
        self.lbl_status = tk.Label(self, textvariable=self.lbl_status_text, width=20)
        self.btn_board.grid_remove()
        self.lbl_status.grid(row=2, column=0)
        self.is_game_started = True

        if self.player_one.get_player_turn():
            self.update_status_label_with(self.player_one.get_player_name())
        elif self.player_two.get_player_turn():
            self.update_status_label_with( self.player_two.get_player_name())
            self.player_two.make_move(self)

    def update_status_label_with(self, name):
        self.lbl_status_text.set(f"{name} turn")

    def update_cell(self, location):
        row, col = location
        
        player = self.player_one if self.player_one.get_player_turn() else self.player_two      
        self.lbl_status_text.set(f"{player.get_player_name()} turn") 
        self.cells[row][col].config(text=player.get_player_symbol(), state="disabled")
        self.update_players_turn()

        if player.is_an_ai_player == False:
            self.lbl_status_text.set(f"{self.player_two.get_player_name()} turn")
            self.player_two.make_move(self)
        
    def evaluate_board(self):
        pass

    def update_players_turn(self):
        self.player_one.update_player_turn()
        self.player_two.update_player_turn()

    def set_game_to_start(self):
        self.is_game_started = True

    def get_board(self):
        table = []

        for row in self.cells:
            row_list = []
            for col in row:
                text = col['text']
                if len(text) == 0:
                    text = "."
                row_list.append(text)
            table.append(row_list)
        return table

    def populate_board(self):
        self.cells = []
        self.board = tk.Frame(self, bg="red")

        self.board.rowconfigure([0, 1, 2], weight=1, minsize=60)
        self.board.columnconfigure([0, 1, 2], weight=1, minsize=60)

        for row_index in range(3):
            local_row = []
            for col_index in range(3):
                btn_cell = tk.Button(self.board, command=lambda i = (row_index, col_index): self.update_cell(i) )
                btn_cell.grid(row=row_index, column=col_index, padx=5, pady=5, sticky="nsew")
                local_row.append(btn_cell)

            self.cells.append(local_row)

        self.board.grid(row=0, column=0, sticky="nsew")