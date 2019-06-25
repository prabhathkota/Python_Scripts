"""
brew install redis

brew services start redis  ### As a background service
or
redis-server ### Not as a background service

brew services stop redis

vim /usr/local/etc/redis.conf

redis-server /usr/local/etc/redis.conf   ###start redis with a config file

Default port: 6379

redis-cli ping  ### Test if Redis is running

redis-cli flushall  ### Usually use when debugging: Clear all data

"""

import redis
r = redis.Redis(host='localhost', port=6379, db=0)
print(r)
print('-'*30)

# Reading/Writing data
print(r.set('foo', 'bar'))
print(r.get('foo'))
print('-'*30)

# increment/decrement
print(r.set('count', 1))
print(r.incr('count'))
print(r.incr('count'))
print(r.incr('count'))
print('-'*30)

# rpush, llen, and lindex
r.rpush('hispanic', 'uno')  # rpush inserts all the specified values at the tail of the list stored at key
r.rpush('hispanic', 'dos')
r.rpush('hispanic', 'tres')
r.rpush('hispanic', 'cuatro')
print(r.llen('hispanic'))   # llen returns the length of the list stored at key.
print(r.lindex('hispanic', 3))








