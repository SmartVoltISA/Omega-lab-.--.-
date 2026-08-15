"""Ω-PHYS-ELECTRON-004
Corrected relation-only clustering and null-control analysis.

This script intentionally uses only the nine relation-level fields recorded in
OMEGA-PHYS-ELECTRON-004-BLINDED-HELDOUT-RELATIONS.md. Particle names are not
used by the clustering algorithm; labels are evaluation-only.
"""
import numpy as np
from sklearn.cluster import AgglomerativeClustering
from sklearn.metrics import adjusted_rand_score, silhouette_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import LeaveOneOut, cross_val_score

# Anonymous rows A-Q. Evaluation labels are kept separately.
X = np.array([
    [1,1,0,1,1,1,1,0,0], [1,1,0,1,1,1,1,0,0], [1,1,0,1,1,1,1,0,0],
    [0,1,0,1,1,0,1,0,0], [0,1,0,1,1,0,1,0,0], [0,1,0,1,1,0,1,0,0],
    [1,1,1,1,1,1,1,0,1], [1,1,1,1,1,1,1,0,1], [1,1,1,1,1,1,1,0,1],
    [1,1,1,1,1,1,1,0,1], [1,1,1,1,1,1,1,0,1], [1,1,1,1,1,1,1,0,1],
    [1,1,0,0,1,0,0,1,0], [0,1,1,0,1,0,0,1,1],
    [1,1,0,1,1,1,0,1,0], [0,1,0,1,1,0,0,1,0], [0,1,0,1,1,0,0,1,0],
], dtype=int)

y = np.array(
    ["charged_lepton"]*3 + ["neutrino"]*3 + ["quark"]*6 +
    ["gauge"]*4 + ["higgs"]
)

for k in range(2, 8):
    pred = AgglomerativeClustering(
        n_clusters=k, metric="hamming", linkage="average"
    ).fit_predict(X)
    ari = adjusted_rand_score(y, pred)
    sil = silhouette_score(X, pred, metric="hamming")
    print(f"k={k}: ARI={ari:.6f}, silhouette={sil:.6f}")

k = 7
pred = AgglomerativeClustering(
    n_clusters=k, metric="hamming", linkage="average"
).fit_predict(X)
observed = adjusted_rand_score(y, pred)

rng = np.random.default_rng(42)
null = []
for _ in range(5000):
    null.append(adjusted_rand_score(
        rng.permutation(y), pred
    ))
null = np.asarray(null)
p = (np.sum(null >= observed) + 1) / (len(null) + 1)
print(f"observed ARI={observed:.6f}")
print(f"null mean={null.mean():.6f}")
print(f"null std={null.std():.6f}")
print(f"permutation p={p:.6f}")

for n in (1, 2, 3):
    clf = KNeighborsClassifier(n_neighbors=n, metric="hamming")
    scores = cross_val_score(clf, X, y, cv=LeaveOneOut())
    print(f"LOO kNN={n}: accuracy={scores.mean():.6f} ({scores.sum()}/17)")
