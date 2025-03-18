from web3 import Web3
from apscheduler.schedulers.blocking import BlockingScheduler
import time

# Monad Testnet RPC URL
RPC_URL = "https://testnet-rpc.monad.xyz" # Replace with actual RPC URL

# Faucet contract details
FAUCET_CONTRACT = "0x09fb6a39471eb9dcee30fb91d8830195b1380e0f"  # Replace with actual faucet contract
CLAIM_FUNCTION_SIG = "0x7bfc2741"  # Replace with actual function signature

# Private keys for 20 accounts
private_keys = [
    "0xfe74a09c16f6ffd8876c2dd74f118c5571553cf984b56d4e3841ef3181f7f0f6",
    "0x0d6477560b3dded4b0f45eb9234748d7a61d26ebefb9382e21a68812bdf29eb3",
]

# Connect to the Monad Testnet
w3 = Web3(Web3.HTTPProvider(RPC_URL))

def claim_faucet(private_key):
    try:
        account = w3.eth.account.from_key(private_key)
        nonce = w3.eth.get_transaction_count(account.address)
        
        tx = {
            "to": FAUCET_CONTRACT,
            "data": CLAIM_FUNCTION_SIG,
            "gas": 500000,  # Adjust based on actual gas usage
            "gasPrice": w3.to_wei("100", "gwei"),  # Adjust if needed
            "nonce": nonce,
        }

        signed_tx = w3.eth.account.sign_transaction(tx, private_key)
        tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
        print(f"Transaction sent for {account.address}: {tx_hash.hex()}")
        
        receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
        print(f"Transaction confirmed for {account.address}: {receipt.status}")
    except Exception as e:
        print(f"Error claiming for {account.address}: {e}")

def run_claiming():
    print("Starting faucet claims...")
    for key in private_keys:
        claim_faucet(key)
        time.sleep(2)  # Small delay to avoid nonce issues

# Schedule to run every 12 hours
scheduler = BlockingScheduler()
scheduler.add_job(run_claiming, "interval", hours=12)

# Run immediately on script start
run_claiming()

print("Scheduled claiming every 12 hours...")
scheduler.start()
