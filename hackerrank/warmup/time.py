def run(ampm_string):
    time = ampm_string.split(':')
    meridian = time[2][2:]
    time[2] = time[2][:2]
    if meridian == 'PM' and time[0] != '12':
        time[0] = str(int(time[0]) + 12)
    if meridian == 'AM' and time[0] == '12':
        time[0] = '00'

    print ':'.join(time)

ampm_string = raw_input()
run(ampm_string)