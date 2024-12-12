import csv
from collections import defaultdict


class DataManager:
    def __init__(self, file_name: str):
        """
        Initializes the DataManager with the given file name.

        Args:
            file_name (str): The name of the CSV file used to store the votes.
        """
        self.file_name = file_name

    def has_voted(self, voter_id: str) -> bool:
        """
        Checks if a voter has already voted by looking for their voter ID in the file.

        Args:
            voter_id (str): The unique identifier of the voter.

        Returns:
            bool: True if the voter has voted, otherwise False.
        """
        try:
            with open(self.file_name, mode='r', newline='') as file:
                reader = csv.reader(file)
                next(reader)  # Skip header row
                for row in reader:
                    if row[0] == voter_id:
                        return True
        except FileNotFoundError:
            return False
        return False

    def record_vote(self, voter_id: str, candidate: str):
        """
        Records a vote for a given voter and candidate in the CSV file.

        Args:
            voter_id (str): The unique identifier of the voter.
            candidate (str): The name of the candidate being voted for.
        """
        try:
            with open(self.file_name, mode='a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([voter_id, candidate])
        except Exception as e:
            print(f"Error while recording vote: {e}")

    def get_results(self) -> dict[str, int]:
        """
        Retrieves the voting results, counting the votes for each candidate.

        Returns:
            dict[str, int]: A dictionary where keys are candidate names and values are the number of votes they received.
        """
        votes = defaultdict(int)
        try:
            with open(self.file_name, mode='r', newline='') as file:
                reader = csv.reader(file)
                next(reader)  # Skip header row
                for row in reader:
                    votes[row[1]] += 1

        except FileNotFoundError:
            pass
        return votes
