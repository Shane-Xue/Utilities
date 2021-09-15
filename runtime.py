import time
# class and function to make runtime more readable
unit = {
    "decade": 365*3600*24*10,
    # seriously? I decided to use 364.25 for a year! haha!
    "year": 365*3600*24,
    # year is 365 days
    "month": 30*60*60*24,
    # month is 30 days
    # try not to use month and year because they cause mistakes in caluculations
    "week": 7*60*60*24,
    "day": 60*60*24,
    "hour": 60*60,
    "minute": 60,
    "second": 1,
    # basic unit (unit "1")
    "millisecond": 10**(-3),
    "microsecond": 10**(-6),
    "nanosecond": 10**(-9)
}


def cast(time, To, From=unit["second"]):
    """
    notice that To is before From in the list.
    """
    return time*(From/To)


class TimerError(Exception):
    def __init__(self, msg):
        super().__init__(msg)


class Timer():
    def __init__(self):
        self.start_time = 0
        self.end_time = 0
        self.tot_time = 0
        self.pause_time = 0  # the time that the time is stoped. should be reset with every resume
        self.pauses = []
        self.laps = []

    # data saving methods
    def start(self):
        if self.end_time == 0 and self.start_time != 0:
            raise TimerError("The timer is still running! You cannot start.")
        elif self.start_time != 0:
            self.__init__()
        self.start_time = time.time()

    def end(self):
        """
        Notice this method will stop the timer ‘forever’
        When you call start it will start timing all over again
        """
        self.end_time = time.time()
        self.tot_time = self.start_time-end_time-accum(pauses)

    def lap(self):
        self.laps.append(time.time()-self.start_time)

    def pause(self):
        if self.pause_time != 0:
            raise TimerError("The timer is already paused!")
        self.pause_time = time.time()

    def resume(self):
        if self.pause_time == 0:
            raise TimerError("The timer is not paused!")
        self.pauses.append(time.time()-self.pause_time)
        self.pause_time = 0

    def reset(self):
        """
        this clears all the data by calling __init__
        this means that the timer is implicitly stopped
        """
        self.__init__()

    # data retrieving methods
    def get_start(self):
        return self.start_time

    def get_end(self):
        return self.end_time

    def get_tot(self):
        return self.tot_time

    def get_pauses(self):
        """
        notice this returns a list of all the pauses
        returns empty list of there are no elements in the list
        """
        return self.pauses

    def get_current_pause_start(self):
        if self.pause_time == 0:
            raise TimerError("Timer is not paused!")
        return self.pause_time

    def get_latest_pause(self):
        """
        return -1 if no pause has been performed.
        notice if the timer is paused this will still return the length of the latest
        resumed pause
        """
        return self.pauses[-1]

    def get_pauses_time(self):
        return accum(self.pauses)

    def get_laps(self):
        return self.laps

    def get_pause(self, serial):
        """
        gets the serial’th pause time
        returns -1 (an illegal data) when there is no such pause
        this is for preparing against malitious programming
        """
        try:
            return self.pauses[serial]
        except IndexError as IE:
            return -1

    def get_lap_now(self):
        self.lap()
        return self.laps[-1]

    def get_latest_lap(self):
        return self.laps[-1]


def main():
    print(unit)
    timer = Timer()
    timer.start()
    print(timer.get_start())
    time.sleep(1)
    timer.pause()
    print(timer.get_current_pause_start())
    time.sleep(1)
    timer.resume()
    timer.pause()
    time.sleep(2)
    timer.resume()
    print(timer.get_pauses())


if __name__ == "__main__":
    main()
