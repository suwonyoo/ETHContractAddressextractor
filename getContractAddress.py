import json
import urllib.request
from collections import OrderedDict

# Info
'''
WyvernV1 : 0x7be8076f4ea4a4ad08075c2508e481d6c946d12b | 0xab834bab
WyvernV2 : 0x7f268357A8c2552623316e2562D90e642bB538E5 | 0xab834bab
OpenseaSeaport : 0x00000000006c3852cbef3e08e8df289169ede581 | 0xfb0f3ee1
'''

WyvernV1 = {'contractname': 'WyvernV1', 'target_methodID': '0xab834bab', 'contractaddress' : '0x7be8076f4ea4a4ad08075c2508e481d6c946d12b'}
WyvernV2 = {'contractname': 'WyvernV2', 'target_methodID': '0xab834bab', 'contractaddress' : '0x7f268357A8c2552623316e2562D90e642bB538E5'}
OpenseaSeaport = {'contractname': 'OpenseaSeaport', 'target_methodID': '0xfb0f3ee1', 'contractaddress' : '0x00000000006c3852cbef3e08e8df289169ede581'}

# get timestamp and NFT contract address of Wyvern1 Contract
def getDataofWyvern1(contractname, target_methodID, contractaddress, offset):
    # initial setting
    api_keys = ''
    startblock = 0
    endblock = 999999999
    jsondata = OrderedDict()
    jsondata["NFTdata"] = list()
    filenum = 0
    
    # except case should be shown by IndexError
    while 1:
        # initialize data
        num_count = 0
        currentindex = 0 
        

        # update url by endblock
        url_setting = 'https://api.etherscan.io/api?module=account&action=txlist&address='+str(contractaddress)+'&startblock='+str(startblock)+'&endblock='+str(endblock)+'&page=1&offset='+str(offset)+'&sort=asc&apikey='+str(api_keys)
        url_input = str(url_setting)
        print(url_input)


        # save raw data by using etherscan.api
        with urllib.request.urlopen(url_input) as url:
            data = json.loads(url.read().decode())
            # classfiy by methodId
            while num_count<offset:
                if data["result"][currentindex]['methodId'] == target_methodID and data["result"][currentindex]['isError'] == str(0):
                    selecteddata = {"timestamp" : data["result"][currentindex]['timeStamp'], "nftContractAddress" : '0x'+data["result"][currentindex]['input'][290:330]}
                    jsondata["NFTdata"].append(selecteddata)
                num_count = num_count + 1
                currentindex = currentindex + 1
            startblock = data["result"][offset-1]['blockNumber']

            # write json file
            with open('./'+str(contractname)+'/output_'+str(contractname)+'_'+str(filenum)+'.json', 'w') as f:
                json.dump(jsondata, f, indent=4)
        filenum = filenum + 1

# get timestamp and NFT contract address of Wyvern2 Contract
def getDataofWyvern2(contractname, target_methodID, contractaddress, offset):
    # initial setting
    api_keys = ''
    startblock = 0
    endblock = 999999999
    jsondata = OrderedDict()
    jsondata["NFTdata"] = list()
    filenum = 0

    # except case should be shown by IndexError
    while 1:
        # initialize data
        num_count = 0
        currentindex = 0
    

        # update url by endblock
        url_setting = 'https://api.etherscan.io/api?module=account&action=txlist&address='+str(contractaddress)+'&startblock='+str(startblock)+'&endblock='+str(endblock)+'&page=1&offset='+str(offset)+'&sort=asc&apikey='+str(api_keys)
        url_input = str(url_setting)
        print(url_input)


        # save raw data by using etherscan.api
        with urllib.request.urlopen(url_input) as url:
            data = json.loads(url.read().decode())
            # classfiy by methodId
            while num_count<offset:
                if data["result"][currentindex]['methodId'] == target_methodID and data["result"][currentindex]['isError'] == str(0):
                    selecteddata = {"timestamp" : data["result"][currentindex]['timeStamp'], "nftContractAddress" : '0x'+data["result"][currentindex]['input'][3626:3666]}
                    jsondata["NFTdata"].append(selecteddata)
                num_count = num_count + 1
                currentindex = currentindex + 1
            startblock = data["result"][offset-1]['blockNumber']

            # write json file
            with open('./'+str(contractname)+'/output_'+str(contractname)+'_'+str(filenum)+'.json', 'w') as f:
                json.dump(jsondata, f, indent=4)
     filenum = filenum + 1

# get timestamp and NFT contract address of Seaport Contract
def getDataofSeaport(contractname, target_methodID, contractaddress, offset):
    # initial setting
    api_keys = ''
    startblock = 0
    endblock = 999999999
    jsondata = OrderedDict()
    jsondata["NFTdata"] = list()
    filenum = 0

    # except case should be shown by IndexError
    while 1:
        # initialize data
        num_count = 0
        currentindex = 0

        # update url by endblock
        url_setting = 'https://api.etherscan.io/api?module=account&action=txlist&address='+str(contractaddress)+'&startblock='+str(startblock)+'&endblock='+str(endblock)+'&page=1&offset='+str(offset)+'&sort=asc&apikey='+str(api_keys)
        url_input = str(url_setting)
        print(url_input)

        # save raw data by using etherscan.api
        with urllib.request.urlopen(url_input) as url:
            data = json.loads(url.read().decode())
            # classfiy by methodId
            while num_count<offset:
                if data["result"][currentindex]['methodId'] == target_methodID and data["result"][currentindex]['isError'] == str(0):
                    selecteddata = {"timestamp" : data["result"][currentindex]['timeStamp'], "nftContractAddress" : '0x'+data["result"][currentindex]['input'][418:458]}
                    jsondata["NFTdata"].append(selecteddata)
                num_count = num_count + 1
                currentindex = currentindex + 1
            startblock = data["result"][offset-1]['blockNumber']

            # write json file
            with open('./'+str(contractname)+'/output_'+str(contractname)+'_'+str(filenum)+'.json', 'w') as f:
                json.dump(jsondata, f, indent=4)
        filenum = filenum + 1
try:
    getDataofWyvern1(WyvernV1.get('contractname'), WyvernV1.get('target_methodID'), WyvernV1.get('contractaddress'), 10000)
except IndexError :
    getDataofWyvern2(WyvernV2.get('contractname'), WyvernV2.get('target_methodID'), WyvernV2.get('contractaddress'), 10000)
