data = []

with open('input.txt') as f:
    for line in f:
        # For Python3, use print(line)
        line = line.rstrip('\n')
        broken_line = line.split(':')
        
        new_line = '{}:{}:{}'.format(broken_line[2], broken_line[0], broken_line[1])

        data.append(new_line)
        if 'str' in line:
            break


with open('output.txt', 'w') as filehandle:
    for line in data:
        filehandle.write('%s\n' % line)

print(data)