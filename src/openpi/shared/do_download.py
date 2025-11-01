# from openpi.training import config as _config
# from openpi.policies import policy_config
from openpi.shared import download
import os

# config = _config.get_config("pi05_droid")
checkpoint_dir = download.maybe_download("gs://openpi-assets/checkpoints/pi05_libero")
print("downloaded checkpoint to:", checkpoint_dir)