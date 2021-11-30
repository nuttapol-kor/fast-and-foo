import connexion
import six

from openapi_server.models.aqi_report import AqiReport  # noqa: E501
from openapi_server.models.speed import Speed  # noqa: E501
from openapi_server.models.tmd_report import TmdReport  # noqa: E501
from openapi_server.models.traffic_report import TrafficReport  # noqa: E501
from openapi_server import util


def controller_get_air_report(lat, lon):  # noqa: E501
    """JeeJee

     # noqa: E501

    :param lat: 
    :type lat: 
    :param lon: 
    :type lon: 

    :rtype: AqiReport
    """
    return 'do some magic!'


def controller_get_specific_humidity(speed_id):  # noqa: E501
    """JeeJee

     # noqa: E501

    :param speed_id: 
    :type speed_id: int

    :rtype: int
    """
    return 'do some magic!'


def controller_get_specific_pm25(speed_id):  # noqa: E501
    """JeeJee

     # noqa: E501

    :param speed_id: 
    :type speed_id: int

    :rtype: float
    """
    return 'do some magic!'


def controller_get_specific_rainfall(speed_id):  # noqa: E501
    """JeeJee

     # noqa: E501

    :param speed_id: 
    :type speed_id: int

    :rtype: float
    """
    return 'do some magic!'


def controller_get_specific_speed(speed_id):  # noqa: E501
    """JeeJee

     # noqa: E501

    :param speed_id: 
    :type speed_id: int

    :rtype: Speed
    """
    return 'do some magic!'


def controller_get_specific_temperature(speed_id):  # noqa: E501
    """JeeJee

     # noqa: E501

    :param speed_id: 
    :type speed_id: int

    :rtype: float
    """
    return 'do some magic!'


def controller_get_speeds():  # noqa: E501
    """Returns a list speed data.

     # noqa: E501


    :rtype: List[Speed]
    """
    return 'do some magic!'


def controller_get_tmd_report(lat, lon):  # noqa: E501
    """JeeJee

     # noqa: E501

    :param lat: 
    :type lat: 
    :param lon: 
    :type lon: 

    :rtype: TmdReport
    """
    return 'do some magic!'


def controller_get_traffic_report(lat, lon):  # noqa: E501
    """JeeJee

     # noqa: E501

    :param lat: 
    :type lat: 
    :param lon: 
    :type lon: 

    :rtype: TrafficReport
    """
    return 'do some magic!'
