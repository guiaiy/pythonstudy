for i in range(1, 10):
    for j in range(1, i+1):
        if i*j < 10:
            print('%s X %s = %s' % (j, i, i*j), end='   ')
        else:
            print('%s X %s = %s' % (j, i, i*j), end='  ')
    print()


