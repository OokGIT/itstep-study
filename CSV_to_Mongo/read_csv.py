import csv
import re
from dateutil.parser import parse
from mongoengine import *
connect(host="mongodb://127.0.0.1:27017/csv_to_mongo")

# def parse_date_convert(date, fmt=None):
#     if fmt is None:
#         fmt = '%Y-%m-%d %H:%M:%S' # Defaults to : 2022-08-31 07:47:30
#     get_date_obj = parse(str(date))
#     return str(get_date_obj.strftime(fmt))

class WriteToDb(Document):
    url = StringField(required=True, primary_key=True)
    intern_id = StringField(max_length=12)
    title = StringField()
    description = StringField()
    published_at_utc = DateTimeField()


    def __str__(self):
        return self.url


with open('inbound.csv', 'r', encoding='utf-8-sig') as f:
    read_csv = csv.reader(f)
    headers_list = next(read_csv)
    # print(headers_list)
    if headers_list is not None:
        for line in read_csv:
            WriteToDb(url=line[4], intern_id=line[0], title=re.sub('\W+', ' ',line[2]), description=line[3], published_at_utc=line[5]).save()
            # item_date = parse_date_convert(line[5])
            # print(item_date)


