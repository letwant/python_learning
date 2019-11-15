
def consumer():
    r = ''
    while True:
        n = yield r
        if not n:
            return
        print('[CONSUMER] Consuming %s...' % n)
        r = '200 OK'

def produce(o):
    o.send(None)
    n = 0
    while n < 6:
        n += 1
        print('[PRODUCER] Producing %s...' % n)
        r = o.send(n)
        print('[PRODUCER] Consumer return: %s' % r)
    o.close()

c = consumer()
produce(c)
