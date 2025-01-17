from src.arthematic_operations import add, sub

def test_add():
    assert add(2,3)==5
    assert add(-9,9)==0
    assert add(-1, -10)==-11
    assert add(-5,6)==1
    assert add(-12,10)==-2

def test_sub():
    assert sub(2,3)==-1
    assert sub(5,2)==3
    assert sub(-10,-20)==10
    
