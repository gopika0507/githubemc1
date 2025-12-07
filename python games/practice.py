import tkinter as tk
from tkinter import messagebox

class tic_tac_toe:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("tic_tac_toe")
        self.current_player="x"
        self.board=[3*[None] for i in range(3)]
        self.button=[3*[None] for i in range(3)]
        self.create_widget()

    def create_widget(self):
        for row in range(3):
            for col in range(3):
                btn=tk.Button(text="",font=("normal",40),width=5,height=2,command= lambda r=row,c=col: self.on_button_click(r,c))
                btn.grid(row=row,column=col)
                self.button[row][col]=btn

    def on_button_click(self,row,col):
        if self.board[row][col] is None:
            self.board[row][col]=self.current_player
            self.button[row][col].config(text=self.current_player)

            if self.check_winner():
                messagebox.showinfo("Game Over",f"Player {self.current_player} wins.")
                self.reset_game()

            elif self.check_draw():
                messagebox.showinfo("gameover",f"game is a draw")
                self.reset_game()

            else:
                self.current_player="o" if self.current_player == "x" else "x"

    def check_winner(self):
        for row in range(3):
            if all(self.board[row][col]==self.current_player for col in range(3)):
                return True
            
        for col in range(3):
            if all(self.board[row][col]==self.current_player for row in range(3)):
                return True
            
        if all(self.board[i][i]==self.current_player for i in range(3)):
                return True
            
        if all(self.board[i][2-i]==self.current_player for i in range(3)):
                return True
            
        return False
    
    def check_draw(self):
        if all(self.board[row][col] is not None for row in range(3) for col in range(3)):
            return True
        
    def reset_game(self):
        self.current_player='x'
        self.board=[[None]*3 for i in range(3)]
        for row in range(3):
            for col in range(3):
                self.button[row][col].config(text=" ")
       


    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    game = tic_tac_toe()
    game.run()

                



        
       