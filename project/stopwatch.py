from datetime import datetime


class StopWatch:
    def __init__(self):
        self.start_time = datetime.now()
        self.current_marker = None
        self.current_marker_time = None

    def mark(self, message):
        print(">", message, end=" ")
        if self.current_marker is not None:
            print(datetime.now() - self.current_marker_time)

        self.current_marker = message
        self.current_marker_time = datetime.now()

    def end(self):
        print(datetime.now() - self.current_marker_time)
        print("Total process time:", datetime.now() - self.start_time)
