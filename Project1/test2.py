# import logging
# import os

# import azure.functions as func

# app = func.FunctionApp()

# @app.function_name(name="HttpTrigger1")
# @app.route(route="req")
# def main(req: func.HttpRequest) -> func.HttpResponse:
#   # Get the setting named 'myAppSetting'
#   my_app_setting_value = os.environ["myAppSetting"]
#   logging.info(f'My app setting value:{my_app_setting_value}')