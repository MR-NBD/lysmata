# Lysmata

**Lysmata** is a powerful smart contract fuzzer for Solidity, designed to automatically discover bugs and invariant violations in Ethereum smart contracts through advanced property-based testing and fuzzing techniques.

## Features

- **Stateful Fuzzing**: Generates sequences of transactions to test complex state transitions
- **Invariant Testing**: Automatically validates user-defined contract invariants
- **Coverage Guidance**: Steers fuzzing towards unexplored code paths for deeper testing
- **Constants Mining**: Extracts hardcoded values from bytecode to generate more effective test inputs
- **Swarm Testing**: Creates diverse test sequences by randomly selecting function subsets
- **Automatic Shrinking**: Minimizes failing test cases to simplest reproducible examples
- **Long Sequence Preference**: Biases generation toward longer transaction sequences to find complex bugs

## Installation

### Prerequisites

- Python 3.8, 3.9, or 3.10
- [Foundry](https://github.com/foundry-rs/foundry) (for Anvil test node)

### Setup

1. **Clone the repository**:
```bash
git clone https://github.com/yourusername/lysmata.git
cd lysmata
```

2. **Install Python dependencies**:
```bash
pip install -r requirements.txt
```

3. **Install and activate Solidity compiler**:
```bash
solc-select install 0.8.19
solc-select use 0.8.19
```

4. **Install Foundry** (if not already installed):
```bash
curl -L https://foundry.paradigm.xyz | bash
```

Then, in a new terminal (to update `PATH`):
```bash
foundryup
```

## Usage

### Basic Usage

Run the fuzzer on a Solidity contract:

```bash
python3 lysmata-cli.py -r 1000 -s 100 -c tests/invariant_breaker.sol
```

**Parameters**:
- `-r, --run`: Number of transaction sequences to generate (default: 1000)
- `-s, --sequence`: Maximum transactions per sequence (default: 100)
- `-c, --contract`: Path to the Solidity contract to test

### Writing Test Contracts

To use Lysmata, your Solidity contract should include:

1. **Invariant functions**: Functions starting with `invariant_` that return a boolean
2. **Optional setUp function**: For contract initialization

**Example**:

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.19;

contract MyContract {
    uint256 public balance;

    function setUp() public {
        balance = 0;
    }

    function deposit(uint256 amount) public {
        balance += amount;
    }

    function withdraw(uint256 amount) public {
        require(balance >= amount, "Insufficient balance");
        balance -= amount;
    }

    // Invariant: balance should never be negative
    function invariant_balanceNonNegative() public view returns (bool) {
        return balance >= 0;
    }
}
```

### Test Examples

The `tests/` directory contains example contracts demonstrating various features:

- **invariant_breaker.sol**: Example showing invariant violation detection
- **constants_test.sol**: Tests the constants mining feature
- **coverage_test.sol**: Demonstrates coverage-guided fuzzing
- **swarm_test.sol**: Example of swarm testing capabilities

## Configuration

Advanced configuration options are available in `config.yaml`:

```yaml
fuzz_runs: 1000          # Number of test sequences
seq_len: 100             # Maximum transactions per sequence
shrinking: true          # Enable test case minimization
swarm_testing: true      # Enable function subset selection
coverage_guidance: true  # Enable coverage-guided fuzzing
constants_mining: true   # Extract hardcoded values
favor_long_sequence: true  # Bias toward longer sequences
anvil_port: 8545        # Local test node port
```

## How It Works

1. **Compilation**: Contracts are compiled with `crytic-compile` to extract ABIs and bytecode
2. **Setup**: Anvil test node is started and contracts are deployed
3. **Test Generation**: Hypothesis generates sequences of function calls using:
   - Random function selection (with swarm testing bias)
   - Type-based argument generation strategies
   - Extracted constants from contract bytecode
4. **Execution**: Each transaction sequence is executed on the test node with:
   - State snapshots for sequence isolation
   - Coverage tracking for guidance
   - Invariant assertions after each transaction
5. **Reporting**: Failures are reported with shrunk examples showing minimal reproducers

## Architecture

```
Lysmata/
├── lysmata/              # Main package
│   ├── __init__.py       # Package initialization
│   ├── main.py           # Fuzzing orchestrator
│   ├── abi.py            # ABI and bytecode extraction
│   ├── strategy.py       # Hypothesis strategy generation
│   ├── utils.py          # Constants mining utilities
│   ├── anvil_setup.py    # Anvil test node management
│   ├── stampa.py         # ASCII art branding
│   └── write_txt.py      # Test result file output
├── tests/                # Example test contracts
├── output/               # Test results (generated)
├── lysmata-cli.py        # Command-line interface
├── config.yaml           # Configuration file
├── requirements.txt      # Python dependencies
└── README.md            # This file
```

## Roadmap

Future improvements planned for Lysmata:

- [ ] Support for payable functions with Ether transfers
- [ ] Multi-account transaction generation
- [ ] Extended constants mining for bytes, arrays, and structs
- [ ] Better handling of contracts/functions with identical names
- [ ] Integration with popular testing frameworks
- [ ] Web-based dashboard for test results

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Built on [Hypothesis](https://hypothesis.readthedocs.io/) for property-based testing
- Uses [Slither](https://github.com/crytic/slither) for static analysis
- Powered by [Foundry's Anvil](https://github.com/foundry-rs/foundry) for local testing
- Inspired by the work of Trail of Bits and other smart contract security tools

## Support

For questions, issues, or feature requests, please open an issue on GitHub.

---

**Note**: Lysmata is a testing tool and should be used as part of a comprehensive smart contract security audit. It does not guarantee the absence of bugs or vulnerabilities.
