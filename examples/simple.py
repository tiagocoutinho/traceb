import sys
import traceb
import traceback

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
    traceb.print_exc()
    print 80*"-"
    traceb.print_exc(tb_mode='compressed', show_args=True)
    print 80*"-"
    traceback.print_exc()
