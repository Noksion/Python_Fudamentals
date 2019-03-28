from functools import partial

print(partial(lambda x, y: x * y, 2)(10))
