import timeit
import example


def sum_vec(vec):
	vec_sum = 0
	for item in vec:
		vec_sum += item
	return vec_sum


def factorial(n):
	result = 1
	for _ in range(n):
		result = result * (result+1)
	return result


vec = [i for i in range(10000)]

print(factorial(4))
# print(example.sum(vec))
# print(sum(vec))

mysetup = '''import example
vec = [i for i in range(10000)]
'''
mycode = 'example.sum(vec)'

mycode2 = 'sum(vec)'

mysetup3 = '''def sum_vec(vec):
	vec_sum = 0
	for item in vec:
		vec_sum += item
	return vec_sum
vec = [i for i in range(10000)]
'''
mycode3 = 'sum_vec(vec)'
print(f'C code: {timeit.timeit(setup=mysetup, stmt=mycode, number=100)}')
print(f'Build in function: {timeit.timeit(setup=mysetup, stmt=mycode2, number=100)}')
print(f'Python code: {timeit.timeit(setup=mysetup3, stmt=mycode3, number=100)}')

mysetup = 'import example'

mycode = 'example.factorial(10)'

mysetup2 = '''def factorial(n):
    result = 1
    for i in range(n):
       result = result * (result+1)
    return result
'''
mycode2 = 'factorial(10)'

print(f'C code: {timeit.timeit(setup=mysetup, stmt=mycode, number=100)}')
print(f'Python code: {timeit.timeit(setup=mysetup2, stmt=mycode2, number=100)}')
