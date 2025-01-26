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
    def __init__(self, csduid, csd, period, indicator_summary_description, unit_of_measure, original_value):
        self._csduid = csduid
        self._csd = csd
        self._period = period
        self._indicator_summary_description = indicator_summary_description
        self._unit_of_measure = unit_of_measure
        self._original_value = original_value

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
    def indicator_summary_description(self):
        return self._indicator_summary_description

    @property
    def unit_of_measure(self):
        return self._unit_of_measure

    @property
    def original_value(self):
        return self._original_value

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

    @indicator_summary_description.setter
    def indicator_summary_description(self, value):
        self._indicator_summary_description = value

    @unit_of_measure.setter
    def unit_of_measure(self, value):
        self._unit_of_measure = value

    @original_value.setter
    def original_value(self, value):
        self._original_value = value

    # String representation of the Record object
    def __str__(self):
        return (f"Record(CSDUID={self._csduid}, CSD={self._csd}, Period={self._period}, "
                f"IndicatorSummaryDescription={self._indicator_summary_description}, "
                f"UnitOfMeasure={self._unit_of_measure}, OriginalValue={self._original_value})")
