from funcs.Log import Log
from funcs.OpenMenu import OpenMenu


def main():
    log = Log()
    start = OpenMenu(log.get_log())


if __name__ == "__main__":
    main()
