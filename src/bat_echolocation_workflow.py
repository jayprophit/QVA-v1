import numpy as np
from scipy.signal import spectrogram

class BatEcholocationAnalyzer:
    def analyze_echolocation(self, audio_input):
        # Compute spectrogram and detect ultrasonic pulses
        f, t, Sxx = spectrogram(audio_input, fs=192000)  # 192kHz sample rate
        ultrasonic_band = (f > 20000) & (f < 120000)  # 20kHz to 120kHz
        pulse_energy = Sxx[ultrasonic_band].sum(axis=0)
        pulse_times = t[pulse_energy > np.percentile(pulse_energy, 95)]
        return {"pulse_times": pulse_times.tolist(), "pulse_count": len(pulse_times)}
