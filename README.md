# ETHContractAddressextractor

## Introduction

WyvernV1 : 0x7be8076f4ea4a4ad08075c2508e481d6c946d12b | 0xab834bab
WyvernV2 : 0x7f268357A8c2552623316e2562D90e642bB538E5 | 0xab834bab
OpenseaSeaport : 0x00000000006c3852cbef3e08e8df289169ede581 | 0xfb0f3ee1

### 1. util.h

We have setup the basic CPU_State that is sufficient to implement the project.
However, you may decide to add more variables, and modify/remove any misleading variables.

### 2. run.h

You may add any additional functions that will be called by your implementation of `process_instruction()`.
In fact, we encourage you to split your implementation of `process_instruction()` into many other helping functions.
You may decide to have functions for each stages of the pipeline.
Function(s) to handle flushes (adding bubbles into the pipeline), etc.

### 3. run.c

**Implement** the following function:

    void process_instruction()

The `process_instruction()` function is used by the `cycle()` function to simulate a `cycle` of the pipelined simulator.
Each `cycle()` the pipeline will advance to the next instruction (if there are no stalls/hazards, etc.).
Your internal register, memory, and pipeline register state should be updated according to the instruction
that is being executed at each stage.

## Details of Register Contents

This is details of Fields newly introduced on `util.h`.

### 1. Signal Set

- `BR_SIGNAL` is signal which indicates that **branch operation** occurred.
- `STALL_SIGNAL` is signal which indicates that pipeline **IF, ID** stalls by lw operation branching.
- `FORWARD_SIGNAL` is signal which indicates that forwarding in **EX_MEM** level occurred.
- `PIPE_FLUSH_SIGNAL` is signal which indicates that last instruction is at IF stage. Which means that PC goes over .text region
- `JUMP_SIGNAL` is signal which indicates that jump operation is observed. JUMP_SIGNAL is transferred by pipeline registers.
-

### 2. IF_ID_latch

- `IF_ID_INST` saves current **program counter**.
- `IF_ID_NPC` saves **next PC** address. When this value goes over .text address region, it turns on `PIPE_FLUSH_SIGNAL`.

### 3. ID_EX_latch

In this stage, instruction information is saved. To accomplish this, instruction address from IF_ID_INST is interpreted.  
Regardless of instruction type, every data is interpreted since only valid data will be selected and used at EX stage.

- `ID_EX_NPC` saves `NPC` value from **IF_ID_latch**.
- `ID_EX_OPCODE` saves **Operation Code** value.
- `ID_EX_RS` saves **rs** register number.
- `ID_EX_RT` saves **rt** register number.
- `ID_EX_REG1` saves data saved in **rs** register number.
- `ID_EX_REG2` saves data saved in **rt** register number.
- `ID_EX_SHAMT` saves **Shift Amount** value.
- `ID_EX_IMM` saves **Immediate** value.
- `ID_EX_FUNCT` saves **Function Code** value.
- `ID_EX_TARGET` saves **Jump Target** value
- `ID_EX_DEST` saves **Destination Register** value. Two cases are possible.
  - Value is **rd** register number when R-type.
  - Value is **rt** register number when I-type or J-type. Since J-type does not have destination register, but it just saves some data in `ID_EX_DEST`.
- `ID_EX_TYPE_FLAG` saves which type the instruction is.
  - Value is **zero** when instruction is **R-type** except **jr** instruction.
  - Value is **one** when instruction is **I-type**.
  - Value is **two** when instruction is **J-type** or it's **jr** instruction.

## CheckList

- Get familiar with github
- Select language to develop -> python?
- Make target feature -> hml parser/error checker/...etc
- Select role -> Parser function/API setting/...etc
- +add checklist you want
