# ETHContractAddressextractor V1(2022-08-26)
- For my research, I created a script that extracts only *timestamp* and *contractaddress*. 
It will make it possible to extract the desired elements in the future.


## Background
- WyvernV1 : {0x7be8076f4ea4a4ad08075c2508e481d6c946d12b,0xab834bab}
- WyvernV2 : {0x7f268357A8c2552623316e2562D90e642bB538E5,0xab834bab}
- OpenseaSeaport : {0x00000000006c3852cbef3e08e8df289169ede581,0xfb0f3ee1}

## Factor
- [Opensea Wyvern V1] : Finding *Atomic Match_* and parsing input data
- [Opensea Wyvern V2] : Finding *Atomic Match_* and parsing input data
- [Opensea Seaport] : Finding *0xfb0f3ee1* and parsing 
- update startblock via last point's block number

## How To use
- You should get Etherscan API via Etherscan.io (https://etherscan.io/)
- you should fill API key in *api_keys*

## TODO
- Sometimes NoneType Error occur. you should restart it manually


## UPDATE
- In some cases, data cannot be fed as much as *offset*, so revise this factor
