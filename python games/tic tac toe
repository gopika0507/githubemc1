import tkinter as tk
from tkinter import messagebox #mainly allows to show text pop up box as in for errors or warnings 
class TicTacToe:
    def __init__(self): # this initializes the variables,can take inputs as well
        self.window = tk.Tk()
        self.window.title("Tic Tac Toe")
        self.current_player = 'X'
        self.board = [[None] * 3 for i in range(3)] #creats single row with 3none clos,and the for  i in range 3 (0,1,2) repeats it for 3 total times
        self.buttons = [[None] * 3 for i in range(3)]
        
        self.create_widgets()
        
    def create_widgets(self):
        for row in range(3):
            for col in range(3):
                btn = tk.Button(self.window, text='',font=('normal', 40),#since the etxt in the box is empty the font and style are not necessary 
                                #but using it only to defnife the size
                width=5,#width and height is just to define the size of the tic tac toe box for x and 0
                height=2,#5 and 2 means it could hold 5 avg words and 2 avg words
                command=lambda r=row, c=col: self.on_button_click(r, c))#the values r and c capture the current values of row and col form the surrounding and pass the values to the function
                btn.grid(row=row, column=col)
                self.buttons[row][col] = btn
        
    def on_button_click(self, row, col):
        if self.board[row][col] is None:
            self.board[row][col] = self.current_player
            self.buttons[row][col].config(text=self.current_player)
            
            if self.check_winner():
                messagebox.showinfo("Game Over", f"Player {self.current_player} wins!")
                self.reset_game()
            elif self.check_draw():
                messagebox.showinfo("Game Over", "It's a draw!")
                self.reset_game()
            else:
                self.current_player = 'O' if self.current_player == 'X' else 'X'
    
    def check_winner(self):
        for row in range(3):
            if all(self.board[row][col] == self.current_player for col in range(3)):
                return True
        for col in range(3):
            if all(self.board[row][col] == self.current_player for row in range(3)):
                return True
        if all(self.board[i][i] == self.current_player for i in range(3)):
            return True
        if all(self.board[i][2-i] == self.current_player for i in range(3)):
            return True
        return False
    
    def check_draw(self):
        return all(self.board[row][col] is not None for row in range(3) for col in range(3))
    
    def reset_game(self):
        self.current_player = 'X'
        self.board = [[None] * 3 for i in range(3)]
        for row in range(3):
            for col in range(3):
                self.buttons[row][col].config(text='')
                
    def run(self):
        self.window.mainloop()
if __name__ == "__main__":
    game = TicTacToe()
    game.run()
