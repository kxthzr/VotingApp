import sys
import os
import csv
import random
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QMessageBox, QButtonGroup
from VotingApp_ui import Ui_MainWindow
from data_manager import DataManager
from PyQt6.QtCore import Qt


class VotingApp(QMainWindow):
    def __init__(self) -> None:
        """
        Initializes the VotingApp class.
        Sets up the UI, groups the radio buttons, and connects button signals to their respective methods.
        """
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.data_manager = DataManager("votes.csv")
        self.create_csv_if_not_exists()

        # Group the radio buttons
        self.radio_button_group = QButtonGroup(self)
        self.radio_button_group.addButton(self.ui.JohnButton)
        self.radio_button_group.addButton(self.ui.JaneButton)

        # Instruction label
        self.instruction_label = QLabel("Enter the ID number to vote.", self)
        self.instruction_label.setGeometry(70, 170, 260, 20)
        self.instruction_label.show()

        # Predefined ID for voting
        self.predefined_id = str(random.randint(1000, 9999))  # Random ID between 1000 and 9999
        self.display_id_label = QLabel(f"Your voting ID is: {self.predefined_id}", self)
        self.display_id_label.setGeometry(80, 140, 260, 20)
        self.display_id_label.show()

        # Connect buttons to their functions
        self.ui.VoteButton.clicked.connect(self.cast_vote)
        self.ui.ResultsButton.clicked.connect(self.show_results)

    def create_csv_if_not_exists(self) -> None:
        """
        Creates the votes.csv file if it does not already exist.
        Writes the header row to the file.
        """
        if not os.path.exists(self.data_manager.file_name):
            with open(self.data_manager.file_name, mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(["Voter ID", "Candidate"])

    def cast_vote(self) -> None:
        """
        Handles the vote-casting process.
        Validates the voter ID and candidate selection, checks if the voter has already voted,
        and records the vote if all conditions are met.
        """
        voter_id = self.ui.textEdit.toPlainText().strip()
        candidate = "John" if self.ui.JohnButton.isChecked() else "Jane" if self.ui.JaneButton.isChecked() else None
        self.ui.results_display.setStyleSheet("color: green;")

        if not voter_id.isdigit():
            self.ui.results_display.setText(
                "<p style='text-align: center;'>Invalid ID format. Please enter numbers only.")
            self.ui.results_display.setStyleSheet("color: red;")
            return

        if voter_id != self.predefined_id:
            self.ui.results_display.setText(
                f"<p style='text-align: center;'>Invalid ID. Please enter your ID provided.")
            self.ui.results_display.setStyleSheet("color: red;")
            return

        if not candidate:
            self.ui.results_display.setText("<p style='text-align: center;'>Please select a candidate to vote for.")
            self.ui.results_display.setStyleSheet("color: red;")
            self.ui.results_display.setAlignment(Qt.AlignmentFlag.AlignCenter)
            return

        if self.data_manager.has_voted(voter_id):
            self.ui.results_display.setText(f"<p style='text-align: center;'>ID {voter_id} has already voted.")
            self.ui.results_display.setStyleSheet("color: red;")
            self.ui.results_display.setAlignment(Qt.AlignmentFlag.AlignCenter)
            return

        self.data_manager.record_vote(voter_id, candidate)
        self.ui.results_display.setText(f"<p style='text-align: center;'>Your vote for {candidate} has been recorded.")
        self.ui.results_display.setStyleSheet("color: green; font-weight: bold; ")
        self.ui.results_display.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.ui.textEdit.clear()

        # Unselect radio buttons after voting
        self.radio_button_group.setExclusive(False)
        self.ui.JohnButton.setChecked(False)
        self.ui.JaneButton.setChecked(False)
        self.radio_button_group.setExclusive(True)

    def show_results(self) -> None:
        """
        Displays the voting results.
        Shows the number of votes each candidate has received.
        """
        results = self.data_manager.get_results()
        if not results:
            self.ui.results_display.setText("No votes have been cast yet.")
            self.ui.results_display.setStyleSheet("color: red;")
            return

        results_text = "\n".join([f"<p style='text-align: center;'>{candidate}: {count} votes" for candidate, count in results.items()])
        self.ui.results_display.setText(results_text)
        self.ui.results_display.setStyleSheet("color: green;")

