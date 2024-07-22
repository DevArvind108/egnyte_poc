# "Helpers/genericHelpers.py"
import datetime


def printRows(rows):
    if rows:
        for row in rows:
            print(row)
    else:
        print("No Rows")


def getCurrentTimeUTC():
    return datetime.datetime.utcnow().replace(tzinfo=datetime.timezone.utc).isoformat()
