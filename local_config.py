
# ERPNext related configs
ERPNEXT_API_KEY = '46bc61a5d6bc557'
ERPNEXT_API_SECRET = '4fd4e476e2fa012'
ERPNEXT_URL = 'http://127.0.0.1:8000'
ERPNEXT_VERSION = 15


# operational configs
PULL_FREQUENCY = 5 # in minutes
LOGS_DIRECTORY = 'logs' # logs of this script is stored in this directory
IMPORT_START_DATE = None # format: '20190501'

# Biometric device configs (all keys mandatory)
    #- device_id - must be unique, strictly alphanumerical chars only. no space allowed.
    #- ip - device IP Address
    #- punch_direction - 'IN'/'OUT'/'AUTO'/None
    #- clear_from_device_on_fetch: if set to true then attendance is deleted after fetch is successful.
                                    #(Caution: this feature can lead to data loss if used carelessly.)
devices = [
    {'device_id':'1','ip':'192.168.1.21', 'punch_direction': 'AUTO', 'clear_from_device_on_fetch': False}
    # {'device_id':'test_2','ip':'192.168.2.209', 'punch_direction': None, 'clear_from_device_on_fetch': False}
]

# Configs updating sync timestamp in the Shift Type DocType 
# please, read this thread to know why this is necessary https://discuss.erpnext.com/t/v-12-hr-auto-attendance-purpose-of-last-sync-of-checkin-in-shift-type/52997
shift_type_device_mapping = [
    {'shift_type_name': ['General'], 'related_device_id': ['1']}
]


# Ignore following exceptions thrown by ERPNext and continue importing punch logs.
# Note: All other exceptions will halt the punch log import to erpnext.
#       1. No Employee found for the given employee User ID in the Biometric device.
#       2. Employee is inactive for the given employee User ID in the Biometric device.
#       3. Duplicate Employee Checkin found. (This exception can happen if you have cleared the logs/status.json of this script)
# Use the corresponding number to ignore the above exceptions. (Default: Ignores all the listed exceptions)
allowed_exceptions = [1,2,3]