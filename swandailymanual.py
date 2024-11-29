from web3 import Web3, HTTPProvider
import requests
import json
import time
from eth_account import Account
from eth_account.messages import encode_defunct
from requests_toolbelt import MultipartEncoder

# List of RPC endpoints to try
rpc_endpoints = [
    "https://mainnet-rpc-01.swanchain.org",
    "https://mainnet-rpc-02.swanchain.org",
    "https://mainnet-rpc-03.swanchain.org",
    "https://mainnet-rpc-04.swanchain.org",
    "https://rpc-swan-tp.nebulablock.com"
]

def connect_web3():
    for rpc_url in rpc_endpoints:
        try:
            print(f"Attempting to connect to RPC: {rpc_url}")
            web3 = Web3(Web3.HTTPProvider(rpc_url))
            
            # Check if the connection is successful
            if web3.is_connected():
                print(f"Successfully connected to RPC: {rpc_url}\n")
                return web3
            else:
                print(f"Failed to connect to RPC: {rpc_url}\n")
        except (Exception, TimeoutError) as e:
            print(f"Error connecting to RPC: {rpc_url}. Error: {e}\n")
        
        # Wait a bit before trying the next RPC
        time.sleep(2)
    
    # If none of the RPCs connect, raise an error
    print("Unable to connect to any RPC endpoint. Please check your network or RPC servers.\n")
    exit()

web3 = connect_web3()
chainId = web3.eth.chain_id

#connecting web3
if  web3.is_connected() == True:
    print("Web3 Connected...\n")
else:
    print("Error Connecting Please Try Again...")
    exit()

print(f'Daily Combo, Checkin & Mint Swan OnChain | @ylasgamers')
senderkey = input('Input Privatekey EVM Swanchain : ')
authtoken = input('Input Auth Token Bearer eyJhb... : ')
target = web3.to_checksum_address('0xb5117C0CFfAA789186291483b9a5B7F69bB6575A')
target2 = web3.to_checksum_address('0x558772Da528b7378823D934130969FaC07C5d655')

def DailyMintWeb(token):
    url = "https://campaign-api.swanchain.io/task/xp_completion_verification"
    
    m = MultipartEncoder(fields={'task_id': '2'})
    headers = {
        'Content-Type': m.content_type,
        'Origin': 'https://mission.swanchain.io',
        'Referer': 'https://mission.swanchain.io/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:109.0) Gecko/20100101 Firefox/115.0'
    }
    
    headers['Authorization'] = f'Bearer {token}'

    response = requests.post(url, data=m, headers=headers)
    print(f'Create xp task verification request process...')
    result = response.json()
    status = result.get('status')
    msg = result.get('message')
    if 200 == status:
        print(f'{msg}')
        print(f'Wait For 5 Second To Prevent Fail')
        print(f'-------------------------------------------')
        time.sleep(5)
    else:
        print(f'Verification request fail! Exit...')
        exit()

def DailyCheckWeb(sender, key, token, txhash1):
    url = "https://campaign-api.swanchain.io/task/xp_completion_verification"
    
    m = MultipartEncoder(fields={'task_id': '1', 'proof': txhash1})
    headers = {
        'Content-Type': m.content_type,
        'Origin': 'https://mission.swanchain.io',
        'Referer': 'https://mission.swanchain.io/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:109.0) Gecko/20100101 Firefox/115.0'
    }
    
    headers['Authorization'] = f'Bearer {token}'

    response = requests.post(url, data=m, headers=headers)
    print(f'Create xp task verification request process...')
    result = response.json()
    status = result.get('status')
    msg = result.get('message')
    if 200 == status:
        print(f'{msg}')
        print(f'Wait For 5 Second To Prevent Fail')
        print(f'-------------------------------------------')
        time.sleep(5)
        DailyMintWeb(token)
    else:
        print(f'Verification request fail! Exit...')
        exit()

