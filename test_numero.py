print("\n")

import pytest

from numero import par, impar

def test_par ():
    
    assert par (4) is True #  4 es par
    assert par (8) is True # 8 es par
    assert par (12) is True # 12 es par
    assert par (19) is False # 19 es imapar
    
def test_impar ():
    
    assert impar (21) is True  #  21 es impar 
    assert impar (33) is True #  33 es impar 
    assert impar (47) is True #  47 es impar 
    assert impar (28) is False #  28 es par
    
    
    