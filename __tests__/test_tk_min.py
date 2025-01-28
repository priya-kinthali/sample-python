import pytest
import subprocess
import os
import sys

@pytest.mark.xfail(
    ('GITHUB_ACTION' in os.environ) and
    sys.platform == 'darwin' and sys.version_info[:2] < (3, 9),
    reason='Tk version mismatch on Azure macOS CI',
    strict=True
)
def test_tk_min_script():
    # Run the tk_min.py script and check if it executes without errors
    result = subprocess.run(['python', 'tk_min.py'], capture_output=True, text=True)
    assert result.returncode == 0

# ('TF_BUILD' in os.environ or 'GITHUB_ACTION' in os.environ) and
