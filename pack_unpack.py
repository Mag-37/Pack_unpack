def print_params(a=1, b='str', c=False):
    print(a, b, c)

print_params()
print_params(b=25)
print_params(c=[1,2,3])

value_list = [1, 'str', True]
dict_list = {'a': 1, 'b': False, 'c': 'Ложь'}
print_params(*value_list)
print_params(**dict_list)

value_list_2 = ('Pack-Unpack', True)
print_params(*value_list_2, 42)