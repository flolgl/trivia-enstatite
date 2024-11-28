import random
import sys

from trivia import Game


output = "Chet was added\nThey are player number 1\nPat was added\nThey are player number 2\nSue was added\nThey are player number 3\nChet is the current player\nThey have rolled a 3\nChet's new location is 3\nThe category is Rock\nRock Question 0\nAnswer was corrent!!!!\nChet now has 1 Gold Coins.\nPat is the current player\nThey have rolled a 3\nPat's new location is 3\nThe category is Rock\nRock Question 1\nAnswer was corrent!!!!\nPat now has 1 Gold Coins.\nSue is the current player\nThey have rolled a 3\nSue's new location is 3\nThe category is Rock\nRock Question 2\nAnswer was corrent!!!!\nSue now has 1 Gold Coins.\nChet is the current player\nThey have rolled a 3\nChet's new location is 6\nThe category is Sports\nSports Question 0\nAnswer was corrent!!!!\nChet now has 2 Gold Coins.\nPat is the current player\nThey have rolled a 3\nPat's new location is 6\nThe category is Sports\nSports Question 1\nAnswer was corrent!!!!\nPat now has 2 Gold Coins.\nSue is the current player\nThey have rolled a 3\nSue's new location is 6\nThe category is Sports\nSports Question 2\nAnswer was corrent!!!!\nSue now has 2 Gold Coins.\nChet is the current player\nThey have rolled a 3\nChet's new location is 9\nThe category is Science\nScience Question 0\nAnswer was corrent!!!!\nChet now has 3 Gold Coins.\nPat is the current player\nThey have rolled a 3\nPat's new location is 9\nThe category is Science\nScience Question 1\nAnswer was corrent!!!!\nPat now has 3 Gold Coins.\nSue is the current player\nThey have rolled a 3\nSue's new location is 9\nThe category is Science\nScience Question 2\nAnswer was corrent!!!!\nSue now has 3 Gold Coins.\nChet is the current player\nThey have rolled a 3\nChet's new location is 0\nThe category is Pop\nPop Question 0\nAnswer was corrent!!!!\nChet now has 4 Gold Coins.\nPat is the current player\nThey have rolled a 3\nPat's new location is 0\nThe category is Pop\nPop Question 1\nAnswer was corrent!!!!\nPat now has 4 Gold Coins.\nSue is the current player\nThey have rolled a 3\nSue's new location is 0\nThe category is Pop\nPop Question 2\nAnswer was corrent!!!!\nSue now has 4 Gold Coins.\nChet is the current player\nThey have rolled a 3\nChet's new location is 3\nThe category is Rock\nRock Question 3\nAnswer was corrent!!!!\nChet now has 5 Gold Coins.\nPat is the current player\nThey have rolled a 3\nPat's new location is 3\nThe category is Rock\nRock Question 4\nAnswer was corrent!!!!\nPat now has 5 Gold Coins.\nSue is the current player\nThey have rolled a 3\nSue's new location is 3\nThe category is Rock\nRock Question 5\nAnswer was corrent!!!!\nSue now has 5 Gold Coins.\nChet is the current player\nThey have rolled a 3\nChet's new location is 6\nThe category is Sports\nSports Question 3\nAnswer was corrent!!!!\nChet now has 6 Gold Coins."

def test_golden_master(monkeypatch, capsys):
    def mock_randrange(range):
        return 2
    monkeypatch.setattr(random, "randrange", mock_randrange)
    not_a_winner = False

    game = Game()

    game.add('Chet')
    game.add('Pat')
    game.add('Sue')

    while True:
        game.roll(random.randrange(5) + 1)

        if random.randrange(9) == 7:
            not_a_winner = game.wrong_answer()
        else:
            not_a_winner = game.was_correctly_answered()

        if not not_a_winner: break

    captured = capsys.readouterr()
    assert captured.out == output
