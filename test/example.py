import unittest
import os
import near_api
import logging
import sys
from config import NODE_URL

logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
class AccountTest(unittest.TestCase):
  

    def setUp(self):
        self.provider = near_api.providers.JsonProvider(NODE_URL)
        self.signer =  near_api.signer.Signer.from_json_file(os.path.expanduser('~/.near-credentials/testnet/your-account-id.testnet.json'))
        self.master_account = near_api.account.Account(self.provider, self.signer, "your-account-id.testnet")
       

    def runTest(self):
        log = logging.getLogger("TestLog")

        # Get the balance of the account. Contract is a simple FT deployed at dev-1625827077759-82654722336619
        view_tx_res = self.master_account.view_function('dev-1625827077759-82654722336619', 'ft_balance_of', {"account_id": "ako4irelabs.testnet"})
        
        log.debug(view_tx_res.keys())
        log.debug(view_tx_res['result'])

        call_tx_res = self.master_account.function_call('dev-1625827077759-82654722336619', 'mint', {"account_id": "ako4irelabs.testnet", "amount": 100})
        log.debug(call_tx_res.keys())
        log.debug(call_tx_res['transaction_outcome'])
        
        view_tx_res = self.master_account.view_function('dev-1625827077759-82654722336619', 'ft_balance_of', {"account_id": "ako4irelabs.testnet"})
        log.debug(view_tx_res['result'])


unittest.TextTestRunner().run(AccountTest())