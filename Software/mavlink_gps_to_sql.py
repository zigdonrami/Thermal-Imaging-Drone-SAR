
import pymysql
import time
from pymavlink import mavutil

conn = pymysql.connect(host='localhost',user='root', password = "password",db='GPS')
cur = conn.cursor()
query = """CREATE TABLE IF NOT EXISTS GPS (
    LATITUDE FLOAT,
    LONGITUDE FLOAT,
    ALTITUDE INT,
    DATE_TIME DATETIME,
    GPSSTATUS INT
);"""
cur.execute(query)
conn.commit()

print ("Start Script")
master = mavutil.mavlink_connection('udpin:localhost:14551') # 14551 30003 192.168.64.30:30003
master.wait_heartbeat()
print("Heartbeat from system (system %u component %u)" % (master.target_system, master.target_component))

print(master.messages.get('GPS_RAW_INT'))


# Wait for the GPS to be detected
while master.messages.get('GPS_RAW_INT') is None:
    master = mavutil.mavlink_connection('udpin:localhost:14551') # 14551 30003 192.168.64.30:30003
    master.wait_heartbeat()
    print(master.messages.get('GPS_RAW_INT'))
    time.sleep(1)

while True:
  master.wait_heartbeat()
  gps = master.messages.get('GPS_RAW_INT')
  if(gps is None):
        print(".")
        continue
  print(gps)
  query = "INSERT INTO GPS(LATITUDE,LONGITUDE,ALTITUDE,GPSSTATUS) VALUES({},{},{},{})"
  query = query.format(gps.lat,gps.lon,gps.alt,gps.satellites_visible)
  cur.execute(query)
  conn.commit()
  #print("Data Inserted in the table ")
  #conn.close()
  time.sleep(1)
