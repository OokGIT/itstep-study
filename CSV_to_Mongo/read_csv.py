import csv
import datetime
from _models import WriteToDb

CSV_FILE = 'inbound.csv'
CSV_ENCODING = 'utf-8-sig'


with open(CSV_FILE, 'r', encoding=CSV_ENCODING) as f:
    read_csv = csv.reader(f)
    headers_list = next(read_csv)
    if headers_list is not None:
        for line in read_csv:
            if WriteToDb.objects.filter(url=line[4]):
                print('Item already in DB. Duplicates will not be written')
                continue
            elif not line[4].startswith('http'):
                print('Seems there is not http/https address found. String will not be written to DB')
                continue
            WriteToDb(internal_id=line[0], title=line[2], description=line[3], url=line[4],
                      published_utc=datetime.datetime.strptime(line[5], '%Y-%m-%d %H:%M:%S%z'),
                      site=line[11]).save()
