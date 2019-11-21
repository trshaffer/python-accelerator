#This is a test function file for whether eval() such
#Within the file, there is a function, the function being called
#  and the call ### asdf = sympy.Rational(3,2) ###
#  This method call is from a module, sympy, that is imported in
#  the main fork loop. This proves that the namespaces/imports are shared
#  For further details, please refer the to the fork loop file
#  
#  Additionally, this module imports a test_module, which has the side effect
#  of sleeping for 10 seconds. This proves that the import is happening in the
#  function file. The namespace does not persist for parent process though, and
#  I cannot import actual modules (non-self-made) here that will actually work
# 
#  Finally, the outputs currently are not passed back from the child process. 
#  Since the globals is still only changing for the child process, it does not make
#  it back out to the parent process memory. This is tested at the end

import test_module
import sympy
def thing():
    x = 5
    y= 8
    f = open('README', 'rU')
    text = f.read()
    f.close
    print(text)
    asdf = sympy.Rational(3,2)
    print(asdf)
    #sympy.asdfsadfsadf()
    return_val = "hello Tim!"


thing()
#print(globals()['return_val'])
print(os.getpid())
import test_module_fail
sys.exit(43)
