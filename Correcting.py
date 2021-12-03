__author__ = "ThIsIsTails"


class Correcting:
    def __init__(self, commands):
        self.commands = commands

    def correct(self, command: str) -> str or None:
        scores = {}  # After all operation python comparing a scores and give u answer

        for char in self.commands:
            correctness = 0
            for i in range(len(self.commands)):
                if char[i].lower() == command[i]:
                    correctness += 1
                scores[char] = correctness

        return max(scores, key=scores.get)  # Getting and returning max score from table


if __name__ == "__main__":
    c = Correcting(["hello", "world"])

    com = input("Enter Hi or wor: ")

    print("Did you mean " + c.correct(com))
    input()
