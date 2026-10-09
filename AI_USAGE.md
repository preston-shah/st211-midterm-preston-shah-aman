# AI Usage Audit & Reflection

Author: Preston Shah AMAN (6705142025)

---

## 1. Audit Table

| Date | Phase / Task | Prompt / Intent | AI Assistance Provided | Accuracy & Changes Made |
| :--- | :--- | :--- | :--- | :--- |
| Oct 9, 2026 | Phase 1 & 2: Environment Setup & Isolation | Prompted for commands to set up `.venv` and git worktree isolation. | Generated exact PowerShell commands for virtual environment creation, package installation, git branching (`draft`), and `bookstore_original` worktree setup. | 100% accurate. Commands executed directly in PowerShell without modification. |
| Oct 9, 2026 | Phase 3: Smoke Tests | Requested smoke test implementations covering core module functionality. | Drafted 5 `@pytest.mark.smoke` tests verifying registration, login, catalog addition, cart addition, and checkout. | Accurate logic. Added required author docstrings to satisfy project guidelines. |
| Oct 9, 2026 | Phase 4: Slow Tests | Requested 2 slow tests measuring system performance on large data volumes. | Provided `test_slow_bulk_product_import` (20,000 imports) and `test_slow_large_cart_repeated_total_calculation` (10,000 cart items). | Accurate performance test design. Executed and marked with `@pytest.mark.slow`. |
| Oct 9, 2026 | Phase 5: Regression & TDD Workflow | Requested step-by-step TDD cycle guidance for bugs across `cart.py`, `users.py`, and `catalog.py`. | Identified bug root causes, generated failing regression tests, provided precise code fixes, and supplied git commit messages. | High accuracy. Resolved minor indentation errors during file pasting in `test_bookstore.py`. |
| Oct 9, 2026 | Phase 6: Documentation | Asked to draft `FINDINGS.md` based on observed test assertion failures. | Structured findings with Suspected, Tried, Observed, Expected, and Fixed sections using exact failure traces. | Refined tone to sound natural while retaining exact failure output like `assert 10 == 30`. |

---

## 2. Reflections

### Where AI Was Most Helpful
- **Command & Workflow Speed:** AI accelerated administrative tasks by providing ready-to-run PowerShell commands for virtual environment management, git worktree creation, and targeted pytest execution flags (`-m smoke`, `-m regression`).
- **TDD Pattern Structure:** AI ensured strict adherence to the Red-Green-Refactor TDD cycle by keeping test generation, bug verification, and code fixes clearly isolated across individual commits.
- **Root Cause Isolation:** AI quickly pinpointed logic oversights in the original codebase, such as the `range(len(self.items) - 1)` boundary flaw in `Cart.total()` and the `isalnum()` filtering issue in `Users.login()`.

### Where Human Oversight & Judgment Were Required
- **Syntax & Indentation Corrections:** When pasting generated code blocks into VS Code, indentation issues occasionally caused `IndentationError` collection failures in pytest. Manual inspection and correction of file indentation were essential to fix these errors.
- **Independent Verification:** Before accepting AI-generated fixes, tests had to be executed locally against both the `draft` working branch and the unmodified `bookstore_original` worktree to guarantee that regression tests failed properly on original code and passed on fixed code.
- **Context Management:** Ensuring that pytest markers (`@pytest.mark.smoke`, `@pytest.mark.regression`, `@pytest.mark.slow`) and docstring standards strictly matched course grading requirements required deliberate review of AI outputs.
--------------------------------------------
I LOST SOME HAIR LINE
-------------------------------------------