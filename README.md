# KTH AI Planning Project

KTH AI course final project. 

Implemtation of a variation of VRP using: Integer Programming, PDDL and Reinforcement Learning.

To run **Integer Programming:**
- Download AMPL
- Run: reset; model P0.i.mod; data P0.i.dat; solve; (For any problem variation i in Integer Programming folder)

To run **PDDL:**
- Download "any" PDDL solver
- Run the solver on any of the problem variations at PDDL/problems/

To run **Reinforcement Learning:**
- Create a python virtual environment
- pip install -r requirements.txt
- run python agent.py for an example
- in data.py you can change initial state
