# to run got command pallet => azurite :start  and than press F5
import logging
import sys

sys.path.append("..")
from Helpers.genericHelpers import getCurrentTimeUTC, printRows
from Helpers.sqlQueries import Query
from Helpers.sqlOperations import SqlOperations

import azure.functions as func

app = func.FunctionApp()


@app.function_name(name="mytimer")
@app.schedule(
    schedule="*/15 * * * * *",  # every 15 seconds
    arg_name="myTimer",
    run_on_startup=True,
    use_monitor=False,
)
def timer_trigger(myTimer: func.TimerRequest) -> None:
    logging.info("::-----------Python timer trigger 15 SEC---------::")
    logging.info("Python timer trigger function ran at %s", getCurrentTimeUTC())

    if myTimer.past_due:
        logging.info("The timer is past due!")

    processJob()

    logging.info("Python timer trigger function Ends at %s", getCurrentTimeUTC())


def processJob():
    # fetch the data
    projectRows = SqlOperations.getRowsFromTable(Query.Project.value)
    printRows(projectRows)

    skuRows = SqlOperations.getRowsFromTable(Query.SKU.value)
    printRows(skuRows)

    logging.info("Process Job Completed")

