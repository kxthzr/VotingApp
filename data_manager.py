import csv
from collections import defaultdict


class DataManager:
    def __init__(self, file_name: str):
        self.file_name = file_name

    def has_voted(self, voter_id: str) -> bool:
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
        try:
            with open(self.file_name, mode='a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([voter_id, candidate])
        except Exception as e:
            print(f"Error while recording vote: {e}")

    def get_results(self) -> dict:
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
