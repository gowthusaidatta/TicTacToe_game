import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self):
        self.Current_player = "x"
        self.board = [["", "", ""], ["", "", ""], ["", "", ""]]
        self.window = tk.Tk()
        self.window.title("Tic Tac Toe")
        self.buttons = []
        for i in range(3):
            row = []
            for j in range(3):
                button = tk.Button(self.window, text="", width=20, height=10,command=lambda i=i,j=j:self.Make_Move(i,j))
                button.grid(row=i, column=j)
                row.append(button)
            self.buttons.append(row)
    def Make_Move(self,row,col):
        if self.board[row][col]=="":
            self.board[row][col]=self.Current_player
            self.buttons[row][col].config(text=self.Current_player)
            if self.Check_Winner(self.Current_player):
                messagebox.showinfo("Game Over","The winner is "+self.Current_player)
                self.window.quit
                self.window.destroy()
            elif self.is_Draw():
                messagebox.showinfo("Game Over "," Game is Draw ")
                self.window.quit
                self.window.destroy()
            self.Current_player="O" if self.Current_player=="x" else "x"
    def Check_Winner(self,Player):
        for i in range(3):
            if Player==self.board[i][0]==self.board[i][1]==self.board[i][2]:
                return True    
            if Player==self.board[0][i]==self.board[1][i]==self.board[2][i]:
                return True  
            if Player==self.board[0][0]==self.board[1][1]==self.board[2][2]:
                return True
            if Player==self.board[0][2]==self.board[1][1]==self.board[2][0]:
                return True 
            return False  
    def is_Draw(self):
        for row in self.board:
            if "" in row:
                return False
            else: return True
               
    def run(self):
        self.window.mainloop()

game = TicTacToe()
game.run()
