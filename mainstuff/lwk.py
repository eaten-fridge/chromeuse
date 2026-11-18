import sys
import valid as v
def main():
    #this is a menu interface for stuff that i make, like a Driver's Ed assistant
    #as shown in 'PG1'
    PG1 = 'Driving Time Calculator'
    PG2 = 'Chess (scuffed)'
    PG3 = 'placeholder'
    

    print('Please choose a option from below.')
    #now its time to display the options
    print('#1:\t', PG1)
    #so far we only have 1 option, which is okay
    print('#2\t', PG2)
    #time for the choice part of all of this
    choice = v.tg('|>')
    #v.tg is a number validator in a different place of the folder, therefore the import at the top (valid)
    if choice == 1:
        print("Launching ", PG1, '...', sep = '')
        pg1()
    elif choice == 2:
        print('Launching ', PG2, '...', sep = '')
        pg2()
    elif choice > 2 or choice < 1:
        print('Please enter a valid number.')
        #literally just more validation just in case


def pg1():
    pass
    print() #this is just a blank spacer
    main() #restarts

def pg2():

    import chess
    import random

    def evaluate_board(board):
        if board.is_checkmate():
            return -100000 if board.turn else 100000

        if board.is_stalemate() or board.is_insufficient_material():
            return 0

        values = {
            chess.PAWN: 100,
            chess.KNIGHT: 320,
            chess.BISHOP: 330,
            chess.ROOK: 500,
            chess.QUEEN: 900,
            chess.KING: 20000
        }

        score = 0

        for piece_type, value in values.items():
            score += len(board.pieces(piece_type, chess.WHITE)) * value
            score -= len(board.pieces(piece_type, chess.BLACK)) * value

        return score


    def minimax(board, depth, alpha, beta, maximizing):
        if depth == 0 or board.is_game_over():
            return evaluate_board(board)

        if maximizing:
            best_score = -float("inf")

            for move in board.legal_moves:
                board.push(move)
                score = minimax(board, depth - 1, alpha, beta, False)
                board.pop()

                best_score = max(best_score, score)
                alpha = max(alpha, score)

                if beta <= alpha:
                    break

            return best_score

        else:
            best_score = float("inf")

            for move in board.legal_moves:
                board.push(move)
                score = minimax(board, depth - 1, alpha, beta, True)
                board.pop()

                best_score = min(best_score, score)
                beta = min(beta, score)

                if beta <= alpha:
                    break

            return best_score


    def ai_move(board):
        best_move = None
        best_score = float("inf")

        moves = list(board.legal_moves)
        random.shuffle(moves)

        for move in moves:
            board.push(move)
            score = minimax(board, 2, -float("inf"), float("inf"), True)
            board.pop()

            if score < best_score:
                best_score = score
                best_move = move

        return best_move
    def display_board(board):
        print("\n")
        print(board)
        print("\n  a b c d e f g h")
        print("")


    def play_chess():
        board = chess.Board()

        print("================================")
        print("       PYTHON CHESS AI")
        print("================================")
        print("You are WHITE.")
        print("The AI is BLACK.")
        print("Enter moves like: e2e4")
        print("Enter 'quit' to exit.")

        while not board.is_game_over():

            display_board(board)

            if board.turn == chess.WHITE:
                move_input = input("Your move: ").strip().lower()

                if move_input == "quit":
                    print("Thanks for playing!")
                    main()
                    return

                try:
                    move = chess.Move.from_uci(move_input)

                    if move not in board.legal_moves:
                        print("Illegal move! Try again.")
                        continue

                    board.push(move)

                except ValueError:
                    print("Invalid input! Example: e2e4")

            else:
                print("AI is thinking...")
                move = ai_move(board)
                print("AI plays:", move.uci())
                board.push(move)

        display_board(board)

        print("GAME OVER!")
        print("Result:", board.result())

        if board.is_checkmate():
            print("Checkmate!")

        elif board.is_stalemate():
            print("Stalemate!")

        main()

    play_chess()
main()