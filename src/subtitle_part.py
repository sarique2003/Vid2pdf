class SubtitlePart:
    def __init__(self, start_time, end_time, text):
        self.start_time = start_time
        self.end_time = end_time
        self.text = text

    def __str__(self):
        return "{}-{}".format(self.start_time, self.end_time)

    def __repr__(self):
        return self.__str__()
