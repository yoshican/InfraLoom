# test_infraloom.py
"""
Tests for InfraLoom module.
"""

import unittest
from infraloom import InfraLoom

class TestInfraLoom(unittest.TestCase):
    """Test cases for InfraLoom class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = InfraLoom()
        self.assertIsInstance(instance, InfraLoom)
        
    def test_run_method(self):
        """Test the run method."""
        instance = InfraLoom()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
