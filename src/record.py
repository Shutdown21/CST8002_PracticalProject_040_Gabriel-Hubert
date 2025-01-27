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
        self.csduid = csduid
        self.csd = csd
        self.period = period
        self.indicatorSummaryDescription = indicatorSummaryDescription
        self.unitOfMeasure = unitOfMeasure
        self.originalValue = originalValue

    # Accessors
    @property
    def csduid(self):
        return self.csduid

    @property
    def csd(self):
        return self.csd

    @property
    def period(self):
        return self.period

    @property
    def indicatorSummaryDescription(self):
        return self.indicatorSummaryDescription

    @property
    def unitOfMeasure(self):
        return self.unitOfMeasure

    @property
    def originalValue(self):
        return self.originalValue

    # Mutators
    @csduid.setter
    def csduid(self, value):
        self.csduid = value

    @csd.setter
    def csd(self, value):
        self.csd = value

    @period.setter
    def period(self, value):
        self.period = value

    @indicatorSummaryDescription.setter
    def indicatorSummaryDescription(self, value):
        self.indicatorSummaryDescription = value

    @unitOfMeasure.setter
    def unitOfMeasure(self, value):
        self.unitOfMeasure = value

    @originalValue.setter
    def originalValue(self, value):
        self.originalValue = value

    # String representation of the Record object
    def __str__(self):
        return (f"Record(CSDUID={self.csduid}, CSD={self.csd}, Period={self.period}, IndicatorSummaryDescription={self.indicatorSummaryDescription}, UnitOfMeasure={self.unitOfMeasure}, OriginalValue={self.originalValue})")

