import sys
from flask import abort
import pymysql as mysql
from config import OPENAPI_AUTOGEN_DIR, DB_HOST, DB_USER, DB_PASSWD, DB_NAME

sys.path.append(OPENAPI_AUTOGEN_DIR)
from openapi_server import models

def db_cursor():
    return mysql.connect(host=DB_HOST,
                         user=DB_USER,
                         passwd=DB_PASSWD,
                         db=DB_NAME).cursor()

def get_speeds():
    with db_cursor() as cs:
        cs.execute("""
            SELECT id, startTime, endTime, avgSpeed, latStart, lonStart, latEnd, lonEnd
            FROM speedmeter
        """)
        result = [models.Speed(*row) for row in cs.fetchall()]
        return result

def get_specific_speed(speed_id):
    with db_cursor() as cs:
        cs.execute("""
            SELECT id, startTime, endTime, avgSpeed, latStart, lonStart, latEnd, lonEnd
            FROM speedmeter
            WHERE id=%s
            """, [speed_id])
        result = cs.fetchone()
    if result:
        id, startTime, endTime, avgSpeed, latStart, lonStart, latEnd, lonEnd = result
        return models.Speed(*result)
    else:
        abort(404)

def get_specific_pm25(speed_id):
    with db_cursor() as cs:
        cs.execute("""
            SELECT pm25
            FROM aqiProject
            WHERE id=%s
            """, [speed_id])
        result = cs.fetchone()
    if result:
        return result[0]
    else:
        abort(404)

def get_specific_temperature(speed_id):
    with db_cursor() as cs:
        cs.execute("""
            SELECT temperature
            FROM tmdProject
            WHERE id=%s
            """, [speed_id])
        result = cs.fetchone()
    if result:
        return result[0]
    else:
        abort(404)

def get_specific_humidity(speed_id):
    with db_cursor() as cs:
        cs.execute("""
            SELECT humidity
            FROM tmdProject
            WHERE id=%s
            """, [speed_id])
        result = cs.fetchone()
    if result:
        return result[0]
    else:
        abort(404)

def get_specific_rainfall(speed_id):
    with db_cursor() as cs:
        cs.execute("""
            SELECT rainfall
            FROM tmdProject
            WHERE id=%s
            """, [speed_id])
        result = cs.fetchone()
    if result:
        return result[0]
    else:
        abort(404)

def get_traffic_report(lat, lon):
    with db_cursor() as cs:
        cs.execute("""
            SELECT *, SQRT(POW(69.1 * (latEnd - %s), 2) + POW(69.1 * (%s - lonEnd) * COS(latEnd / 57.3), 2)) AS distance
            FROM speedmeter
            ORDER BY distance
            LIMIT 1
        """, [lat, lon])
        result = cs.fetchone()
    if result:
        # id, startTime, endTime, avgSpeed, latStart, lonStart, latEnd, lonEnd = result
        start = result[1].strftime("%Y/%m/%d %H:%M:%S").split()
        end = result[2].strftime("%Y/%m/%d %H:%M:%S").split()
        if result[3] >= 45:
            report = "not a traffic jam"
        else:
            report = "traffic jam"
        return models.TrafficReport(date=start[0], time=start[1]+" - "+end[1], traffic_status=report)
    else:
        abort(404)

def get_air_report(lat, lon):
    with db_cursor() as cs:
        cs.execute("""
            SELECT *, SQRT(POW(69.1 * (latEnd - %s), 2) + POW(69.1 * (%s - lonEnd) * COS(latEnd / 57.3), 2)) AS distance
            FROM aqiProject
            ORDER BY distance
            LIMIT 1
        """, [lat, lon])
        result = cs.fetchone()
    if result:
        # id, startTime, endTime, avgSpeed, latStart, lonStart, latEnd, lonEnd = result
        start = result[1].strftime("%Y/%m/%d %H:%M:%S").split()
        end = result[2].strftime("%Y/%m/%d %H:%M:%S").split()
        if result[3] >= 70:
            report = "อากาศแย่"
        elif result[3] >= 57:
            report = "อากาศปานกลาง"
        else:
            report = "อากาศดี"
        return models.AqiReport(date=start[0], time=start[1]+" - "+end[1], air_quality=report, pm25=result[3])
    else:
        abort(404)

