# Projection Combination Check

Series: Inside the Spec – Real Scenarios. Working Artifacts. Decisions That Matter.  
Case: 02  
Author: Yulia Melekhova  
Version: 0.3  
Language: en  
Status: Draft

## Purpose
Use decision-combinations.csv to inspect every state tuple under the first-match rules. Run python3 artifacts/verify.py from the package root to regenerate the table, the embedded dictionary, and the model-check report.

The rejected OMS path increases the state space from 3×4×4=48 to 4×4×4=64. The table lists all 64 tuples with F=false and the result with F=true. Thus 128 model inputs are checked, including all 64 D01 overrides. Tuples include inconsistent and unreachable-in-normal-flow combinations deliberately, because asynchronous or faulty sources can supply them.

D02 rows record the decision that creates a flag; a subsequent evaluation selects D01. Coverage confirms totality of the finite projection function and selected invariants. It does not test transport, authentication, dispatch, event validation, persistence, concurrency, timers, or reconciliation implementation. Acceptance scenarios are separate specified expectations.

The function in verify.py implements the prose decision table. It is a review model, not production integration code. The script checks independent invariants and selected manually specified outcomes in addition to enumerating its own outputs.


---
Inside the Spec · Real Scenarios. Working Artifacts. Decisions That Matter.
https://github.com/YuliaMelekhova/inside-the-spec
https://www.linkedin.com/in/yuliamelekhova
