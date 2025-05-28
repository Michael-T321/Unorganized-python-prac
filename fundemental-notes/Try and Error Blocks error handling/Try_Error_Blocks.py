
import os

try:
    f = open('/Users/mikeytaylor/CS Supplementry Work/Try and Error Blocks error handling/test_file.txt')
    var = bad_var
except FileNotFoundError:
    print('Sorry. This file does not exist')
except Exception:
    print('Sorry. Something went wrong')

""" else:
    pass
finally:
    pass """