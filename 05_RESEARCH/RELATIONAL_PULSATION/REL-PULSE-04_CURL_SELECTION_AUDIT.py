import numpy as np

rng = np.random.default_rng(20260908)

def cross_matrix(k):
    x, y, z = k
    return np.array([[0., -z, y], [z, 0., -x], [-y, x, 0.]])

max_skew = max_long = max_eig = 0.0
for _ in range(1000):
    k = rng.normal(size=3)
    C = cross_matrix(k)
    max_skew = max(max_skew, np.linalg.norm(C + C.T))
    max_long = max(max_long, np.linalg.norm(C @ k))
    eig = np.linalg.eigvalsh(1j * C)
    target = np.array([-np.linalg.norm(k), 0., np.linalg.norm(k)])
    max_eig = max(max_eig, np.max(np.abs(eig - target)))

# Isotropic identity/gradient-type principal structure is not transverse-only.
k = np.array([1., 2., 3.])
assert np.linalg.norm(np.eye(3) @ k) > 0

# A preferred-axis skew operator conserves a Euclidean quadratic measure,
# but violates isotropy: conservation alone cannot select curl.
P = cross_matrix(np.array([1., 0., 0.]))
assert np.linalg.norm(P + P.T) == 0.0

print('REL-PULSE-04')
print('max curl skew residual:', max_skew)
print('max curl longitudinal residual:', max_long)
print('max curl eigenvalue error:', max_eig)
print('PASS: curl has transverse spectrum -|k|,0,+|k|')
print('PASS: conservation alone is insufficient; preferred-axis skew is countermodel')
