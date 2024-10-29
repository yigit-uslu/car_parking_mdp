from types import SimpleNamespace
import numpy as np

N = 3
C = 4
p = 0.4

CANNOT_PARK = 0
CAN_PARK = 1
KEEP_LOOKING = 0
PARK = 1
PARKED_STATE = -1

park_status_dict = {'CANNOT_PARK': CANNOT_PARK, 'CAN_PARK': CAN_PARK}
PARK_STATUS_NS = SimpleNamespace(**park_status_dict)
action_dict = {'KEEP_LOOKING': KEEP_LOOKING, 'PARK': PARK}
ACTION_SPACE_NS = SimpleNamespace(**action_dict)

state_space_dict = {'PARKED_STATE': PARKED_STATE}
for n in range(1, N+1):
    for _, park_status in park_status_dict.items():
        state_space_dict[f'{(n, park_status)}'] = (n, park_status)
state_space_dict[f"(0, {PARK})"] = (0, PARK)

print('State-space: ', state_space_dict)
STATE_SPACE_NS = SimpleNamespace(**state_space_dict)
print('state-space-ns: ', STATE_SPACE_NS)