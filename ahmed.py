data = []

print('Opening INPUT file...')

with open('input.txt') as f:
    x = 0

    for line in f:
        x = x + 1

        print('Reading line: {}'.format(x))
        
        # For Python3, use print(line)
        line = line.rstrip('\n')
        broken_line = line.split(':')
        
        new_line = '{}:{}:{}'.format(broken_line[2], broken_line[0], broken_line[1])

        print('Saving line: {} into memory.'.format(x))
        data.append(new_line)
        if 'str' in line:
            break

    print('FINISHED READING...')


with open('output.txt', 'w') as filehandle:
    print('STARTING WRITING TO OUTPUT...')
    y = 0

    for line in data:
        y = y + 1

        print('Writing line {} of {}... COMPLETED: {}%'.format(y, len(data), (y / len(data) * 100)))

        filehandle.write('%s\n' % line)

print('FINISHED! Check output.txt')