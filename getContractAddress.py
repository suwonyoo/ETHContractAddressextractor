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
    filenum = 0
    jsondata = OrderedDict()

    while 1:
        # initialize data
        finalindex = 0
        currentindex = 0
        count = 0

        # update url by endblock
        url_setting = 'https://api.etherscan.io/api?module=account&action=txlist&address='+str(contractaddress)+'&startblock='+str(startblock)+'&endblock='+str(endblock)+'&page=1&offset='+str(offset)+'&sort=asc&apikey='+str(api_keys)
        url_input = str(url_setting)
        print(url_input)


        # save raw data by using etherscan.api
        with urllib.request.urlopen(url_input) as url:
            data = json.loads(url.read().decode())
            endnumber = len(data["result"])

            # writing startblock
            jsondata["startblock"] = str(startblock)
            
            # initialized dictionary
            selecteddata = {}
            jsondata["NFTdata"] = list()

            # classfiy by methodId
            while currentindex<endnumber:
                if data["result"][currentindex]['methodId'] == target_methodID and data["result"][currentindex]['isError'] == str(0):
                    selecteddata = {"timestamp" : data["result"][currentindex]['timeStamp'], "nftContractAddress" : '0x'+data["result"][currentindex]['input'][290:330]}
                    jsondata["NFTdata"].append(selecteddata)
                    count = count + 1
                    finalindex = currentindex
                currentindex = currentindex + 1   

            # setting startblock and endblock
            jsondata["endblock"] = str(data["result"][finalindex]['blockNumber'])
            jsondata["count"] = str(count)
            startblock = data["result"][finalindex]['blockNumber']

            # write json file
            with open('./'+str(contractname)+'/output_'+str(contractname)+'_'+str(filenum)+'.json', 'w') as f:
                json.dump(jsondata, f, indent=4)
                filenum = filenum +1

# get timestamp and NFT contract address of Wyvern2 Contract
def getDataofWyvern2(contractname, target_methodID, contractaddress, offset):
    # initial setting
    api_keys = ''
    startblock = 0
    endblock = 999999999
    filenum = 0
    jsondata = OrderedDict()

    while 1:
        # initialize data
        finalindex = 0
        currentindex = 0
        count = 0

        # update url by endblock
        url_setting = 'https://api.etherscan.io/api?module=account&action=txlist&address='+str(contractaddress)+'&startblock='+str(startblock)+'&endblock='+str(endblock)+'&page=1&offset='+str(offset)+'&sort=asc&apikey='+str(api_keys)
        url_input = str(url_setting)
        print(url_input)


        # save raw data by using etherscan.api
        with urllib.request.urlopen(url_input) as url:
            data = json.loads(url.read().decode())
            endnumber = len(data["result"])

            # writing startblock
            jsondata["startblock"] = str(startblock)
            
            # initialized dictionary
            selecteddata = {}
            jsondata["NFTdata"] = list()

            # classfiy by methodId
            while currentindex<endnumber:
                if data["result"][currentindex]['methodId'] == target_methodID and data["result"][currentindex]['isError'] == str(0):
                    selecteddata = {"timestamp" : data["result"][currentindex]['timeStamp'], "nftContractAddress" : '0x'+data["result"][currentindex]['input'][3626:3666]}
                    jsondata["NFTdata"].append(selecteddata)
                    count = count + 1
                    finalindex = currentindex
                currentindex = currentindex + 1   

            # setting startblock and endblock
            jsondata["endblock"] = str(data["result"][finalindex]['blockNumber'])
            jsondata["count"] = str(count)
            startblock = data["result"][finalindex]['blockNumber']

            # write json file
            with open('./'+str(contractname)+'/output_'+str(contractname)+'_'+str(filenum)+'.json', 'w') as f:
                json.dump(jsondata, f, indent=4)
                filenum = filenum +1

            if len(data["result"])==1:
                exit()


# get timestamp and NFT contract address of Seaport Contract
def getDataofSeaport(contractname, target_methodID, contractaddress, offset):
    # initial setting
    api_keys = ''
    startblock = 0
    endblock = 999999999
    filenum = 0
    jsondata = OrderedDict()

    while 1:
        # initialize data
        finalindex = 0
        currentindex = 0
        count = 0
        
        with open('./'+str(contractname)+'_endblock.txt', 'r') as g:
            startblock = int(g.readline())

        with open('./'+str(contractname)+'_filenum.txt', 'r') as h:
            filenum = int(h.readline())

        # update url by endblock
        url_setting = 'https://api.etherscan.io/api?module=account&action=txlist&address='+str(contractaddress)+'&startblock='+str(startblock)+'&endblock='+str(endblock)+'&page=1&offset='+str(offset)+'&sort=asc&apikey='+str(api_keys)
        url_input = str(url_setting)
        print(url_input)


        # save raw data by using etherscan.api
        with urllib.request.urlopen(url_input) as url:
            data = json.loads(url.read().decode())
            endnumber = len(data["result"])

            # writing startblock
            jsondata["startblock"] = str(startblock)
            
            # initialized dictionary
            selecteddata = {}
            jsondata["NFTdata"] = list()

            # classfiy by methodId
            while currentindex<endnumber:
                if data["result"][currentindex]['methodId'] == target_methodID and data["result"][currentindex]['isError'] == str(0):
                    # WETH case
                    if( data["result"][currentindex]["input"][418:458] == "c02aaa39b223fe8d0a0e5c4f27ead9083c756cc2"):
                        selecteddata = {"inputlen" : str(len(data["result"][currentindex]['input']))
                        ,"txhash" : data["result"][currentindex]["hash"], "contractaddress" : '0x'+data["result"][currentindex]["input"][99:139]}
                        count = count + 1
                        jsondata["NFTdata"] .append(selecteddata)
                    else:
                        selecteddata = {"inputlen" : str(len(data["result"][currentindex]['input']))
                        ,"txhash" : data["result"][currentindex]["hash"], "contractaddress" : '0x'+data["result"][currentindex]["input"][418:458]}
                        count = count + 1
                        jsondata["NFTdata"] .append(selecteddata)
                finalindex = currentindex
                currentindex = currentindex + 1   
                    

            # setting startblock and endblock
            jsondata["endblock"] = str(data["result"][finalindex]['blockNumber'])
            jsondata["count"] = str(count)
            startblock = data["result"][finalindex]['blockNumber']

            # write json file
            with open('./'+str(contractname)+'/output_'+str(contractname)+'_'+str(filenum)+'.json', 'w') as f:
                json.dump(jsondata, f, indent=4)
                filenum = filenum +1

            with open('./'+str(contractname)+'_endblock.txt', 'w') as g:
                g.truncate()
                g.write(str(jsondata["endblock"]))
            
            with open('./'+str(contractname)+'_filenum.txt', 'w') as h:
                h.truncate()
                h.write(str(filenum))


