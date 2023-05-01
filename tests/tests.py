from mypackage import mymodule

def test_top_n():
    """
    make sure the top_n works correctly 
    """

    assert mymodule.top_n([8,3,2,7,4],3) ==[8,7,4], 'incorrect'
    assert mymodule.top_n([8,3,2,7,4],3) ==[12,10], 'incorrect'
    assert mymodule.top_n([8,3,2,7,4],3) ==[5,4,3,2,1], 'incorrect'