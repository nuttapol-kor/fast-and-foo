from openapi_server import models
import sys
from flask import abort
import pymysql as mysql
from config import OPENAPI_AUTOGEN_DIR, DB_HOST, DB_USER, DB_PASSWD, DB_NAME

sys.path.append(OPENAPI_AUTOGEN_DIR)


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
            report = "Clear road"
        else:
            report = "Traffic jam"
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
            report = "Unhealthy"
        elif result[3] >= 57:
            report = "Moderate"
        else:
            report = "Good"
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
            report = "Rain"
        else:
            report = "Cleary sky"
        return models.TmdReport(date=start[0], time=start[1]+" - "+end[1], rain_status=report, rainfall=result[5])
    else:
        abort(404)
