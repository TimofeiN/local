time_t = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
# print(time_t)

for idx in range(len(time_t)):
    if time_t[idx].isdigit():
        time_t[idx] = f'{int(time_t[idx]):02d}'
    elif time_t[idx].startswith('+'):
        time_t[idx] = f'+{int(time_t[idx][1:]):02d}'

new_time_t = []
for v in time_t:
    if v.isdigit() or v[1:].isdigit():
        new_time_t.append('"')
        new_time_t.append(v)
        new_time_t.append('"')
    else:
        new_time_t.append(v)
print(new_time_t)

message = []
for i in range(len(new_time_t)):
    if new_time_t[i].startswith('+') or new_time_t[i].isdigit():
        message_part = new_time_t[i - 1] + new_time_t[i] + new_time_t[i + 1]
        message.append(message_part)
    elif not new_time_t[i].startswith('"'):
        message.append(new_time_t[i])
# print(message)

message = ' '.join(message)
print(message)
