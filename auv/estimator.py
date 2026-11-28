"""
auv/estimator.py
Scalar Kalman filter for depth estimation.

Blends a noisy pressure-sensor reading with a simple
"depth doesn't change on its own" process model.
"""


class DepthKalmanFilter:
    """
    One-dimensional Kalman filter for depth.

    Parameters
    ----------
    q : float
        Process noise variance. Higher = trust the sensor more.
    r : float
        Measurement noise variance. Higher = trust the model more.
    initial_depth : float
        Starting depth estimate in metres.
    """

    def __init__(self, q: float = 0.001, r: float = 0.1,
                 initial_depth: float = 0.0):
        self.q = q
        self.r = r
        self.x = initial_depth   # state estimate
        self.p = 1.0              # estimate uncertainty

    def update(self, measurement: float) -> float:
        """
        Run one predict-update cycle.

        Parameters
        ----------
        measurement : float
            Raw depth reading from the sensor (metres).

        Returns
        -------
        float
            Filtered depth estimate.
        """
        # Predict
        x_pred = self.x
        p_pred = self.p + self.q

        # Update
        k = p_pred / (p_pred + self.r)          # Kalman gain
        self.x = x_pred + k * (measurement - x_pred)
        self.p = (1.0 - k) * p_pred

        return self.x