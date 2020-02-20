from sumproduct import sumproduct
def test_sumproduct():
    """ Test for sumproduct """
    assert sumproduct(3, 2) == (5, 6)
    assert sumproduct(5, 7) != (15, 30)
    
