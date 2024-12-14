import sys
from PyQt6.QtWidgets import QApplication
from VotingApp import VotingApp

def main():
    """
    Main function to initialize and run the Voting App.
    """
    app = QApplication(sys.argv)
    main_window = VotingApp()
    main_window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
