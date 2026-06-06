# Mock to patch pcbnew during tests
import sys
from unittest.mock import MagicMock

class MockPcbnew:
    __file__ = "mocked_pcbnew"

sys.modules['pcbnew'] = MockPcbnew()
