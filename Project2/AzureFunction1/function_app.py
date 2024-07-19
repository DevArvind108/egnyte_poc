import logging
import datetime
import azure.functions as func

app = func.FunctionApp()

@app.function_name(name="mytimer")
@app.schedule(schedule="01 0 0 * * *", 
              arg_name="myTimer", 
              run_on_startup=True,
              use_monitor=False) 
def asana_timer_trigger(myTimer: func.TimerRequest) -> None:
    utc_timestamp = datetime.datetime.utcnow().replace(
        tzinfo=datetime.timezone.utc).isoformat()
    
    if myTimer.past_due:
        logging.info('The timer is past due!')

    logging.info('Python timer trigger function ran at %s', utc_timestamp)