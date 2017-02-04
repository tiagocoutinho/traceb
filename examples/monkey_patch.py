import sys
import traceb
import traceback

traceb.monkey_patch(tb_mode='compressed', show_args=True)

def div(a, b):
  return a / b

def f(a, b):
  div(a+1, b)

def g(a, b):
  f(a+1, b)

def h(a, b):
  g(a+1, b)

try:
    h(1, 0)
except:
    traceback.print_exc()
    print 80*"-"
