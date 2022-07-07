import re

Date = 2020|2|2

dmatch = re.fullmatch(r'^("^\d{3}-?\d{2}-?\d{4}$)', Date)
#dmatch = re.findall(r'^(\d{4}(0[1-9]|1[0-2])|(0[1-9]|[12][0-9]|3[01])$)', Date)
print(dmatch)
