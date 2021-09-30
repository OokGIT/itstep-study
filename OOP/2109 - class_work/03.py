# def return_time(seconds):
#     d = int(seconds // 3600 * 24)
#     h = int(seconds % (3600 * 24) // 3600)
#     m = int(seconds % 3600 // 60)
#     s = int(seconds % 60)
#     print('days:hours:minutes:seconds: ', d, ':', h, ':', m, ':', s, sep='')
#
#
# return_time(12360)

import datetime
secs = 360
result = datetime.timedelta(seconds=secs)
print(result)