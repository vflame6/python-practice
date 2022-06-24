from pages.EnterMenu import Enter_menu


class Log():
    def __init__(self):
        if self.check_log():
            self.name = self.checked_name
        else:
            enter = Enter_menu()
            self.name = self.get_current_log()


    def check_log(self):
        with open('save\\saves.txt', 'r') as f:
            name = f.readline()
            if name:
                self.checked_name = name
                return True
            else:
                return False


    def get_current_log(self):
        with open('save\\current_log.txt', 'r') as f:
            return f.read()


    def get_log(self):
        return self.name
