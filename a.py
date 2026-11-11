import random

# 生成 [0.0, 1.0) 之间的浮点数
print(random.random())

# 生成 [1, 10] 之间的整数，包含 1 和 10
print(random.randint(1, 10))

# 生成 [1, 10) 之间的整数，不包含 10
print(random.randrange(1, 10))

# 生成 [1, 10] 之间的浮点数
print(random.uniform(1, 10))
