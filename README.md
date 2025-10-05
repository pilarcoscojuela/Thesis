
## Main files

- initial_setup.txt 
  Initializes cryptographic parameters, the finite field F_q, polynomial rings, and matrices.

- compute_equations_simplify_linear.txt  
  - Derives equations between the last linear map and a modified linear map with the suitable last but one linear map, which are printed in "result_ab.txt".
  
- linear_simplified.txt  
  - Solves equations in "result_ab.txt".

- compute_equations.txt  
  - Generates a public key from a fixed private key defined in initial_setup.txt.  
  - Constructs systems of equations following the framework introduced by Daniel Smith-Tone et al. and are printed in "original_system.txt".
  - 
- replace.py  
  Python helper script that removes the exponents of equation in "original_system.txt" and prints the output in "result_replaced.txt".
  
- solution_result_replaced.txt  
  - Solves "result_replaced.txt"

## Notes

For a precise definition of DME_w see Chapter 3 of the thesis.

