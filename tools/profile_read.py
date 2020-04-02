import pstats
path = "/var/log/slots/test_1585728421683.prof"
p = pstats.Stats(path)
p.sort_stats("cumulative")
p.print_stats()