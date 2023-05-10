# thesis

For Lemma 4.2.6, we used lemma_4.2.6.py, which computes the 2-norms of ((MA)^(α) * (MB)^(β))/λ^(α + β) for 1 ≤ α ≤ 25 and 1 ≤ β ≤ 2 and prints the cases in which the norm is greater than 1. In fact, we replace λ = 1.658967081916... with a value smaller than it (namely ell = 1.658967). The script returns α = 1, β = 1, with norm = 1.0277.... We use the Python packages numpy (for matrix arithmetic) and itertools (for more easily readable nested for loops).

For Theorem 5.4.10, we used thm_5.4.10.py, which checks equations (5.39), (5.40), (5.41), (5.42), and (5.44) much in the same manner as we did for Lemma 4.2.6. For (5.39) and (5.41), we have a boolean which should be set to True if there are exceptions -- if not, then it prints "No exceptions". For (5.40), exceptions are printed. For (5.42) and (5.44), potential exceptions (e.g. for (5.42), (α, β) such that the 2-norm of ((MA)^(α) * (MB)^(β))/λ^(α + β) is greater than 0.8) are printed.
