import os
import json
from typing import List, Dict # https://docs.python.org/3/library/typing.html


def get_functions(test_file_name) -> (List, Dict):
    funzione = {}
    contract_set = set()

    with open(f"crytic-export/{test_file_name.split('/')[-1]}.json") as crytic_out:
        out_info = json.load(crytic_out)
        unit = list(out_info["compilation_units"].keys())[0]

        contracts = out_info["compilation_units"][unit]["contracts"][unit]
        contract_names = list(contracts.keys())

        for contratto in contracts:
            contract_set.add(contratto)
            funzione[contratto] = [
                data
                for data in contracts[contratto]["abi"]
                if data["type"] == "function"
                and data["stateMutability"] != "view"
                and data["stateMutability"] != "pure"
            ]

            # If the internalType of an input starts with `contract` we should save it,
            # and look for it in the other abis, then deduce which functions are available to us

    return (contract_names, funzione)


def get_abi_and_bytecode(test_file_name):
    abi = {}
    bytecode = {}
    contract_set = set()

    with open(f"crytic-export/{test_file_name.split('/')[-1]}.json") as crytic_out:
        out_info = json.load(crytic_out)
        unit = list(out_info["compilation_units"].keys())[0]

        contracts = out_info["compilation_units"][unit]["contracts"][unit]
        contract_names = list(contracts.keys())

        for contratto in contracts:
            contract_set.add(contratto)
            abi[contratto] = contracts[contratto]["abi"]
            bytecode[contratto] = contracts[contratto]["bin"]

    return (abi, bytecode)


def get_abi_by_name(contract_name, test_file_name):
    abi = {}

    with open(f"crytic-export/{test_file_name.split('/')[-1]}.json") as crytic_out:
        out_info = json.load(crytic_out)
        unit = list(out_info["compilation_units"].keys())[0]
        contracts = out_info["compilation_units"][unit]["contracts"][unit]

    return contracts[contract_name]["abi"]
