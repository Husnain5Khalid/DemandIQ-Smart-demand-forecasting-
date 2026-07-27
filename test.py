from demand_iq.exception import DemandIQException
import sys

try:

    number = 10 / 0

except Exception as e:

    raise DemandIQException(e, sys)