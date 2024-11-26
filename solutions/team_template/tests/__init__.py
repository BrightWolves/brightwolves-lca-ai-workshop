# tests/__init__.py
"""Root test package initialization.

This package contains test suites for the LCA workshop implementation.
Tests are organized into:
- examples: Complete reference implementations
- exercises: Templates for student implementation
- helpers: Shared test utilities
"""

from pathlib import Path

# Useful constants for test modules
TEST_DIR = Path(__file__).parent
FIXTURES_DIR = TEST_DIR / "helpers" / "test_data"