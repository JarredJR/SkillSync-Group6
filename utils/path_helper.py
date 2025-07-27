import os
import sys
import shutil

def get_data_dir():
    """Return a writable data directory for the app."""
    if getattr(sys, 'frozen', False):  
        base_dir = os.path.join(
            os.path.expanduser("~"),
            "Library", "Application Support", "SkillSync"
        ) if sys.platform == "darwin" else os.path.join(
            os.environ.get("APPDATA", os.path.expanduser("~")),
            "SkillSync"
        )
        os.makedirs(base_dir, exist_ok=True)
        bundle_data = os.path.join(sys._MEIPASS, "data")
        for file in ["users.json", "requests.json", "messages.json", "providers.json"]:
            target = os.path.join(base_dir, file)
            if not os.path.exists(target):
                shutil.copy(os.path.join(bundle_data, file), target)
        return base_dir
    else:
        return os.path.abspath("data")

def resource_path(relative_path):
    return os.path.join(get_data_dir(), relative_path)
