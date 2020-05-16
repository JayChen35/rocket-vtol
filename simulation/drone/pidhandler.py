class PDHandler:
    def __init__(self, Kp, Kd, dt):
        self.last_error = None
        self.Kp = Kp
        self.Kd = Kd
        self.dt = dt

    
    def calculate(self, error):
#        return self.Kp * error
        de = 0 if self.last_error is None else error - self.last_error
        self.last_error = error
        p = self.Kp * error
        d = self.Kd * (de / self.dt)
#        return p
        return p, d, p + d