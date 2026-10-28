from simulation import SimulationRunner
from controller import Controller
from modelica_interface import ModelicaInterface
from data_provider import FakeDataProvider


def main():

    provider = FakeDataProvider()
    controller = Controller()
    model = ModelicaInterface()

    simulation = SimulationRunner(
        provider,
        controller,
        model
    )

    simulation.setup()

    results = simulation.run()

    for hour in results:
        print(hour)


if __name__ == "__main__":
    main()