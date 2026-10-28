class SimulationRunner:

    def __init__(self, data_provider, controller, model):
        self.data_provider = data_provider
        self.controller = controller
        self.model = model
        self.results = []

    def setup(self):
        self.data_provider.load_data()

        network = self.data_provider.get_network_config()
        self.model.setup(network)

    def run(self):
        data = self.data_provider.get_all_data()

        for hour in data:

            decisions = self.controller.allocate_heat(hour)

            result = self.model.simulate(hour, decisions)

            self.results.append({
                "timestamp": hour.timestamp,
                "result": result
            })

        return self.results