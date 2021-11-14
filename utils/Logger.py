import datetime

class Color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

class Logger:

    @staticmethod
    def timestamp():
        return "[" + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")) + "]"
    
    @staticmethod
    def log(message):
        print(Color.BOLD + Color.GREEN + Logger.timestamp() + Color.END + " " + message)

    @staticmethod
    def error(message):
        print(Color.BOLD + Color.RED + Logger.timestamp() + Color.END + " " + message)

    @staticmethod
    def warning(message):
        print(Color.BOLD + Color.YELLOW + Logger.timestamp() + Color.END + " " + message)

    @staticmethod
    def info(message):
        print(Color.BOLD + Color.BLUE + Logger.timestamp() + Color.END + " " + message)

    @staticmethod
    def debug(message):
        print(Color.BOLD + Color.PURPLE + Logger.timestamp() + Color.END + " " + message)

    @staticmethod
    def success(message):
        print(Color.BOLD + Color.GREEN + Logger.timestamp() + Color.END + " " + message)