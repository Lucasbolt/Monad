from web3 import Web3
from eth_account import Account
from dotenv import load_dotenv
from os import getenv

load_dotenv()
RPC_URL = getenv("RPC_ENDPOINT_URL")
NUMBER_OF_ACCOUNTS = 10
w3 = Web3(Web3.HTTPProvider(RPC_URL))
account = Account.create()

print(f"🔑 New account created: {account.address}"
      f"\n🔒 Private Key: {account.key.hex()}")
# The create() method generates a new private key and returns an Account object.
# The address and private key are then printed to the console.

account1 = w3.eth.account.create()
print(f"🔑 New account created: {account1.address}"
      f"\n🔒 Private Key: {account1.key.hex()}")

def create_account(number_of_accounts=NUMBER_OF_ACCOUNTS):
    with open("private_keys.txt", "w") as f:
        for _ in range(number_of_accounts):
            account = w3.eth.account.create()
            f.write(f"0x{account.key.hex()}\n")
            print(f"🔑 New account created: {account.address}"
                  f"\n🔒 Private Key: {account.key.hex()}")

if __name__ == "__main__":
    create_account()
