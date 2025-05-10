import unittest
import numpy as np
from src.bat_echolocation_workflow import BatEcholocationAnalyzer

class TestBatEcholocationAnalyzer(unittest.TestCase):
    def test_detects_pulses(self):
        # Simulate a fake ultrasonic pulse train
        fs = 192000
        t = np.linspace(0, 1, fs)
        audio = np.sin(2 * np.pi * 40000 * t) * (np.random.rand(fs) > 0.98)
        analyzer = BatEcholocationAnalyzer()
        result = analyzer.analyze_echolocation(audio)
        self.assertGreater(result["pulse_count"], 0)

if __name__ == "__main__":
    unittest.main()
