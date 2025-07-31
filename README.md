# Spatial Distribution of Black Hole–Type Objects in Strong Lensing Clusters

This repository presents data, code, and results from a novel observational study investigating the spatial distribution of black hole (BH)–type objects around nine massive galaxy clusters exhibiting strong gravitational lensing. By comparing observed distributions of BH-related objects (e.g., AGN, QSOs, X-ray binaries) to randomized background fields, we uncover statistically significant clustering patterns that correlate with cluster dynamical state.

## Key Findings

- **Central Deficits in Merging Clusters**: Several dynamically active or merging clusters (e.g., Bullet Cluster, Abell 2744) exhibit a marked absence of BH-type objects in their cores, with overdensities emerging at larger radii.

- **Central Concentration in Select Cases**: In contrast, clusters like MACS J1149.5+2223 show a strong central peak in BH-type object density.

- **Statistical Significance**: Using Poisson probabilities and KS tests, we confirm that these patterns deviate significantly from randomized expectations, often at p-values ≪ 10⁻²⁰.

- **Implications**: Results suggest that BH-type object distributions trace not just gravitational wells, but also the dynamical history and core state of the host cluster.

## Cluster Sample

| Cluster Name         | Notable Properties                     |
|----------------------|----------------------------------------|
| Bullet Cluster       | Post-merger, highly disturbed          |
| MACS J1149.5+2223    | Centrally concentrated BHs             |
| Abell 2744           | Extreme merger (Pandora's Cluster)     |
| CL J1226.9+3332      | Relaxed large-scale, disturbed core    |
| Abell 1689           | Very relaxed, central BH deficit       |
| RX J0717.5+3745      | Active merger, sparse BHs              |
| MACS J1206.2-0847    | No BHs detected                        |
| MACS J0416.1-2403    | No BHs detected                        |
| RX J1347.5-1145      | No BHs detected                        |

## Methodology Overview

### BH-Type Object Querying

Queried SIMBAD for BH-like types (`BH`, `BHXRB`, `XRB`, `QSO`, `AGN`, `BLAZAR`) within 20′ of each cluster center.

### Random Field Controls

Generated 200 randomized control points per cluster, avoiding known lens centers, to model expected background distributions.

### Radial Profile Analysis

Measured BH counts in radial bins (0.1′ to 20′) and compared observed vs. random cumulative counts.

### Significance Testing

Employed Poisson statistics and Kolmogorov–Smirnov (KS) tests to assess deviations from randomness.

## How to Use

Install required packages:

```bash
pip install astroquery astropy
```

Run the script:

```bash
python scripts/query_bh_near_lens_example.py
```

Modify `ra`, `dec`, or `radius` in the script to analyze a different cluster.

## License

This repository is made publicly available for research transparency and reproducibility. See the LICENSE file for terms.
