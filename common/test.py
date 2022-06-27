import getopt
import sys

print(sys.argv, sys.argv[0])

opts, args = getopt.gnu_getopt(sys.argv[1:], 'i:o:v', ['input=', 'output_path=', 'version'])
print(opts)
print(args)


# https://blog.csdn.net/qq_16912257/article/details/52222540
# > python test.py arg1 arg2 -i input --output output -v
# ['test.py', 'arg1', 'arg2', '-i', 'input', '--output', 'output', '-v']
# [('-i', 'input'), ('--output_path', 'output'), ('-v', '')]
# ['arg1', 'arg2']

