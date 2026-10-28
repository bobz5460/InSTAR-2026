class DataCenterData:
    def __init__(self):
        self.available_heat_W = None
        self.coolant_supply_temperature_K = None
        self.coolant_return_temperature_K = None
        self.coolant_mass_flow_kg_s = None

        self.it_power_W = None
        self.facility_power_W = None
        self.cooling_electric_power_W = None
        self.rejected_heat_W = None
        self.server_utilization = None


class DistrictData:
    def __init__(self):
        self.district_id = None
        self.heating_demand_W = None

        self.required_supply_temperature_K = None
        self.return_temperature_K = None

        self.space_heating_demand_W = None
        self.hot_water_demand_W = None

        self.minimum_heat_W = None
        self.maximum_heat_W = None


class WeatherData:
    def __init__(self):
        self.outdoor_temperature_K = None
        self.ground_temperature_K = None
        self.humidity = None
        self.wind_speed_m_s = None


class GridData:
    def __init__(self):
        self.carbon_intensity_kg_per_kWh = None
        self.electricity_price_USD_per_kWh = None
        self.renewable_fraction = None


class PipeConfig:
    def __init__(self):
        self.pipe_id = None
        self.district_id = None
        self.length_m = None

        self.inner_diameter_m = None
        self.wall_thickness_m = None
        self.insulation_thickness_m = None

        self.thermal_conductivity = None
        self.insulation_conductivity = None

        self.mass_flow_kg_s = None
        self.burial_depth_m = None
        self.pipe_role = None


class HeatPumpConfig:
    def __init__(self):
        self.heat_pump_id = None
        self.district_id = None

        self.rated_heating_capacity_W = None
        self.nominal_COP = None
        self.minimum_COP = None
        self.maximum_COP = None

        self.min_source_temperature_K = None
        self.max_sink_temperature_K = None
        self.maximum_electric_power_W = None


class PumpConfig:
    def __init__(self):
        self.pump_id = None
        self.district_id = None

        self.rated_flow_kg_s = None
        self.rated_head_Pa = None
        self.rated_electric_power_W = None
        self.efficiency = None


class StorageConfig:
    def __init__(self):
        self.storage_id = None
        self.capacity_J = None

        self.maximum_charge_W = None
        self.maximum_discharge_W = None
        self.initial_energy_J = None
        self.efficiency = None
        self.heat_loss_per_hour = None


class DistrictConfig:
    def __init__(self):
        self.district_id = None
        self.household_equivalents = None
        self.design_peak_demand_W = None

        self.backup_heater_efficiency = None
        self.backup_heater_fuel = None
        self.backup_heater_capacity_W = None


class NetworkConfig:
    def __init__(self):
        self.districts = []
        self.pipes = []
        self.heat_pumps = []
        self.pumps = []
        self.storage = []


class SimulationInput:
    def __init__(self):
        self.timestamp = None
        self.data_center = None
        self.districts = []
        self.weather = None
        self.grid = None


class DatasetMetadata:
    def __init__(self):
        self.dataset_name = None
        self.source_name = None
        self.source_url = None

        self.start_time = None
        self.end_time = None
        self.interval_seconds = None

        self.is_synthetic = False
        self.description = None


class DataQualityReport:
    def __init__(self):
        self.total_records = 0
        self.missing_records = 0
        self.imputed_values = 0
        self.warnings = []


class DataProvider:

    def __init__(self, file_path):
        raise NotImplementedError

    def load_data(self):
        raise NotImplementedError

    def get_metadata(self):
        raise NotImplementedError

    def get_network_config(self):
        raise NotImplementedError

    def get_all_data(self):
        raise NotImplementedError

    def get_data(self, timestamp):
        raise NotImplementedError

    def get_time_range(self):
        raise NotImplementedError

    def get_quality_report(self):
        raise NotImplementedError