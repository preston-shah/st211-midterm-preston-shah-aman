"""ST211 Bookstore QA Midterm Test Suite.

Author: Preston Shah
"""
import pytest
from bookstore_app import Users, Catalog, Cart


# ==============================================================================
# PHASE 3: SMOKE TESTS
# ==============================================================================

@pytest.mark.smoke
def test_smoke_register_new_user():
    """Author: Preston Shah. Smoke: Registering a new user returns True."""
    u = Users()
    assert u.register("preston", "pass123") is True


@pytest.mark.smoke
def test_smoke_login_correct_and_incorrect_password():
    """Author: Preston Shah. Smoke: Login succeeds with matching alphanumeric pw and fails with wrong pw."""
    u = Users()
    u.register("preston", "pass123")
    assert u.login("preston", "pass123") is True
    assert u.login("preston", "wrongpassword") is False


@pytest.mark.smoke
def test_smoke_catalog_add_and_store_product():
    """Author: Preston Shah. Smoke: Adding a product stores it in catalog.products."""
    cat = Catalog()
    cat.add_product(101, "Python Testing", 25)
    assert 101 in cat.products
    assert cat.products[101] == {"title": "Python Testing", "price": 25}


@pytest.mark.smoke
def test_smoke_cart_add_item_verifies_state():
    """Author: Preston Shah. Smoke: Adding a product appends its product_id to cart.items."""
    cat = Catalog()
    cat.add_product(101, "Python Testing", 25)
    c = Cart(cat)
    result = c.add(101)
    assert result is True
    assert 101 in c.items


@pytest.mark.smoke
def test_smoke_checkout_non_empty_cart():
    """Author: Preston Shah. Smoke: Checking out a non-empty cart returns items and empties cart."""
    cat = Catalog()
    cat.add_product(101, "Python Testing", 25)
    c = Cart(cat)
    c.add(101)
    order = c.checkout()
    assert order == [101]
    assert c.items == []

    # ==============================================================================
# PHASE 4: SLOW TESTS
# ==============================================================================

@pytest.mark.slow
def test_slow_bulk_product_import():
    """Author: Preston Shah. Slow test: Imports 20,000 products into the catalog.
    
    Why slow: Iterates through 20,000 product tuples calling Catalog.add_product,
    executing thousands of dict insertions and timing overhead.
    """
    cat = Catalog()
    c = Cart(cat)
    large_catalog_data = [(i, f"Book {i}", 10 + (i % 50)) for i in range(20000)]
    imported_count = c.import_products(large_catalog_data)
    
    # Check that products were actually stored in the catalog
    assert 19999 in cat.products
    assert cat.products[19999]["title"] == "Book 19999"


@pytest.mark.slow
def test_slow_large_cart_repeated_total_calculation():
    """Author: Preston Shah. Slow test: Calculates total on a cart with 10,000 items repeatedly.
    
    Why slow: Builds a 10,000 item cart and computes total multiple times across thousands 
    of list iterations and dictionary lookups.
    """
    cat = Catalog()
    for i in range(100):
        cat.add_product(i, f"Title {i}", 5)
    
    c = Cart(cat)
    for _ in range(100):
        for i in range(100):
            c.add(i)
            
    assert len(c.items) == 10000
    
    # Calculate total 5 times to execute dense iteration loops
    for _ in range(5):
        _ = c.total()