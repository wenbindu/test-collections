from copy import deepcopy
import simdjson
from line_profiler import LineProfiler

stream_remove_fields = [
    'data.extra.event.outComeData'
]


def remove_data_in_spin(data):
    """
    remove some data of spin before save to stream
    :param data: {"data":{"extra":{"event":{"outComeData":"[2,3,45]", "key": "value"}}}}
    :return: {"data":{"extra":{"event":{"key": "value"}}}}
    """
    data = deepcopy(data)

    for field in stream_remove_fields:
        data_backup = data_copy = data.copy()
        split_field = field.split(".")
        for item in split_field[:-1]:
            data_copy = data_copy.get(item, {})
            print(data_copy)
        data_copy.pop(split_field[-1], None)
        data = data_backup

    return data


def for_range():
    z = {"data":{"extra":{"event":{"outComeData":"[2,3,45]", "key": "value"}}}}
    for _ in range(100000):
        k = remove_data_in_spin(z)
    remove_data_in_spin(z)
    # pj = simdjson.ParsedJson(z)
    # print(pj.items('.data'))

if __name__ == '__main__':
    prof = LineProfiler()
    prof.add_function(remove_data_in_spin)
    prof.enable_by_count()
    for_range()
    prof.print_stats()
    

# python -m cProfile -s cumtime copy_test.py
# 