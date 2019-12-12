"""Test for the majority of my functions.
   Created a function that test all the test code I developed, so no need to call each test funciton.
"""

from functions import *

# used to test some functions
test_string = 'yes'
test_dictionary = {'double-double': 3.65, 'fries': 1.75, 'shake': 2.25}

def test_start_order():
    """Test start_order function in few cases."""
    assert callable(start_order)
    assert isinstance(start_order('yes'), bool)
    assert start_order('yes') == False
    
    
def test_burger_selection():
    """Test burger_selection function in few cases."""
    assert callable(burger_selection)
    assert isinstance(burger_selection('double-double'), float)
    assert burger_selection('double-double') == 3.65
    
    
def test_fries_selection():
    """Test fries_selection function in few cases."""
    assert callable(fries_selection)
    assert isinstance(fries_selection('fries'), float)
    assert fries_selection('fries') == 1.75

    
def test_shake_selection():
    """Test shake_selection function in few cases."""
    assert callable(shake_selection)
    assert isinstance(shake_selection('shake'), float)
    assert shake_selection('shake') == 2.25
    
    
def test_total_cost():
    """Test total_cost function in few cases."""
    assert callable(total_cost)
    assert isinstance(total_cost('yes', 'double-double', 'fries', 'shake'), float)
    assert total_cost('yes', 'double-double', 'fries', 'shake') == 7.65

    
def test_discount_cost():
    """Test discount_cost function in few cases."""
    assert callable(discount_cost)
    assert isinstance(discount_cost('yes', 'double-double', 'fries', 'shake'), float)
    assert discount_cost('yes', 'double-double', 'fries', 'shake') == 6.885000000000001
    
    
def test_all():
    """Test all the testers I created."""
    test_start_order()
    test_burger_selection()
    test_fries_selection()
    test_shake_selection()
    test_total_cost()
    test_discount_cost()