# How to reproduce
```
virtualenv -p <python3.5> pulsar-pex
cd pulsar-pex
pex -vvvv -r requirements.txt -o virtualenv.pex
./virtualenv.pex manage.py
```

Note that we're not doing pip install -r requirements.txt

This will create a standalone zip/binary of the entire environment that can be easily distributed and used to run apps.


# Error Output
```
(pulsar-pex) Robs-MacBook-Pro:pulsar-pex rgil$ ./virtualenv.pex manage.py 
Traceback (most recent call last):
  File ".bootstrap/_pex/pex.py", line 326, in execute
  File ".bootstrap/_pex/pex.py", line 258, in _wrap_coverage
  File ".bootstrap/_pex/pex.py", line 290, in _wrap_profiling
  File ".bootstrap/_pex/pex.py", line 372, in _execute
  File ".bootstrap/_pex/pex.py", line 382, in execute_interpreter
  File ".bootstrap/_pex/pex.py", line 412, in execute_content
  File ".bootstrap/_pex/compatibility.py", line 72, in exec_function
  File "manage.py", line 46, in <module>
    server().start()
  File "/Users/rgil/.pex/install/pulsar-1.4.1-cp35-cp35m-macosx_10_11_x86_64.whl.f65d6cae4f83ab554f929a3af8a2f8376c3e54ff/pulsar-1.4.1-cp35-cp35m-macosx_10_11_x86_64.whl/pulsar/apps/__init__.py", line 352, in start
    on_start = self()
  File "/Users/rgil/.pex/install/pulsar-1.4.1-cp35-cp35m-macosx_10_11_x86_64.whl.f65d6cae4f83ab554f929a3af8a2f8376c3e54ff/pulsar-1.4.1-cp35-cp35m-macosx_10_11_x86_64.whl/pulsar/apps/__init__.py", line 461, in __call__
    actor = pulsar.arbiter(cfg=self.cfg.clone())
  File "/Users/rgil/.pex/install/pulsar-1.4.1-cp35-cp35m-macosx_10_11_x86_64.whl.f65d6cae4f83ab554f929a3af8a2f8376c3e54ff/pulsar-1.4.1-cp35-cp35m-macosx_10_11_x86_64.whl/pulsar/utils/config.py", line 387, in clone
    return pickle.loads(pickle.dumps(self))
_pickle.PicklingError: Can't pickle <class '__main__.Site'>: attribute lookup Site on __main__ failed
```
