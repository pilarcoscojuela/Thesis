
## Main files

- initial_setup.txt 
  Initializes cryptographic parameters, the finite field F_q, polynomial rings, and matrices.

- compute_equations.txt  
  - Generates a public key from a fixed private key defined in initial_setup.txt.  
  - Constructs systems of equations following the framework introduced by Daniel Smith-Tone et al.; only four lists appear, corresponding to the known components of the public key in the DME− variant.  
  - Instead of computing a Gröbner basis on the original system, the script builds an alternative system by applying a weighted-variable reduction; the new system uses variables Rt, St, Kt, Lt, Zt, Wt, Xt, Yt.  
  - Writes the relations between the reduced-system variables and the original variables to linear_system.txt.  
  - Introduce collision variables H's to the system in the variables Rt, St, Kt, Lt, Zt, Wt, Xt, Yt.
  - Returns the values of the collision variables that appear in the systems for the first and second components.

- remove_exp.py  
  Python helper script.

- simplify.txt  
  Simplifies exponent expressions (e.g., transforms Rt1^(2^3) * Xt1^(2^5) = T^5 into Rt1 * Xt1^(2^2) = (T^5)^(2^11) when working with q = 2^14).

- Intermediate outputs  
  result.txt, result_without_exp.txt, linear_system.txt.

## Usage

Run compute_equations.txt in Magma (version V2.21-5).

## Notes

For a precise definition of DME−, see https://blogs.mat.ucm.es/dme/

