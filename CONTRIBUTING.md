# Contributing to Lysmata

Thank you for considering contributing to Lysmata! This document provides guidelines and instructions for contributing.

## How to Contribute

### Reporting Bugs

If you find a bug, please open an issue on GitHub with:
- A clear, descriptive title
- Detailed steps to reproduce the issue
- Expected vs actual behavior
- Your environment (OS, Python version, etc.)
- Relevant code samples or error messages

### Suggesting Enhancements

Enhancement suggestions are welcome! Please open an issue with:
- A clear description of the enhancement
- Use cases and benefits
- Potential implementation approach (if you have ideas)

### Pull Requests

1. **Fork the repository** and create your branch from `main`
2. **Make your changes**:
   - Write clear, documented code
   - Follow the existing code style
   - Add tests if applicable
3. **Test your changes**:
   - Ensure all tests pass
   - Test with example contracts in `tests/`
4. **Commit your changes**:
   - Use clear, descriptive commit messages
   - Reference issues if applicable (e.g., "Fixes #123")
5. **Push to your fork** and submit a pull request

## Development Setup

### Prerequisites
- Python 3.8, 3.9, or 3.10
- Git
- Foundry (for Anvil)

### Local Setup

```bash
# Clone your fork
git clone https://github.com/yourusername/lysmata.git
cd lysmata

# Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
pip install -e .  # Install in editable mode

# Install development dependencies
pip install pytest pytest-cov black isort flake8

# Install solc
solc-select install 0.8.19
solc-select use 0.8.19
```

### Running Tests

```bash
# Run basic test
python3 lysmata-cli.py -r 100 -s 50 -c tests/invariant_breaker.sol

# Test all example contracts
for contract in tests/*.sol; do
    echo "Testing $contract..."
    python3 lysmata-cli.py -r 50 -s 30 -c "$contract"
done
```

### Code Style

This project follows PEP 8 style guidelines:

```bash
# Format code with black
black lysmata/

# Sort imports with isort
isort lysmata/

# Check for issues with flake8
flake8 lysmata/
```

## Code Structure

```
lysmata/
├── __init__.py       # Package initialization
├── main.py           # Main fuzzing orchestrator
├── abi.py            # ABI extraction from compiled contracts
├── strategy.py       # Hypothesis strategy generation
├── utils.py          # Constants mining and utilities
├── anvil_setup.py    # Anvil test node management
├── stampa.py         # ASCII art output
└── write_txt.py      # Test result file writing
```

## Coding Guidelines

### Python Code

- Use type hints where appropriate
- Write docstrings for functions and classes
- Keep functions focused and modular
- Handle errors gracefully
- Use meaningful variable and function names

Example:
```python
def extract_constants(bytecode: str, param_type: str) -> List[str]:
    """
    Extract hardcoded constants from contract bytecode.

    Args:
        bytecode: Contract bytecode as hex string
        param_type: Solidity type to extract (uint, address, etc.)

    Returns:
        List of extracted constant values
    """
    # Implementation...
```

### Solidity Test Contracts

- Use clear, descriptive names
- Document expected behavior
- Include both passing and failing scenarios
- Keep examples simple and focused

## Areas for Contribution

### High Priority
- Support for payable functions with Ether transfers
- Multi-account transaction generation
- Extended constants mining (bytes, arrays, structs)
- Better handling of name collisions

### Medium Priority
- Integration with other testing frameworks
- Performance optimizations
- Better error messages and debugging
- Documentation improvements

### Nice to Have
- Web-based dashboard for results
- Additional fuzzing strategies
- More example contracts
- Tutorial videos or guides

## Testing Your Contributions

Before submitting a PR, ensure:

1. **Code runs without errors**:
   ```bash
   python3 lysmata-cli.py -r 100 -s 50 -c tests/invariant_breaker.sol
   ```

2. **Code follows style guidelines**:
   ```bash
   black --check lysmata/
   flake8 lysmata/
   ```

3. **No regressions**: Test with existing example contracts

4. **New features are documented**: Update README.md if needed

## Questions?

If you have questions about contributing:
- Open a GitHub issue with the "question" label
- Check existing issues and discussions
- Review the README.md and code documentation

## License

By contributing, you agree that your contributions will be licensed under the MIT License.

Thank you for helping make Lysmata better!
