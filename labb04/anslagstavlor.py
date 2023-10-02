


class board:
    def __init__(self, msg):
        self.msg = msg
        
    def main():
        chris = board("board1")
        kim = board("board2")
        
        while True:
            print("=== Bulletin board system ===")
            print("Kim reads message: Board1:")
            print("Chris reads message: Board2:")
            
            print("1: Direct Kim to other board")
            print("2: Direct Chris to other board")
            print("3: Tell Kim to post a message")
            print("4: Tell Chris to post a message")
            print("0: exit")
            choice = input("Enter choice:")
            
            if choice == "1":
                print("x")
            elif choice == "2":
                print("x")