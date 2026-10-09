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