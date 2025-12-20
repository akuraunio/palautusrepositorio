# Test configuration and fixtures
import sys
from pathlib import Path

# Add src directory to path so we can import modules
src_path = Path(__file__).parent.parent
sys.path.insert(0, str(src_path))
