import unittest
from hangman import get_random_word, hangmangame


class TestHangman(unittest.TestCase):
    def setUp(self):
        self.word = get_random_word()
        self.game = hangmangame()

    def test_hangman_revealed_letter_matches(self):
        # self.game.guess()
        updated_hangman_string = self.game.status()
        self.assertEqual(updated_hangman_string, "_ _ _")


if __name__ == '__main__':
    unittest.main()
