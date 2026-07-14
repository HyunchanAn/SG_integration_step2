# Benchmark & E2E Test Report

- **Repository**: SG_integration_step2
- **Date**: 2026-07-14 22:41:30

## 1. E2E Testing Summary
❌ **Status**: FAILED

### Test Logs (Snippet)
```text
platform darwin -- Python 3.13.9, pytest-9.0.3, pluggy-1.5.0
rootdir: /Users/hyunchanan/Documents/GitHub/SG_integration_step2
configfile: pyproject.toml
plugins: anyio-4.12.1, cov-7.1.0, hypothesis-6.155.7, hydra-core-1.3.2, respx-0.23.1
collected 8 items / 2 errors

==================================== ERRORS ====================================
_______________ ERROR collecting SG_proj_004/tests/test_main.py ________________
ImportError while importing test module '/Users/hyunchanan/Documents/GitHub/SG_integration_step2/SG_proj_004/tests/test_main.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/opt/homebrew/Caskroom/miniconda/base/lib/python3.13/importlib/__init__.py:88: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
SG_proj_004/tests/test_main.py:5: in <module>
    from src.database import get_db, Base
E   ModuleNotFoundError: No module named 'src.database'
_______________ ERROR collecting SG_proj_012/tests/test_main.py ________________
import file mismatch:
imported module 'test_main' has this __file__ attribute:
  /Users/hyunchanan/Documents/GitHub/SG_integration_step2/SG_proj_010/tests/test_main.py
which is not the same as the test file we want to collect:
  /Users/hyunchanan/Documents/GitHub/SG_integration_step2/SG_proj_012/tests/test_main.py
HINT: remove __pycache__ / .pyc files and/or use a unique basename for your test file modules
=========================== short test summary info ============================
ERROR SG_proj_004/tests/test_main.py
ERROR SG_proj_012/tests/test_main.py
!!!!!!!!!!!!!!!!!!! Interrupted: 2 errors during collection !!!!!!!!!!!!!!!!!!!!
============================== 2 errors in 14.59s ==============================

```

## 2. Models Detected
- No pre-trained weights or models detected in this repository.
