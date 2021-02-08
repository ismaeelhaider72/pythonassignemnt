import datetime
import sys

err = []
on = []
off = []
with open(sys.argv[1], 'rt') as f:
    data = f.readlines()
    if(data):
        for line in data:
            if line.__contains__('Device State: OFF'):
                off.append(line)
            elif line.__contains__('Device State: ON'):
                     on.append(line)
            elif line.__contains__('ERR'):
                     err.append(line)


        on=[i.split('[', 1)[0] for i in on]
        off = [i.split('[', 1)[0] for i in off]
        err = [i.split('[', 1)[0] for i in err]
    else:
        print("no record found")


def totaltime(on, off):
    format = '%b %d %H:%M:%S:%f '
    i=0
    time=0
    while(i<len(on)):
        onevent = datetime.datetime.strptime(on[i], format)
        offevent = datetime.datetime.strptime(off[i], format)
        result=(offevent - onevent).total_seconds()
        time=time+result
        i=i+1
    return time

print("Device was ON for ",(totaltime(on, off)),'seconds')
print('Timestamps of error events:')
i=0
while i<len(err):
    print(err[i])
    i=i+1

