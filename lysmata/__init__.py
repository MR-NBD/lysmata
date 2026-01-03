"""
Lysmata - Smart Contract Fuzzer for Solidity

A Python-based automated testing tool designed to find bugs and invariant
violations in Ethereum smart contracts through property-based testing and fuzzing.
"""

__version__ = "0.1.0"
__author__ = "Your Name"
__license__ = "MIT"

from .main import fuzz, main

__all__ = ["fuzz", "main"]
