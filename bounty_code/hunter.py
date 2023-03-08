class Hunter:
    """
    A class used to represent a Bounty Hunter.

    Attributes
    ----------
    __MIN_PAY : int
        minimum allowed payment

    __MIN_DAY : int
        minimum allowed of days to complete task

    Methods
    -------
    calculatePayRate() -> None
        uses _pay and _days to calculate pay rate of Bounty Hunter

    availabilitySetter(available : bool) -> None
        allows to update available property
    """

    __MIN_PAY = 2
    __MIN_DAY = 1

    def __init__(self, pay, days, name="Cad Bane"):
        """
        Constructs all the necessary attributes for the bounty hunter object.

        Parameters
        ----------
            pay : int
                pay per task completed. Must be greater than 1
            days : int
                number of days to complete one task. Must be greater than 0
            name : str
                name of the bounty hunter
        """

        if days < self.__MIN_DAY:
            raise ValueError("days must be greater than 0")
        else:
            self._days = days

        if pay < self.__MIN_PAY:
            raise ValueError("pay is too little!")
        else:
            self._pay = pay

        self._name = name
        self.available = True
        self.days_on_task = 0
        self.calculatePayRate()

    def __eq__(self, other):
        return True if self._name == other._name and self._pay == other._pay else False

    def __str__(self):
        return f"""
        Hunter {self._name}:
            pay per task: {self._pay}
            number of days to completion: {self._days}
            pay rate: {self._pay_rate}
        """

    def __repr__(self):
        return f"Hunter(name='{self._name}', " f"pay={self._pay} "

    def calculatePayRate(self):
        self._pay_rate = self._pay / self._days

    def availability(self, newAvailability: bool) -> None:
        self.available = newAvailability

    def daysOnTaskSetter(self, new_day: int) -> None:
        self.days_on_task = new_day

    @property
    def isAvailable(self):
        return self.available

    @property
    def getPay(self):
        return self._pay

    @property
    def getDays(self):
        return self._days

    @property
    def getPayRate(self):
        return self._pay_rate
