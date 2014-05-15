Mapper:

#!/usr/bin/python

import sys

while 1:
    line = sys.stdin.readline()
    if line == "":
        break
    fields = line.split(",")
    year = fields[1]
    runs = fields[8]

    if year == "1956":
       print runs


Reducer: 
#!/usr/bin/python

import sys
total_count = 0
for line in sys.stdin:
    try:
        count = int(line)
        total_count += count
    except ValueError:
        # count was not a number, so silently
        # ignore/discard this line
        continue

print total_count
