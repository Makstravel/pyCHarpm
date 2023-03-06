import os
import random
import string
from web3 import Web3
from web3.auto import w3
from web3.middleware import geth_poa_middleware
from bip_utils import Bip39MnemonicGenerator, Bip44, Bip44Coins, Bip44Changes

class MetamaskWallet:
    def __init__(self, num_wallets, file_name):
        self.num_wallets = num_wallets
        self.file_name = file_name
        self.wallets = []
        self.create_wallets()

    def create_wallets(self):
        # Enable middleware for POA network
        w3.middleware_onion.inject(geth_poa_middleware, layer=0)

        # Generate random mnemonic for each wallet
        for i in range(self.num_wallets):
            mnemonic = Bip39MnemonicGenerator().Generate()
            wallet = self.get_wallet(mnemonic)
            self.wallets.append(wallet)

    def get_wallet(self, mnemonic):
        # Create seed from mnemonic
        seed_bytes = Bip39MnemonicGenerator.ToSeed(mnemonic)
        seed_hex = seed_bytes.hex()

        # Create wallet from seed
        bip44_account = Bip44.FromSeed(seed_bytes).Purpose().Coin(Bip44Coins.ETH).Account(0)
        private_key_bytes = bip44_account.Change(Bip44Changes.CHAIN_EXT).PrivateKey().Raw().ToBytes()
        private_key_hex = private_key_bytes.hex()
        address = w3.eth.account.from_key(private_key_bytes).address

        # Save mnemonic, private key, and address to file
        with open(self.file_name, 'a') as f:
            f.write(f'Mnemonic: {mnemonic}\n')
            f.write(f'Private Key: {private_key_hex}\n')
            f.write(f'Address: {address}\n\n')

        # Return wallet object
        return {'mnemonic': mnemonic, 'private_key': private_key_hex, 'address': address}


# Example usage
num_wallets = 10
file_name = 'metamask_wallets.txt'
wallet = MetamaskWallet(num_wallets, file_name)
print(wallet.wallets)
