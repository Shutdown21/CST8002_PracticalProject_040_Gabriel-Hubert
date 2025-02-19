from Model.record import Record

def createRecord(csduid, csd, period, indicatorSummaryDescription, unitOfMeasure, originalValue, records):
    """
    Create a new record and add it to the records list.

    Args:
        csduid (str): The CSDUID of the record.
        csd (str): The CSD of the record.
        period (str): The period of the record.
        indicatorSummaryDescription (str): The indicator summary description of the record.
        unitOfMeasure (str): The unit of measure of the record.
        originalValue (str): The original value of the record.
        records (list): The list of records to which the new record will be added.

    Returns:
        list: The updated list of records with the new record added.
    """
    new_record = Record(
        csduid, csd, period, indicatorSummaryDescription, unitOfMeasure, originalValue
    )
    records.append(new_record)
    return records

