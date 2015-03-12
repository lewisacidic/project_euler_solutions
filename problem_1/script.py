import sys

def is_multiple(x, y):
  return x % y == 0

def is_multiple_list(x, y_list):
  head, *tail = y_list
  return is_multiple(x, head) if not tail else is_multiple(x, head) or is_multiple_list(x, tail)

if __name__ == '__main__':
  args = list(map(int, sys.argv[1:]))
  print(sum(filter(lambda i: is_multiple_list(i, args[1:]), range(args[0]))))
