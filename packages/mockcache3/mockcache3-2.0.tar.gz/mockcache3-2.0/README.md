The Python dictionary-based mock memcached client library. It does not
connect to any memcached server, but keeps a dictionary and stores every cache
into there internally. It is a just emulated API of memcached client only for
tests. It implements expiration also. NOT THREAD-SAFE.
This module and other memcached client libraries have the same behavior.

It is a fork from [mockcache](https://github.com/lunant/mockcache) to support
new Python versions and fix a few bugs.
