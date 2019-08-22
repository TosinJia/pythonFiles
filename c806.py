
# 默认（值）参数
def print_student_info(name, gender='M', age=20, college='XXUniversity'):
    print('name: '+name)
    print('\t|-gender: '+gender)
    print("\t|-age: "+str(age))
    print('\t|-college: '+college)

print_student_info('tosin', 'M', 22, 'cclg')
print_student_info('s01')
print_student_info('s02', 'W', 24)
print_student_info('s03', gender='W', age=26)

print_student_info('s04', age=28)

