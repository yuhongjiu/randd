import pytest
import numpy as np
from randd.rdmetrics import SsimplusEgrdCodecComparison1d


# Test data for 1d case
h264_quality_1d = np.array(
    [34.31, 71.97, 83.44, 88.02, 90.94, 92.74, 93.91, 94.87, 95.35,
     96.06, 96.22, 96.74, 97.03, 97.06, 97.12, 97.38, 97.69, 97.89,
     98.01, 98.01, 98.01, 98.02, 98.03, 98.04, 98.06, 98.14, 98.27,
     98.35, 98.47, 98.6, 98.67, 98.73, 98.81, 98.88, 98.94, 98.98,
     98.99, 99., 99., 99.]
)

vp9_quality_1d = np.array(
    [75.56, 88.71, 91.98, 93.49, 95.15, 95.98, 96.54, 97.03, 97.4,
     97.57, 97.74, 97.89, 98.1, 98.3, 98.38, 98.48, 98.55, 98.57,
     98.66, 98.69, 98.72, 98.81, 98.86, 98.89, 98.89, 98.9, 98.91,
     98.91, 98.91, 98.92, 98.93, 98.95, 98.95, 98.95, 98.95, 98.95,
     98.96, 98.96, 98.96, 98.96]
)

bitrates = np.array(
    [100.,  200.,  300.,  400.,  500.,  600.,  700.,  800.,  900.,
     1000., 1100., 1200., 1300., 1400., 1500., 1600., 1700., 1800.,
     1900., 2000., 2100., 2200., 2300., 2400., 2500., 2600., 2700.,
     2800., 2900., 3000., 3100., 3200., 3300., 3400., 3500., 3600.,
     3700., 3800., 3900., 4000.]
)

uniform_sample_idx_1d = np.array([0, 2, 11, 39])

uncertainty_sample_idx_1d = np.array([0, 2, 8, 18])

range_r = np.array([100., 4000.])

expected_result = np.array([[2.003466, -44.592343],
                            [2.190101, -45.964366]])


class TestEgrdRdmetrics:
    def test_01(self):
        egrd = SsimplusEgrdCodecComparison1d()
        bitrates_uniform = bitrates[uniform_sample_idx_1d]
        h264_quality_uniform = h264_quality_1d[uniform_sample_idx_1d]
        vp9_quality_uniform = vp9_quality_1d[uniform_sample_idx_1d]

        rd_metrics = egrd(
            bitrates_uniform, h264_quality_uniform,
            bitrates_uniform, vp9_quality_uniform,
            range_r=range_r
        )
        assert np.allclose(rd_metrics, expected_result[0], rtol=1e-4, equal_nan=True)

    def test_02(self):
        egrd = SsimplusEgrdCodecComparison1d()
        bitrates_uncertainty = bitrates[uncertainty_sample_idx_1d]
        h264_quality_uncertainty = h264_quality_1d[uncertainty_sample_idx_1d]
        vp9_quality_uncertainty = vp9_quality_1d[uncertainty_sample_idx_1d]

        rd_metrics = egrd(
            bitrates_uncertainty, h264_quality_uncertainty,
            bitrates_uncertainty, vp9_quality_uncertainty,
            range_r=range_r
        )
        assert np.allclose(rd_metrics, expected_result[1], rtol=1e-4, equal_nan=True)


if __name__ == "__main__":
    pytest.main([__file__])
