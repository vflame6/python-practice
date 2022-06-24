from pages.GameMenu import GameMenu


class OpenMenu():
    def __init__(self, login):
        self.login = login
        game = GameMenu(self.login)
        game.OpenMenu()
