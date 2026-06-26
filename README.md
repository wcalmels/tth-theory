# Torsional Holofractal Theory (TTH)

<div align="center">

**A Geometric Framework for Objective Quantum Collapse,  
Integrated Information, and the Physical Basis of Consciousness**

[![Author](https://img.shields.io/badge/Author-Walter%20Calmels%20Von%20dem%20Knesebeck-blue)](mailto:wcalmels@phi47.cl)
[![Institution](https://img.shields.io/badge/Lab-TUCH%20Systems%20Research%20Laboratory-green)](https://tuch.systems)
[![License](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.10%2B-yellow)](https://python.org)
[![LaTeX](https://img.shields.io/badge/LaTeX-pdflatex-red)](https://www.latex-project.org/)

*"The universe is a quantum gravitational optimizer, collapsing superpositions  
into definite experiences at a rate governed by δ = 4.66920…"*

</div>

---

## Overview

**Torsional Holofractal Theory (TTH)** is a mathematically rigorous extension of
Einstein–Cartan gravity incorporating a holofractal scalar field φ(x) whose vacuum
expectation value is fixed by the **golden ratio** Φ = (1+√5)/2 = 1.61803… and whose
potential is modulated by the **Feigenbaum constant** δ = 4.66920160910299…

The theory derives — from a single action principle — three coupled field equations
that produce:

| Result | Description | Section |
|--------|-------------|---------|
| **R1** | Modified Einstein–Cartan equations with φ²-modulated torsion | §III |
| **R2** | CMB log-periodic modulations with frequency δ in ln(ℓ) | §IV |
| **R3** | Objective quantum collapse when Φ_TTH > ℏ/(δ·M_Pl) | §V |
| **R4** | EEG fractal dimension D_f = 2 − (δ−4)/(δ−3) = **1.599** | §VI |
| **R5** | Three-level consciousness hierarchy from field equations | §VI |

---

## Five Falsifiable Predictions

| # | Domain | Prediction | Test |
|---|--------|-----------|------|
| **P1** | Cosmology | δC_ℓ/C_ℓ ~ 2% sin(δ·ln ℓ) | Planck 2018, CMB-S4 |
| **P2** | Quantum optics | Γ_UCN ~ 10⁻⁶ Hz (UCN decoherence) | PSI, ILL, SNS |
| **P3** | Neuroscience | D_f^EEG = 1.599 (conscious wakefulness) | 256-ch EEG + MFDFA |
| **P4** | Neuroscience | Φ_IIT ∝ (D_f − 3)² | TMS-EEG + MFDFA |
| **P5** | Neuroscience | Schumann (7.83 Hz) entrains D_f and PCI | TMS protocol |

---

## Repository Structure

```
tth-theory/
│
├── README.md                        ← This file
├── LICENSE                          ← CC BY 4.0
│
├── papers/
│   ├── latex/
│   │   ├── paper1.tex               ← TTH Foundations (Physical Review D)
│   │   ├── paper2.tex               ← Hierarchical Consciousness (Consciousness & Cognition)
│   │   └── cover_letter.tex         ← Cover letter for Phys Rev D
│   └── pdf/
│       ├── TTH_Paper1_CalmelsVondemKnesebeck_2026.pdf
│       └── TTH_Paper2_Hierarchy_CalmelsVondemKnesebeck_2026.pdf
│
├── figures/
│   ├── scripts/
│   │   ├── figures_1to7.py          ← Generate Figures 1–7 (matplotlib)
│   │   ├── figure8.py               ← Tesla–Russell–Feigenbaum connection
│   │   ├── figure9.py               ← Three-level hierarchy diagram
│   │   └── figure10.py              ← Dimensional scenarios
│   └── output/                      ← Generated PNG/PDF figures (300 DPI)
│
├── code/
│   ├── simulations/
│   │   ├── tth_field_equations.py   ← Numerical solver: FLRW + φ field
│   │   ├── collapse_dynamics.py     ← Φ_TTH evolution and collapse timescale
│   │   ├── cmb_oscillations.py      ← CMB power spectrum with TTH modulations
│   │   └── eeg_fractal.py           ← EEG fractal dimension simulation
│   ├── analysis/
│   │   ├── mfdfa.py                 ← Multifractal DFA implementation
│   │   ├── hurst_exponent.py        ← Hurst exponent from Feigenbaum potential
│   │   └── phi_iit_correlation.py   ← Φ_IIT vs D_f correlation analysis
│   └── validation/
│       ├── test_golden_vacuum.py    ← Verify φ₀ = Φ_gold · M_Pl
│       ├── test_feigenbaum_hurst.py ← Verify H = (δ−4)/(δ−3) = 0.401
│       ├── test_collapse_criterion.py ← Verify Φ_crit = ℏ/(δ·M_Pl)
│       └── run_all_tests.py         ← Full test suite
│
└── docs/
    ├── THEORY.md                    ← Mathematical summary of TTH
    ├── PREDICTIONS.md               ← Detailed experimental predictions
    └── CHANGELOG.md                 ← Version history
```

---

## Quick Start

### Requirements

```bash
pip install numpy scipy matplotlib pandas astropy
```

### Run All Validations

```bash
cd code/validation
python run_all_tests.py
```

Expected output:
```
✓ Test 1: Golden Vacuum  — φ₀ = 1.61803 · M_Pl  [PASS]
✓ Test 2: Feigenbaum–Hurst — H = 0.4009  [PASS]
✓ Test 3: Collapse Criterion — Φ_crit = 2.19×10⁻⁴⁴ J·s  [PASS]
✓ Test 4: EEG Fractal Dimension — D_f = 1.5991  [PASS]
✓ Test 5: CMB oscillation frequency — Δln(ℓ) = 0.6731  [PASS]
✓ Test 6: Neural collapse timescale — τ ∈ [10⁻³, 10⁻¹] s  [PASS]

6/6 tests passed ✓
```

### Generate All Figures

```bash
cd figures/scripts
python figures_1to7.py    # Generates figures 1–7
python figure8.py          # Tesla–Russell–Feigenbaum
python figure9.py          # Hierarchy diagram
python figure10.py         # Dimensional scenarios
```

### Compile Papers (requires LaTeX)

```bash
cd papers/latex
pdflatex paper1.tex && pdflatex paper1.tex   # Two passes for TOC/refs
pdflatex paper2.tex && pdflatex paper2.tex
```

---

## Key Equations

### TTH Action
```
S_TTH = ∫ d⁴x √(-g) [L_EC + L_φ + L_matter + L_int]
```

### Holofractal Potential
```
V(φ) = (λ/4)(φ² - v²)² + Λ_δ⁴[1 - cos(δ·φ/v)]
```
where **v = Φ_gold · M_Pl** (Golden Vacuum, Theorem 1).

### Modified Einstein Equation
```
(1 - ξφ²/M_Pl²) G_μν(Γ) + ξφ/M_Pl² (∇_μ∇_ν - g_μν□)φ + g_μν Λ = 8πG T_μν
```

### Torsion Equation (new vs standard EC)
```
T^λ_μν (1 + ξφ²/M_Pl²) = 8πG S^λ_μν − (α_T/M_Pl³) φ δ^λ_[μ j⁵_ν]
```

### Collapse Criterion
```
Φ_TTH = ∫ η(t)|Ψ|² S_vN(ρ_r) d³r  >  Φ_crit = ℏ/(δ·M_Pl) ≈ 2.2×10⁻⁴⁴ J·s
```

### Feigenbaum–Hurst Theorem
```
H_TTH = (δ−4)/(δ−3) = 0.669/1.669 = 0.4009
D_f^EEG = 2 − H_TTH = 1.599     (conscious wakefulness)
```

---

## Physical Constants in TTH

| Constant | Symbol | Value | Role |
|----------|--------|-------|------|
| Planck mass | M_Pl | 2.176 × 10⁻⁸ kg | Sets vacuum v = Φ·M_Pl |
| Golden ratio | Φ_gold | 1.61803398… | Vacuum φ₀/M_Pl |
| Feigenbaum δ | δ_F | 4.66920160… | Φ_crit denominator; V(φ) frequency |
| Collapse threshold | Φ_crit | 2.2 × 10⁻⁴⁴ J·s | Objective reduction criterion |
| Non-min. coupling | ξ | ~10⁴ | From CMB n_s constraint |
| Torsion coupling | α_T | ~1 (dimensionless) | Sets η₀ = α_T·Φ_gold |
| Feigenbaum scale | Λ_δ | ~2.4 meV | Dark energy amplitude |
| EEG Hurst exponent | H_TTH | 0.4009 | D_f = 2 − H = 1.599 |

---

## Relation to Existing Theories

```
          ┌─────────────────────────────────────────────────────┐
          │                  TTH (this work)                   │
          │  Derives from: S = ∫d⁴x√(-g)[L_EC + L_φ + ...]   │
          └────────┬──────────────┬──────────────┬─────────────┘
                   │              │              │
          ┌────────▼──────┐ ┌────▼────┐ ┌──────▼──────┐
          │   Orch-OR     │ │   IIT   │ │     GNW     │
          │ (limit ξ→0)   │ │ Φ_IIT = │ │ "ignition"= │
          │ τ~ℏ/E_G match │ │ Φ_TTH/η │ │ φ threshold │
          └───────────────┘ └─────────┘ └─────────────┘
```

---

## Citation

If you use TTH in your research, please cite:

```bibtex
@article{CalmelsVondemKnesebeck2026a,
  author  = {Calmels Von dem Knesebeck, Walter},
  title   = {Torsional Holofractal Theory: A Geometric Framework for
             Objective Quantum Collapse, Integrated Information,
             and the Physical Basis of Consciousness},
  journal = {Physical Review D},
  year    = {2026},
  note    = {Manuscript submitted}
}

@article{CalmelsVondemKnesebeck2026b,
  author  = {Calmels Von dem Knesebeck, Walter},
  title   = {Hierarchical Consciousness Architecture in Torsional
             Holofractal Theory: Neural Implementation and
             Experimental Predictions},
  journal = {Consciousness and Cognition},
  year    = {2026},
  note    = {Manuscript submitted}
}
```

---

## Author

**Walter Calmels Von dem Knesebeck**  
Founder & CTO, TUCH Systems Research Laboratory  
Buenos Aires, Argentina · Santiago (Maipú Lab), Chile  
📧 [wcalmels@phi47.cl](mailto:wcalmels@phi47.cl)  
🐙 [github.com/wcalmels](https://github.com/wcalmels)

---

## License

This work is licensed under [Creative Commons Attribution 4.0 International (CC BY 4.0)](LICENSE).  
You are free to share and adapt this material for any purpose, provided appropriate credit is given.

---

*"If confirmed, TTH would establish: consciousness has a geometric basis in torsional spacetime;  
the golden ratio and Feigenbaum constant are fundamental constants of the theory of mind."*
