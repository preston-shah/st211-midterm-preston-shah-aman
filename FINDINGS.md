# ST211 Bookstore Bug Findings

Author: Preston Shah aman (6705142025)

---

## Finding 1: Off-by-one loop in Cart.total omits final item

- **Suspected:** Looking at `Cart.total()`, it seemed like the calculation was stopping short and missing the last item added to the cart because of how the loop range was set up.
- **Tried:** Added two items (\$10 and \$20) to a new cart, called `c.total()`, and asserted that the total should be `30`.
- **Observed:** The test failed with `AssertionError: assert 10 == 30` (where `10 = total()`). It only counted the first \$10 item and skipped the \$20 item.
- **Expected:** `c.total()` should return `30`.
- **Fixed:** Updated `for i in range(len(self.items) - 1):` to `for pid in self.items:` in `bookstore_app/cart.py` so it iterates through every item.

---

## Finding 2: Cart.import_products overcounts imported items by 1

- **Suspected:** `Cart.import_products()` was incrementing a counter for each product added, but returning `count + 1` for some reason, artificially bumping up the result.
- **Tried:** Passed a list of 2 product tuples `[(1, "Book A", 10), (2, "Book B", 15)]` into `c.import_products()` and checked if the returned count matched 2.
- **Observed:** The test failed with `AssertionError: assert 3 == 2` (where `3 = import_products(...)`).
- **Expected:** `c.import_products()` should return `2`.
- **Fixed:** Changed `return count + 1` to `return count` in `bookstore_app/cart.py`.

---

## Finding 3: Cart.checkout on empty cart returns empty list instead of None

- **Suspected:** `Cart.checkout()` didn't check if the cart had any items before running, which meant checking out an empty cart returned `[]` and saved an empty order to history instead of returning `None`.
- **Tried:** Created an empty cart, immediately called `c.checkout()`, and checked if the result was `None` and order history remained empty.
- **Observed:** The test failed with `AssertionError: assert [] is None`.
- **Expected:** `c.checkout()` should return `None` and leave `c.history()` as `[]`.
- **Fixed:** Added an explicit check `if not self.items: return None` at the start of `checkout()` in `bookstore_app/cart.py`.

---

## Finding 4: Users.login strips non-alphanumeric characters from supplied password

- **Suspected:** `Users.login()` was using `isalnum()` to strip out special characters from the input password before checking it, which broke valid logins when passwords had punctuation.
- **Tried:** Registered a user `"preston"` with password `"secret!123"`, then tried logging in with the exact same password `"secret!123"`.
- **Observed:** The test failed with `AssertionError: assert False is True` (where `False = login('preston', 'secret!123')`).
- **Expected:** `u.login()` should return `True` when given the exact matching password.
- **Fixed:** Removed the character filtering loop and changed the return condition to `return stored is not None and stored == password` in `bookstore_app/users.py`.

---

## Finding 5: Catalog.search performs case-sensitive keyword matching

- **Suspected:** `Catalog.search()` was doing a direct `keyword in info["title"]` check, meaning any difference in letter casing caused search hits to be missed.
- **Tried:** Added a product titled `"Python Testing Guide"` (ID 1) to the catalog and searched for the lowercase keyword `"python"`.
- **Observed:** The test failed with `AssertionError: assert [] == [1]`.
- **Expected:** `cat.search("python")` should return `[1]`.
- **Fixed:** Lowercased both sides of the comparison in `bookstore_app/catalog.py`: `if keyword.lower() in info["title"].lower():`.

-----------------------------------------------------------------------
TRUST ME GANG I LOST SOME HAIR LINE FINDING THESE.
-----------------------------------------------------------------------