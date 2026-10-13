from simpleintrest import simInt

def test_simpleInt_pos():
    assert simInt(20000,8,12) == 19200

def test_simpleInt_zer():
    assert simInt(1000,7,0) == 0

def test_simpleInt_zero():
    assert simInt(1000,0,5) == 0