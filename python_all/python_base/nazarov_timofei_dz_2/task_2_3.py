time_t = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
# print(time_t)

for idx in range(len(time_t)):
    if time_t[idx].isdigit():
        time_t[idx] = f'{int(time_t[idx]):02d}'
    elif time_t[idx].startswith('+'):
        time_t[idx] = f'+{int(time_t[idx][1:]):02d}'
# print(time_t)

for v in time_t:
    if v.isdigit() or v.startswith('+'):
        i = time_t.index(v)
        number = time_t.pop(i)
        time_t.insert(i, '"')
        time_t.insert(i, '"')
        time_t.insert(0, number)

for i in range(len(time_t)-1, -1, -1):
    if time_t[i].startswith('"') and time_t[i+1].startswith('"'):
        number = time_t.pop(0)
        time_t.insert(i, number)
print(time_t)

message = ''
for i in range(len(time_t[:-1])):
    if time_t[i].startswith('+') or time_t[i].isdigit():
        message_part = time_t[i-1]+time_t[i]+time_t[i+1]+' '
        message += message_part
    elif not time_t[i].startswith('"'):
        message += f'{time_t[i]} '
last_part_msg = ''.join(time_t[-1:])
message += last_part_msg
print(message)
