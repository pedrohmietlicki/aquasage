from datetime import datetime
import time
def datetime_to_seconds(dt_str):
    dt = datetime.strptime(dt_str, "%Y-%m-%d %H:%M")
    return int(time.mktime(dt.timetuple()))