import pymysql
from datetime import datetime, timedelta

img_name = 1

def get_gps_data():
    conn = pymysql.connect(
        host='127.0.0.1',
        user='root',
        password='password',
        db='GPS'
        )
    cursor = conn.cursor()
    cursor.execute("select @@version")
    version = cursor.fetchone()
    if version:
        print("DB connection ok")
        print(version)
    else:
        print("DB connection has some problems!")
    now = datetime.now() - timedelta(seconds=10)
    dt_string = now.strftime("%Y-%m-%d %H:%M:%S")
    query = "SELECT * FROM GPS WHERE date_time >= {}   ORDER BY date_time asc LIMIT 1"
    query = query.format("'"+dt_string+"'")
    cursor.execute(query)
    result = cursor.fetchall()
    # (LAT,LON)
    for row in result:
        return row[:2]


def get_image_name(gps_data):
    #listOfGlobals = globals()
    #listOfGlobals['img_name'] = listOfGlobals['img_name']  + 1
    #return str(img_name) + ".jpg"
    try:
        return str(gps_data[0])+str(gps_data[1])+".jpg"
    except Exception as e:
        print(e)
        return None