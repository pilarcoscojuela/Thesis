# Thesis experimental results

This repository contains some of the Magma code using in the thesis: Security Analysis of the Family of DME Schemes. Because Magma V2.21-5 does not support exponents larger than 2^(30), our examples works over finite fieldd F_q with q up to  2^8 and 2^14 in some cases.

# Branches:
- DME: shows how to model the collision recovery in DME by computing the minors of order two of a matrix. It corresponds to Chapter 4 in the thesis.
- DME_minus_2_entries: shows how to model the collision recovery in DME minus by computing the minors of order three of a matrix, in the case that the considered rows of the matrix corresponding to the last exponential map does not have more than two entries per row. It corresponds to Chapter 5 in the thesis.
- DME_minus_3_entries:  shows how to model the collision recovery in DME minus by computing the minors of order three of a matrix, for an instance where all the rows of the matrix corresponding to the last exponenetial map have three entries. It corresponds to Chapter 5 in the thesis.
- DME_plus: compute the system of equations of the version of DME plus that consists of adding two extra polynomials per component. Therefore, the final linear map is given by a matrix 16x16. The systems of equations are still unsolved as Gröbner basis computation does not finish on Magma.It corresponds to the DME plus section of Chapter 6. 
- DME_w: It is still in progress but corresponds to the section of DME_w in Chapter 5.
- recovery_variables_3ent: illustrate section recovery variables before the last exponential of Chapter 5 in the case the system of equations corresponds to a row of the matrix with three non zero entries.


## Notes
Visit 
https://blogs.mat.ucm.es/dme/ for a precise definition of DME minus.
