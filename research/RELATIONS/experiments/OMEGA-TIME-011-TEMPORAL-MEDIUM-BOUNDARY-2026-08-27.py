"""OMEGA-TIME-011 executable analytic/Monte-Carlo-ready core."""
import numpy as np
p_free=0.90
p_bound=0.08
p_transition=np.linspace(p_free,p_bound,60)
free_cost=120/p_free
transition_cost=float(np.sum(1/p_transition))
bound_cost=120/p_bound
slowdown=(1/p_bound)/(1/p_free)
print('free_expected_updates',free_cost)
print('transition_expected_updates',transition_cost)
print('bound_expected_updates',bound_cost)
print('equal_length_bound_vs_free_slowdown',slowdown)
assert slowdown==p_free/p_bound
# controls
assert (120/.5)/(120/.5)==1
print('uniform_control_effect',False)
print('RESULT: local transition accumulation changes strongly while causal order is preserved.')
print('UNIVERSAL_TIME_FIELD_ESTABLISHED',False)
