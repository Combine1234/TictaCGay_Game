##################################################################################################################################
##################################################################################################################################
# This code created by Fronkja1221 [Fronk][Thanawat Sukam p o r N] #
# Enjoy the game bro and u can read how to place the cell in the Cell.jpg naja bro #
# if u not read this i think u are gay pls read me bro #
##################################################################################################################################
##################################################################################################################################
#Import using
import cv2
import mediapipe as mp
import tkinter as tk
from tkinter import messagebox
import threading



#Game all
class HandTicTacToe:
    def __init__(self):
        self.num = 1
        self.num2 = 0
        self.index_state = True
        self.middle_state = False
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands()
        self.cap = cv2.VideoCapture(0)
        self.current_player = "X"
        self.board = [["" for _ in range(3)] for _ in range(3)]
        self.root = tk.Tk()
        self.root.title("Holy Fucking finger to control tictactoe")
        self.labels = [[None for _ in range(3)] for _ in range(3)]
        self.create_board()
    #For create the sussy game
    def create_board(self):
        for i in range(3):
            for j in range(3):
                self.labels[i][j] = tk.Label(self.root, text="", font=('Arial', 30), width=4, height=2)
                self.labels[i][j].grid(row=i, column=j)

        self.entry = tk.Entry(self.root)
        self.entry.grid(row=3, columnspan=3)
        self.entry.bind("<Return>", self.process_input)

    #for run the tictacgay
    def process_input(self):

        row, col = self.parse_input()
        if row is None or col is None:
            return
        if self.board[row][col] == "":
            self.board[row][col] = self.current_player
            self.labels[row][col].config(text=self.current_player)
            if self.check_winner():
                messagebox.showinfo("Winner", f"{self.current_player} wins!")
                self.reset_game()
            elif self.check_draw():
                messagebox.showinfo("Draw", "It's a draw!")
                self.reset_game()
            else:
                self.switch_player()
        else:
            messagebox.showerror("Invalid Move", "This cell is already occupied!")

    #check the input that what ta fak is cell
    def parse_input(self):
        if self.num == 1 and self.num2 == 1:
            self.num = 0
            self.num2 = 0
            return 0, 0
        elif self.num == 2 and self.num2 == 1:
            self.num = 0
            self.num2 = 0
            return 0, 1
        elif self.num == 3 and self.num2 == 1:
            self.num = 0
            self.num2 = 0
            return 0, 2
        elif self.num == 4 and self.num2 == 1:
            self.num = 0
            self.num2 = 0
            return 1, 0
        elif self.num == 5 and self.num2 == 1:
            self.num = 0
            self.num2 = 0
            return 1, 1
        elif self.num == 6 and self.num2 == 1:
            self.num = 0
            self.num2 = 0
            return 1, 2
        elif self.num == 7 and self.num2 == 1:
            self.num = 0
            self.num2 = 0
            return 2, 0
        elif self.num == 8 and self.num2 == 1:
            self.num = 0
            self.num2 = 0
            return 2, 1
        elif self.num == 9 and self.num2 == 1:
            self.num = 0
            self.num2 = 0
            return 2, 2
        else:
            return None, None
    #Check what who is the fucking winner
    def check_winner(self):
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != "":
                return True
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != "":
                return True
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != "":
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != "":
            return True
        return False
    
    #Check that u are draw
    def check_draw(self):
        for row in self.board:
            for cell in row:
                if cell == "":
                    return False
        return True
    
    #nothing. it just change the player x to o o to x
    def switch_player(self):
        self.current_player = "O" if self.current_player == "X" else "X"

    #just for reset the game
    def reset_game(self):
        self.current_player = "X"
        self.board = [["" for _ in range(3)] for _ in range(3)]
        for i in range(3):
            for j in range(3):
                self.labels[i][j].config(text="")

    #it detect finger not hand so sorry na
    def hand_detection(self):
        while self.cap.isOpened():
            ret, frame = self.cap.read()
            if not ret:
                break

            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            results = self.hands.process(rgb_frame)

            if results.multi_hand_landmarks:
                for hand_landmarks in results.multi_hand_landmarks:
                    index_landmark = hand_landmarks.landmark[self.mp_hands.HandLandmark.INDEX_FINGER_TIP]
                    thumb_landmark = hand_landmarks.landmark[self.mp_hands.HandLandmark.THUMB_TIP]
                    middle_landmark = hand_landmarks.landmark[self.mp_hands.HandLandmark.MIDDLE_FINGER_TIP]

                    h, w, _ = frame.shape
                    index_px = int(index_landmark.x * w), int(index_landmark.y * h)
                    thumb_px = int(thumb_landmark.x * w), int(thumb_landmark.y * h)
                    middle_px = int(middle_landmark.x * w), int(middle_landmark.y * h)

                    if is_touching(index_px, thumb_px):
                        cv2.putText(frame, 'Index Fucked', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                        if self.index_state == True:
                            self.num += 1
                            self.index_state = False
                    else:
                        if not self.index_state:
                            self.index_state = True
                            self.process_input()

                    if is_touching(middle_px, thumb_px):
                        cv2.putText(frame, 'Middle Fucked', (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                        if self.middle_state == True:
                            self.num2 = 1
                            self.middle_state = False
                    else:
                        if self.middle_state == False:
                            self.middle_state = True
                            self.process_input()

                    cv2.circle(frame, index_px, 5, (255, 0, 0), -1)
                    cv2.circle(frame, thumb_px, 5, (255, 0, 0), -1)
                    cv2.circle(frame, middle_px, 5, (255, 0, 0), -1)
            print(self.num)
            cv2.imshow('Gay? Detection oh so sorry, Hand Detection', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        self.cap.release()
        cv2.destroyAllWindows()

    #we use system treading because python is suck can't run two code in the same time
    def run(self):
        hand_thread = threading.Thread(target=self.hand_detection)
        hand_thread.start()

        self.root.mainloop()
        
def is_touching(landmark1, landmark2, threshold=30):
    return abs(landmark1[0] - landmark2[0]) < threshold and abs(landmark1[1] - landmark2[1]) < threshold

if __name__ == "__main__":
    game = HandTicTacToe()
    game.run()
