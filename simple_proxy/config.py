import os

from dotenv import load_dotenv

from simple_proxy.paths import ENV_FILE

# --- Load Environment
load_dotenv(dotenv_path=ENV_FILE)

# --- Bind Environment variables

# Category
CONFIGURATION_VARIABLE_1 = str(os.environ.get("CONFIGURATION_VARIABLE_1", "default"))