def DailyMint(sender, key, token, txhash1):
    try:
        gasPrice = web3.to_wei(0.000001, 'gwei')
        nonce = web3.eth.get_transaction_count(sender)

        gasAmount = web3.eth.estimate_gas({
            'chainId': chainId,
            'from': sender,
            'to': target2,
            'data': '0x7b996fd6'
        })

        dailymint_tx = {
            'chainId': chainId,
            'from': sender,
            'to': target2,
            'gas': gasAmount,
            'gasPrice': gasPrice,
            'data': '0x7b996fd6',
            'nonce': nonce
        }
        raw_tx = web3.eth.account.sign_transaction(dailymint_tx, key).rawTransaction
        #sign & send the transaction
        tx_hash = web3.eth.send_raw_transaction(raw_tx)
        #wait for transaction
        print(f'Wait For Transaction Until Mined...')
        transaction_receipt = web3.eth.wait_for_transaction_receipt(tx_hash)
        #get transaction hash
        print(f'Daily Mint OnChain Success!')
        print(f'TX-ID : {str(web3.to_hex(tx_hash))}')
        print(f'Wait For 5 Second To Prevent Fail')
        print(f'-------------------------------------------')
        time.sleep(5)
        DailyCheckWeb(sender, key, token, txhash1)
    except Exception as e:
        print(f"Error: {e}")
        pass

def DailyCheck(sender, key, token):
    try:
        gasPrice = web3.to_wei(0.000001, 'gwei')
        nonce = web3.eth.get_transaction_count(sender)

        gasAmount = web3.eth.estimate_gas({
            'chainId': chainId,
            'from': sender,
            'to': target,
            'data': '0x183ff085'
        })

        daily_tx = {
            'chainId': chainId,
            'from': sender,
            'to': target,
            'gas': gasAmount,
            'gasPrice': gasPrice,
            'data': '0x183ff085',
            'nonce': nonce
        }
        raw_tx = web3.eth.account.sign_transaction(daily_tx, key).rawTransaction
        #sign & send the transaction
        tx_hash = web3.eth.send_raw_transaction(raw_tx)
        #wait for transaction
        print(f'Wait For Transaction Until Mined...')
        transaction_receipt = web3.eth.wait_for_transaction_receipt(tx_hash)
        #get transaction hash
        print(f'Daily Checkin OnChain Success!')
        print(f'TX-ID : {str(web3.to_hex(tx_hash))}')
        print(f'Wait For 5 Second To Prevent Fail')
        print(f'-------------------------------------------')
        time.sleep(5)
        DailyMint(sender, key, token, str(web3.to_hex(tx_hash)))
    except Exception as e:
        print(f"Error: {e}")
        pass
        
def DailyCombo(sender, key, token):
    combo1 = str(input('Input Combo Number 1 : '))
    combo2 = str(input('Input Combo Number 2 : '))
    combo3 = str(input('Input Combo Number 3 : '))
    url = "https://campaign-api.swanchain.io/task/daily_combo"
    
    m = MultipartEncoder(fields={'number1': combo1, 'number2': combo2, 'number3': combo3})
    headers = {
        'Content-Type': m.content_type,
        'Origin': 'https://mission.swanchain.io',
        'Referer': 'https://mission.swanchain.io/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:109.0) Gecko/20100101 Firefox/115.0'
    }
    
    headers['Authorization'] = f'Bearer {token}'

    response = requests.post(url, data=m, headers=headers)
    print(f'Daily combo request process...')
    result = response.json()
    status = result.get('status')
    msg = result.get('message')
    if 200 == status:
        print(f'{msg}')
        print(f'Wait For 5 Second To Prevent Fail')
        print(f'-------------------------------------------')
        time.sleep(5)
        DailyCheck(sender, key, token)
    elif f'Already sumbited combo today.' == msg:
        print(f'{msg} Skipping...')
        print(f'Wait For 5 Second To Prevent Fail')
        print(f'-------------------------------------------')
        time.sleep(5)
        DailyCheck(sender, key, token)
    else:
        print(f'Verification request fail! Exit...')
        exit()

def WalletLogin():
    sender = Account.from_key(senderkey)
    DailyCombo(sender.address, senderkey, authtoken)

WalletLogin()
