class pd_controller():

    def __init__(self):
        # Set controller gains
        self.Kp = 0.15
        self.Kd = 0.6
    
    def control_action(self, e, e_1) -> float:
        u = self.Kp*e + self.Kd*(e-e_1)     # Generate controller output
        return u