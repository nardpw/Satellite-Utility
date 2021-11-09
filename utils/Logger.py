import datetime

class Logger:

    @staticmethod
    def timestamp():
        return "[" + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")) + "]"
    
    @staticmethod
    def log(message):
        print(Logger.timestamp() + " " + message)
    
    @staticmethod
    def error(exception):
        Logger.log("ERROR: " + str(exception))