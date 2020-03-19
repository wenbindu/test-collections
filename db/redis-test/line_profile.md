27.57813000679016
Timer unit: 1e-06 s

Total time: 27.2688 s
File: line_profile.py
Function: direct at line 21

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
    21                                           @profile
    22                                           def direct(r):
    23     50000    5501887.0    110.0     20.2      r.sadd('test_info', '123')
    24     50000    5465576.0    109.3     20.0      r.expire('test_info', 2)
    25     50000    5138089.0    102.8     18.8      r.get('redis_test')
    26     50000    5660353.0    113.2     20.8      r.set('redis_test', 5)
    27     50000    5502879.0    110.1     20.2      r.expire('redis_test', 10)

Total time: 18.7384 s
File: line_profile.py
Function: pipeline at line 29

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
    29                                           @profile
    30                                           def pipeline(r):
    31     50000     317686.0      6.4      1.7      p = r.pipeline()
    32     50000     198717.0      4.0      1.1      p.sadd('test_info', '123')
    33     50000     163995.0      3.3      0.9      p.expire('test_info', 2)
    34     50000     122449.0      2.4      0.7      p.get('redis_test')
    35     50000     208529.0      4.2      1.1      p.set('redis_test', 5)
    36     50000     136294.0      2.7      0.7      p.expire('redis_test', 10)
    37     50000   17590751.0    351.8     93.9      p.execute()