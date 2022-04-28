from src.controllers.calculator import Calculator

class Routes():
    def __init__(self, api):
        api.add_resource(Calculator, '/calculate')