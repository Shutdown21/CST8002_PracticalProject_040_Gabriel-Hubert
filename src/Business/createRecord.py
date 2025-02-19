from Model.record import Record


def createRecord(csduid, csd, period, indicatorSummaryDescription, unitOfMeasure, originalValue, records):
    new_record = Record(
        csduid, csd, period, indicatorSummaryDescription, unitOfMeasure, originalValue
    )
    records.append(new_record)
    return records

