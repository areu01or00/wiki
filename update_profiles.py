import json
from datetime import datetime, timezone

# Load temp results
with open('/home/hermes/wiki/temp/watch_run_20260611_084726.json', 'r') as f:
    temp_data = json.load(f)

all_hashes_used = temp_data['all_hashes_used']

# Load profiles
with open('/home/hermes/wiki/watch_profiles.json', 'r') as f:
    data = json.load(f)

now_str = datetime.now(timezone.utc).isoformat()

# Update each profile
for profile_name, new_hashes in all_hashes_used.items():
    if not new_hashes:
        continue
    
    # Append new hashes (keep max 20)
    existing = data['profiles'][profile_name]['last_result_hashes']
    existing.extend(new_hashes)
    data['profiles'][profile_name]['last_result_hashes'] = existing[-20:]
    
    # Update last_run
    data['profiles'][profile_name]['last_run'] = now_str
    
    print(f"{profile_name}: appended {len(new_hashes)} hashes, total {len(data['profiles'][profile_name]['last_result_hashes'])}")

# Write back
with open('/home/hermes/wiki/watch_profiles.json', 'w') as f:
    json.dump(data, f, indent=2)

print(f"\nUpdated watch_profiles.json at {now_str}")
