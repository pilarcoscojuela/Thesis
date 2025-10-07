# Thesis Experimental Results

This repository contains Magma code used in the thesis “Security Analysis of the Family of DME Schemes.” Because Magma V2.21-5 does not support exponents larger than 2^30, the examples operate over finite fields F_q with q up to 2^8 (and up to 2^14 in some cases).

## Branches
- DME: shows how to model collision recovery in DME by computing the 2-order minors of a matrix; corresponds to Chapter 4 of the thesis.
- DME_minus_2_entries: models collision recovery in DME minus by computing the 3-order minors of a matrix when the rows of the matrix corresponding to the last exponential map have at most two nonzero entries per row; corresponds to Chapter 5.
- DME_minus_3_entries: models collision recovery in DME minus by computing the 3-minors of a matrix for an instance where all rows of the matrix corresponding to the last exponential map have three nonzero entries; corresponds to Chapter 5.
- DME_plus: computes the system of equations for the DME plus variant that adds four extra polynomials per component; the final linear map is 24×24. These systems remain unsolved because Gröbner basis computation does not finish in Magma; corresponds to the DME+ section of Chapter 6.
- DME_w: work in progress; corresponds to the DME_w section in Chapter 6.
- recovery_variables_3ent: illustrates the “recovery of variables before the last exponential” section of Chapter 5 for a system where a matrix row has three nonzero entries.

============================================================================================================================================================================================================================

Except for the branch DME_w, main files are (not all the files are needed in all the branches)

## Main files

- initial_setup.txt 
  Initializes cryptographic parameters, the finite field F_q, polynomial rings, and matrices.

- compute_equations.txt  
  - Generates a public key from a fixed private key defined in initial_setup.txt.  
  - Constructs systems of equations following the framework introduced by Daniel Smith-Tone et al.; only four lists appear, corresponding to the known components of the public key in the DME−     variant.  
  - Instead of computing a Gröbner basis on the original system, the script builds an alternative system by applying a weighted-variable reduction; the new system uses variables Rt, St, Kt, Lt, Zt, Wt, Xt, Yt.  
  - Writes the relations between the reduced-system variables and the original variables to linear_system.txt.  
  - Introduces collision variables H's to the system in the variables Rt, St, Kt, Lt, Zt, Wt, Xt, Yt.
  - Returns the values of the collision variables that appear in the systems for the first and second components.

- remove_exp.py  
  Python helper script.

- simplify.txt  
  Simplifies exponent expressions (e.g., transforms Rt1^(2^3) * Xt1^(2^5) = T^5 into Rt1 * Xt1^(2^2) = (T^5)^(2^11) when working with q = 2^14).

- Intermediate outputs  
  result.txt, result_without_exp.txt, linear_system.txt.

## Usage

Run compute_equations.txt in Magma (version V2.21-5). This script calls Python3.

## Notes

For a precise definition of DME and DME-, see https://blogs.mat.ucm.es/dme/
For other variants, see Chapter 3 of the thesis.
