class Record:
    """
    The Record class is used to store the data from the columns in the CSV file.

    Attributes:
        csduid (str): The CSDUID of the record.
        csd (str): The CSD of the record.
        period (str): The period of the record.
        indicatorSummaryDescription (str): The indicator summary description of the record.
        unitOfMeasure (str): The unit of measure of the record.
        originalValue (str): The original value of the record.
    """

    def __init__(self, csduid, csd, period, indicatorSummaryDescription, unitOfMeasure, originalValue):
        """
        Initialize a new Record instance.

        Args:
            csduid (str): The CSDUID of the record.
            csd (str): The CSD of the record.
            period (str): The period of the record.
            indicatorSummaryDescription (str): The indicator summary description of the record.
            unitOfMeasure (str): The unit of measure of the record.
            originalValue (str): The original value of the record.
        """
        self._csduid = csduid
        self._csd = csd
        self._period = period
        self._indicatorSummaryDescription = indicatorSummaryDescription
        self._unitOfMeasure = unitOfMeasure
        self._originalValue = originalValue

    # Accessors
    @property
    def csduid(self):
        """str: Get or set the CSDUID of the record."""
        return self._csduid

    @property
    def csd(self):
        """str: Get or set the CSD of the record."""
        return self._csd

    @property
    def period(self):
        """str: Get or set the period of the record."""
        return self._period

    @property
    def indicatorSummaryDescription(self):
        """str: Get or set the indicator summary description of the record."""
        return self._indicatorSummaryDescription

    @property
    def unitOfMeasure(self):
        """str: Get or set the unit of measure of the record."""
        return self._unitOfMeasure

    @property
    def originalValue(self):
        """str: Get or set the original value of the record."""
        return self._originalValue

    # Mutators
    @csduid.setter
    def csduid(self, value):
        self._csduid = value

    @csd.setter
    def csd(self, value):
        self._csd = value

    @period.setter
    def period(self, value):
        self._period = value

    @indicatorSummaryDescription.setter
    def indicatorSummaryDescription(self, value):
        self._indicatorSummaryDescription = value

    @unitOfMeasure.setter
    def unitOfMeasure(self, value):
        self._unitOfMeasure = value

    @originalValue.setter
    def originalValue(self, value):
        self._originalValue = value

    def __str__(self):
        """
        Return a string representation of the Record object.

        Returns:
            str: A string representation of the Record object.
        """
        return (f"Record(CSDUID={self._csduid}, CSD={self._csd}, Period={self._period}, "
                f"IndicatorSummaryDescription={self._indicatorSummaryDescription}, "
                f"UnitOfMeasure={self._unitOfMeasure}, OriginalValue={self._originalValue})")