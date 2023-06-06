from datetime import datetime

def add_dates(dict):
    for key, datestring in dict.items():
        if "date" in key:
            dict[key] = datetime.fromisoformat(datestring)

def try_save(object):
    try:
        object.save()
        result = "ok"
    except:
        result = "error"
    return result