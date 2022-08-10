STark - Executable Lark-based EBNF grammar for IEC 61131-3 ST POUs
=============================================================

STark is composed of the two terms ST and [Lark](https://github.com/lark-parser/lark) and represents an executable grammar for IEC 61131-3 Structured Text modules that is defined using the Lark-based Extended Backus-Naur Form (EBNF). It represents a subset of the grammars in [blark](https://github.com/klauer/blark) [1] and the IEC 61131-3 standard [2].

Features
----------------
* IEC 61131-3 POU-Types: Program, Functionblock, Function
* Sections (each available only once): VAR_INPUT, VAR, VAR_OUTPUT, VAR_IN_OUT, VAR_EXTERNAL
* Data types: BOOL, INT, DINT, UINT, REAL, TIME, ARRAY
* Operators: *, /, MOD, +, -, NOT, AND, XOR, OR, <=, >=, <, >, =, <>, FALSE, TRUE, external function/functionblocks, variable, constant
* Statements: assignments, if/else, case, macro, for, while, repeat, exit, return

Our goal is to minimize and to ensure uniqueness of the resulting parsing tree for a subset of the ST constructs for further use. In addition to the grammar, the repository contains more than 80 test cases for evaluating correctness, as well as a simple python script demonstrating a possible use of the Lark library.

Example
----------------
````
FUNCTION_BLOCK TC081
  VAR_INPUT
    IN1 : INT;
    IN2 : INT;
    IN3 : INT;
    IN4 : BOOL;
  END_VAR
  VAR_OUTPUT
    Wrn : BOOL;
    Err : BOOL;
    Ctr : INT;
    iOut2 : INT;
  END_VAR
  VAR
    SR1 : SR;
    TON1 : TON;
    TON2 : TON;
  END_VAR
  
  SR1(((((20*IN1)+(6*IN2)+IN3))=(100*2)) AND (IN1+IN2+IN3=100),IN4);
  TON1((((((20*IN1)+(6*IN2)+IN3))=(100*2)) AND (IN1+IN2+IN3=100)),2);
  TON2((IN1+IN2+IN3=42) AND SR1.Q,3);
  Ctr := TON2.ET;
  Err := TON1.Q;
  Wrn := SR1.Q;
END_FUNCTION_BLOCK
````
![diagram-20220810](https://user-images.githubusercontent.com/92115516/183843727-027604d9-24c2-483a-9a78-2f4827f862ec.svg)

References
----------------
[1] Ken Lauer, “Beckhoff TwinCAT IEC 61131-3 Lark-based Structured Text Tools”, v0.5.0, https://github.com/klauer/blark

[2] DIN Deutsches Institut für Normung e. V., “Programmable controllers – Part 3: Programming languages (IEC 61131-3:2013); German version EN 61131-3:2013,” 2014.
