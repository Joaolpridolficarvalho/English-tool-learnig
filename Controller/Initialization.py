class Initialization:
        def __init__(self):
            pass
        @abs
        def activate_automatic_initialization(self, system):
            system.enable_automatic_initialization()

        @abs
        def deactivate_automatic_initialization(self, system):
            system.disable_automatic_initialization()