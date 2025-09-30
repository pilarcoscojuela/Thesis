# Thesis Experimental Results

This repository contains Magma code used in the thesis “Security Analysis of the Family of DME Schemes.” Because Magma V2.21-5 does not support exponents larger than 2^30, the examples operate over finite fields F_q with q up to 2^8 (and up to 2^14 in some cases).

## Branches
- DME: shows how to model collision recovery in DME by computing the 2-order minors of a matrix; corresponds to Chapter 4 of the thesis.
- DME_minus_2_entries: models collision recovery in DME minus by computing the 3-order minors of a matrix when the rows of the matrix corresponding to the last exponential map have at most two nonzero entries per row; corresponds to Chapter 5.
- DME_minus_3_entries: models collision recovery in DME minus by computing the 3-minors of a matrix for an instance where all rows of the matrix corresponding to the last exponential map have three nonzero entries; corresponds to Chapter 5.
- DME_plus: computes the system of equations for the DME plus variant that adds two extra polynomials per component; the final linear map is 16×16. These systems remain unsolved because Gröbner basis computation does not finish in Magma; corresponds to the DME+ section of Chapter 6.
- DME_w: work in progress; corresponds to the DME_w section in Chapter 6.
- recovery_variables_3ent: illustrates the “recovery of variables before the last exponential” section of Chapter 5 for a system where a matrix row has three nonzero entries.

## Notes
For a precise definition of DME, see https://blogs.mat.ucm.es/dme/