def get_tmd_report(lat, lon):
    with db_cursor() as cs:
        cs.execute("""
            SELECT *, SQRT(POW(69.1 * (latEnd - %s), 2) + POW(69.1 * (%s - lonEnd) * COS(latEnd / 57.3), 2)) AS distance
            FROM tmdProject
            ORDER BY distance
            LIMIT 1
        """, [lat, lon])
        result = cs.fetchone()
    if result:
        # id, startTime, endTime, avgSpeed, latStart, lonStart, latEnd, lonEnd = result
        start = result[1].strftime("%Y/%m/%d %H:%M:%S").split()
        end = result[2].strftime("%Y/%m/%d %H:%M:%S").split()
        if result[5] > 0:
            report = "ฝนตก"
        else:
            report = "ฝนไม่ตก"
        return models.TmdReport(date=start[0], time=start[1]+" - "+end[1], rain_status=report, rainfall=result[5])
    else:
        abort(404)

# def get_basins():
#     with db_cursor() as cs:
#         cs.execute("""
#             SELECT basin_id, ename, area
#             FROM basin
#         """)
#         result = [models.Basin(*row) for row in cs.fetchall()]
#         return result

# def get_basin_details(basin_id):
#     with db_cursor() as cs:
#         cs.execute("""
#             SELECT basin_id, ename, area
#             FROM basin
#             WHERE basin_id=%s
#             """, [basin_id])
#         result = cs.fetchone()
#     if result:
#         basin_id, ename, area = result
#         return models.Basin(*result)
#     else:
#         abort(404)

# def get_basin_geom(basin_id):
#     with db_cursor() as cs:
#         cs.execute("""
#             SELECT ST_AsText(geometry)
#             FROM basin
#             WHERE basin_id=%s
#             """, [basin_id])
#         result = cs.fetchone()
#     if result:
#         return result[0]
#     else:
#         abort(404)

# def get_stations_in_basin(basin_id):
#     with db_cursor() as cs:
#         cs.execute("""
#             SELECT station_id, basin_id, ename, lat, lon
#             FROM station WHERE basin_id=%s
#             """, [basin_id])
#         result = [models.Station(*row) for row in cs.fetchall()]
#         return result

# def get_station_details(station_id):
#     with db_cursor() as cs:
#         cs.execute("""
#             SELECT station_id, basin_id, ename, lat, lon 
#             FROM station 
#             WHERE station_id=%s
#             """, [station_id])
#         result = cs.fetchone()
#     if result:
#         return models.Station(*result)
#     else:
#         abort(404)

# def get_basin_annual_rainfall(basin_id, year):
#     with db_cursor() as cs:
#         cs.execute("""
#             SELECT SUM(daily_avg)
#             FROM (
#                 SELECT r.year, r.month, r.day, AVG(r.amount) as daily_avg
#                 FROM rainfall r
#                 INNER JOIN station s ON r.station_id=s.station_id
#                 INNER JOIN basin b ON b.basin_id=s.basin_id
#                 WHERE b.basin_id=%s AND r.year=%s
#                 GROUP BY r.year, r.month, r.day
#             ) daily_avg
#         """, [basin_id, year])
#         result = cs.fetchone()
#     if result and result[0]:
#         amount = round(result[0], 2)
#         return amount
#     else:
#         abort(404)

# def get_basin_monthly_average(basin_id):
#     with db_cursor() as cs:
#         cs.execute("""
#             SELECT month, AVG(monthly_amount)
#             FROM (
#                 SELECT SUM(r.amount) as monthly_amount, month
#                 FROM rainfall r
#                 INNER JOIN station s ON r.station_id = s.station_id
#                 INNER JOIN basin b ON s.basin_id = b.basin_id
#                 WHERE b.basin_id=%s
#                 GROUP BY r.station_id, month, year
#             ) monthly
#             GROUP BY month
#             ORDER BY month ASC
#             """, [basin_id])
#         months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
#                   'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
#         result = [
#                 models.MonthlyAverage(months[month-1], month, round(amount, 2))
#                 for month, amount in cs.fetchall()
#             ]
#         return result
