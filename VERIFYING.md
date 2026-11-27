# Reproduce the checks

Run these commands from the root of this repository. The Python certificates use the standard library. The C++ checker uses C++17. The Lean files use the Mathlib revision pinned by Formal Conjectures.

## Signed graphs

```sh
python3 -B results/signed-cycle-vectors/check.py
c++ -std=c++17 -O2 results/signed-cycle-vectors/verify-multiplicity.cpp -o /tmp/verify-multiplicity
/tmp/verify-multiplicity
```

The first script verifies both eight-vertex inventories, a separate base example, triangle-count identities, and the membership formula on small graphs. The second program computes cycle counts by a different method. All four two-block choices agree at every length from 3 through 19. The written extension argument proves the claims for arbitrarily many vertices. [Proof](results/signed-cycle-vectors/multiplicity.md)

## Covering systems and open investigations

```sh
(cd results/covering-systems && python3 -B check_prime_tower.py)
(cd results/covering-systems/irredundant && python3 -B check_construction.py && python3 -B concrete_example.py)
python3 -B results/covering-systems/third-order/coverage_bound.py 15015
python3 -B investigations/hofstadter-modular/check.py
python3 -B investigations/bjorner-kl-realization/check.py
python3 -B investigations/cramer-prime-gaps/check.py
python3 -B investigations/cramer-prime-gaps/check-wheel.py
python3 -B investigations/cramer-prime-gaps/check-rough.py
python3 -B investigations/cramer-prime-gaps/check-prime-rows.py
python3 -B investigations/cramer-prime-gaps/check-alignment.py
python3 -B investigations/cramer-prime-gaps/check-count-polynomials.py
python3 -B investigations/cramer-prime-gaps/check-divisor-translates.py
python3 -B investigations/cramer-prime-gaps/check-deficit.py
python3 -B investigations/cramer-prime-gaps/check-far-pairs.py
```

For the illustrative odd period 15015, the coverage bound leaves at least 2905 residues uncovered. The Hofstadter and Kazhdan–Lusztig scripts check examples of the accompanying structural arguments. The Cramér scripts check counterexamples, finite polynomial identities, exact joint probabilities under the interpolated count law, and residue counts over full sieve periods. The rough-number script checks complete and incomplete period counts, the two inclusion–exclusion bounds, and the companion polynomial identity using exact arithmetic. The growing-order estimates and covering-product corollary have written proofs. The prime-row script checks the row and column counts for every eligible subset in its examples, handles gaps crossing the summation boundaries, and verifies the one-start-per-class deletion bound.

The alignment script exhausts marking patterns through length nine and checks the inequalities for suffix maxima and overlapping windows. The count-polynomial script checks the sliding-window crossing and Lagrange weights on exact and perturbed integer nodes. The arithmetic abundance estimate has a [written proof](investigations/cramer-prime-gaps/count-polynomials.md). The deficit script checks two pair-sum kernels, subwindow containment and the spacing argument for proper powers. The far-pair script checks the near/far cutoff signs and the weighted second difference with exact rational arithmetic. The optional floating-point replays use the plain-text file of the first 100,000 positive zero ordinates from Andrew Odlyzko. From the repository root, run the following command with the path to the uncompressed file. [Odlyzko’s zero table](https://www-users.cse.umn.edu/~odlyzko/zeta_tables/)

```sh
python3 -B investigations/cramer-prime-gaps/check-zero-sum.py /path/to/zeros1
python3 -B investigations/cramer-prime-gaps/check-far-pairs.py /path/to/zeros1
python3 -B investigations/cramer-prime-gaps/check-wide-band.py /path/to/zeros1
python3 -B investigations/cramer-prime-gaps/check-wheel-sampling.py /path/to/zeros1
```

The wide-band replay uses the compact Fourier transform of $(1-u^2)(\sin(u)/u)^8$ and the first two Taylor corrections for the Mellin weight. It compares a difference of scales with a directly sieved prime-power sum on four finite intervals, truncating the arithmetic kernel at log-distance $1/2$. Its residual includes the effects of the spatial truncation, Taylor approximation and rounded ordinates. It checks the single-zero calculation and power correction. The all-start bounds and pair-to-single-zero transfer in the [wide-separation note](investigations/cramer-prime-gaps/wide-separations.md) have written proofs.

The wheel-sampling replay checks interpolation on residues modulo 2, 6 and 30 and reconstructs six von Mangoldt weights from the tabulated zeros, including primes, proper powers and a composite with distinct prime factors. Without the ordinate file it runs the interpolation checks alone. [Formula and error bounds](investigations/cramer-prime-gaps/wheel-sampling.md)

## Lean

Install Lean's elan toolchain manager and Git. With the following pin, Lake uses Lean 4.33.1. The dependency checkout and initial cache download require several GB of disk. You can reuse an existing checkout at this exact revision.

```sh
git clone https://github.com/google-deepmind/formal-conjectures.git ../formal-conjectures
git -C ../formal-conjectures checkout --detach 9097e2f90e66d2f6244209cb1c07f7120d17ec53
(cd ../formal-conjectures && lake exe cache get)
```

From the root of this repository:

```sh
collection_dir="$(pwd)"
formal_dir="$(cd ../formal-conjectures && pwd)"
(cd "$formal_dir" && lake env lean "$collection_dir/investigations/cramer-prime-gaps/Counterexamples.lean")
(cd "$formal_dir" && lake env lean "$collection_dir/investigations/cramer-prime-gaps/WheelMoments.lean")
(cd "$formal_dir" && lake env lean "$collection_dir/results/signed-cycle-vectors/Dimension.lean")
(cd "$formal_dir" && lake env lean "$collection_dir/results/union-determinant/UnionDeterminant.lean")
(cd "$formal_dir" && lake env lean "$collection_dir/results/union-determinant/UnionMobius.lean")
bash results/covering-systems/verify.sh "$formal_dir"
bash results/covering-systems/third-order/verify.sh "$formal_dir"
bash results/covering-systems/irredundant/verify.sh "$formal_dir"
```

The signed-graph formalization proves the full-span statement for distinct edge sets grouped by labels. The manuscript identifies simple cycles with their edge sets. For third-order coverage the final Lean theorem assumes the normalization identified in the manuscript. The covering-system audit imports the upstream Erdős problem to check the reduction and repair step. The Gaussian equality proof and the signed-graph multiplicity proof are written mathematical arguments.
