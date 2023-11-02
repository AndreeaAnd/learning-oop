import math_pipeline

nrs = range(30)
print(type(nrs))
print(list(math_pipeline.to_str(math_pipeline.to_square(math_pipeline.to_even(nrs)))))
print(list(math_pipeline.to_str(math_pipeline.to_cube(math_pipeline.to_odd(nrs)))))