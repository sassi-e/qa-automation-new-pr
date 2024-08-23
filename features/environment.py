import json
import os
from types import SimpleNamespace
from behave import use_fixture
from fixtures import browser_chrome
import configparser



def open_json_config(context, json_conf):
    try:
        with open(json_conf, "r") as file:
            loaded_data = json.load(file)
            parsed_json = json.loads(json.dumps(loaded_data), object_hook=lambda d: SimpleNamespace(**d))
            for key in list(loaded_data.keys()):
                setattr(context, key, getattr(parsed_json, key))
    except IOError as error:
        raise error
    

def setup_debug_on_error(userdata):
    global BEHAVE_DEBUG_ON_ERROR
    BEHAVE_DEBUG_ON_ERROR = userdata.getbool("BEHAVE_DEBUG_ON_ERROR")    

def before_all(context):
    json_conf = os.environ['USERDATA']
    json_conf = f'{json_conf};'
    json_files = json_conf.split(";")
    for json_file in json_files:
        if json_file.strip() != '':
            open_json_config(context=context, json_conf=json_file)


    use_fixture(browser_chrome, context)
    setup_debug_on_error(context.config.userdata)

    userdata = context.config.userdata
    configfile = userdata.get("configfile", "userconfig.ini")
    section = userdata.get("config_section", "behave.userdata")
    parser = configparser.SafeConfigParser()
    parser.read(configfile)
    if parser.has_section(section):
        userdata.update(parser.items(section))