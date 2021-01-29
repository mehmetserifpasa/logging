import datetime


class log:

    def __init__(self):
        time = datetime.datetime.now()
        self.date = time.strftime("%c")

    def __call__(self, *args):
        self.debug(args[0], args[1])

    def Create(self, filename):
        self.filename = filename
        self.filename_create = open(str(self.filename), "a")

    def debug(self, logType, logDesc):
        self.filename_create.writelines(
            str(logType).upper() + " " +
            "[" + self.date + "]" + " " +
            str(logDesc) +
            "\n"
        )


