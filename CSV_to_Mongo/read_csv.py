import csv
import re
from dateutil.parser import parse
from _models import WriteToDb

# def parse_date_convert(date, fmt=None):
#     if fmt is None:
#         fmt = '%Y-%m-%d %H:%M:%S' # Defaults to : 2022-08-31 07:47:30
#     get_date_obj = parse(str(date))
#     return str(get_date_obj.strftime(fmt))




with open('inbound.csv', 'r', encoding='utf-8-sig') as f:
    read_csv = csv.reader(f)
    headers_list = next(read_csv)
    # print(headers_list)
    if headers_list is not None:
        for line in read_csv:
            WriteToDb(url=line[4], intern_id=line[0], title=re.sub('\W+', ' ',line[2]), description=line[3], published_at_utc=line[5]).save()
            # item_date = parse_date_convert(line[5])
            # print(item_date)


