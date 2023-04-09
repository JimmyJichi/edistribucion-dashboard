from datetime import datetime, timedelta


def format_date_dashes(date: str) -> datetime:
    return datetime.strptime(date, "%Y-%m-%d")


def format_date_slashes(date: str) -> datetime:
    return datetime.strptime(date, "%d/%m/%Y")


# data_is_complete will be True if the data is complete (not missing valueDouble attribute in any object)
# Data is often incomplete because electricity measures often have a delay of 1-2 days until they are
# available in the online website of EDistribución
def data_is_complete(electricity_data: dict) -> bool:
    return all("valueDouble" in obj for obj in electricity_data)


# month_is_complete will be True if the data es complete (complete = true is present in all the objects)
# since the variable electricity_data_month will only be all the days in the same month, it is safe to just check the complete attribute
def month_is_complete(electricity_data_month: dict) -> bool:
    return all(obj["complete"] == True for obj in electricity_data_month)


# Given a list of datetimes, group them by those who are consecutive and 
def group_datetimes_by_consecutive_days(datetimes: list):
    if not datetimes:
        return []
    
    datetimes.sort()
    result = [[datetimes[0]]]
    for i in range(1, len(datetimes)):
        if datetimes[i] - datetimes[i-1] <= timedelta(days=1):
            result[-1].append(datetimes[i])
        else:
            result.append([datetimes[i]])
    
    # return a list of pairs (start,end) where start and end are datetime objects
    result = [(date_range[0], date_range[-1]) for date_range in result]
    return result