"""
Author: Gabriel Hubert
Date: 2025-01-26
Due Date: 2025-01-26
Course: CST8002 Section 040 - Programming Research Project
Professor: Tyler DeLay
Assignment: Practical Project 1
Description: This file contains the Record class which is used to store the data from the csv file.
"""
#The Record class is used to store the data from the columns in the csv file.
class Record:
    def __init__(self, csduid, csd, period, indicatorSummaryDescription, unitOfMeasure, originalValue):
        self._csduid = csduid
        self._csd = csd
        self._period = period
        self._indicatorSummaryDescription = indicatorSummaryDescription
        self._unitOfMeasure = unitOfMeasure
        self._originalValue = originalValue

    # Accessors
    @property
    def csduid(self):
        return self._csduid

    @property
    def csd(self):
        return self._csd

    @property
    def period(self):
        return self._period

    @property
    def indicatorSummaryDescription(self):
        return self._indicatorSummaryDescription

    @property
    def unitOfMeasure(self):
        return self._unitOfMeasure

    @property
    def originalValue(self):
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

    # String representation of the Record object
    def __str__(self):
        return (f"Record(CSDUID={self._csduid}, CSD={self._csd}, Period={self._period}, IndicatorSummaryDescription={self._indicatorSummaryDescription}, UnitOfMeasure={self._unitOfMeasure}, OriginalValue={self._originalValue})")