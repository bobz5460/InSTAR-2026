
from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional


@dataclass
class DataCenterData:
    available_heat_W: float
    coolant_supply_temperature_K: Optional[float] = None
    coolant_return_temperature_K: Optional[float] = None
    coolant_mass_flow_kg_s: Optional[float] = None
    coolant_pressure_Pa: Optional[float] = None

    it_power_W: Optional[float] = None
    facility_power_W: Optional[float] = None
    cooling_electric_power_W: Optional[float] = None
    cooling_load_W: Optional[float] = None
    rejected_heat_W: Optional[float] = None

    server_utilization_fraction: Optional[float] = None
    heat_recovery_enabled: Optional[bool] = None


@dataclass
class DistrictData:
    district_id: str
    heating_demand_W: float

    required_supply_temperature_K: Optional[float] = None
    return_temperature_K: Optional[float] = None
    mass_flow_kg_s: Optional[float] = None

    space_heating_demand_W: Optional[float] = None
    hot_water_demand_W: Optional[float] = None
    industrial_heat_demand_W: Optional[float] = None

    minimum_heat_delivery_W: Optional[float] = None
    maximum_heat_acceptance_W: Optional[float] = None


@dataclass
class WeatherData:
    outdoor_temperature_K: float
    ground_temperature_K: Optional[float] = None
    relative_humidity_fraction: Optional[float] = None
    wind_speed_m_s: Optional[float] = None
    solar_irradiance_W_m2: Optional[float] = None
    atmospheric_pressure_Pa: Optional[float] = None


@dataclass
class GridData:
    carbon_intensity_kg_per_kWh: float
    marginal_carbon_intensity_kg_per_kWh: Optional[float] = None
    electricity_price_USD_per_kWh: Optional[float] = None
    renewable_generation_fraction: Optional[float] = None
    grid_demand_W: Optional[float] = None


@dataclass
class PipeConfig:
    pipe_id: str
    district_id: str
    length_m: float

    inner_diameter_m: Optional[float] = None
    wall_thickness_m: Optional[float] = None
    insulation_thickness_m: Optional[float] = None

    pipe_thermal_conductivity_W_mK: Optional[float] = None
    insulation_conductivity_W_mK: Optional[float] = None

    roughness_m: Optional[float] = None
    nominal_mass_flow_kg_s: Optional[float] = None
    burial_depth_m: Optional[float] = None
    pipe_role: str = "supply"


@dataclass
class HeatPumpConfig:
    heat_pump_id: str
    district_id: str
    rated_heating_capacity_W: float

    nominal_COP: Optional[float] = None
    minimum_COP: Optional[float] = None
    maximum_COP: Optional[float] = None

    min_source_temperature_K: Optional[float] = None
    max_source_temperature_K: Optional[float] = None
    max_sink_temperature_K: Optional[float] = None

    maximum_electric_power_W: Optional[float] = None
    minimum_load_fraction: Optional[float] = None
    performance_map_path: Optional[str] = None


@dataclass
class PumpConfig:
    pump_id: str
    district_id: str

    rated_flow_kg_s: Optional[float] = None
    rated_head_Pa: Optional[float] = None
    rated_electric_power_W: Optional[float] = None
    nominal_efficiency: Optional[float] = None
    performance_map_path: Optional[str] = None


@dataclass
class StorageConfig:
    storage_id: str
    capacity_J: float

    maximum_charge_W: Optional[float] = None
    maximum_discharge_W: Optional[float] = None
    initial_energy_J: Optional[float] = None

    round_trip_efficiency: Optional[float] = None
    standing_loss_fraction_per_hour: Optional[float] = None


@dataclass
class DistrictConfig:
    district_id: str

    household_equivalents: Optional[int] = None
    design_peak_demand_W: Optional[float] = None

    backup_heater_efficiency: Optional[float] = None
    backup_heater_fuel: Optional[str] = None
    backup_heater_capacity_W: Optional[float] = None


@dataclass
class NetworkConfig:
    districts: list[DistrictConfig]
    pipes: list[PipeConfig]
    heat_pumps: list[HeatPumpConfig]

    pumps: list[PumpConfig] = field(default_factory=list)
    storage: list[StorageConfig] = field(default_factory=list)


@dataclass
class SimulationInput:
    timestamp: datetime
    data_center: DataCenterData
    districts: list[DistrictData]
    weather: WeatherData
    grid: GridData


@dataclass
class DatasetMetadata:
    dataset_name: str
    source_name: str
    source_url: Optional[str]

    start_time: datetime
    end_time: datetime
    interval_seconds: int

    is_synthetic: bool = False
    description: str = ""
    license: Optional[str] = None
    version: Optional[str] = None


@dataclass
class DataQualityReport:
    total_records: int
    missing_records: int
    imputed_values: int
    warnings: list[str] = field(default_factory=list)


class DataProvider:

    def __init__(self, file_path: str):
        raise NotImplementedError

    def load_data(self) -> None:
        raise NotImplementedError

    def get_metadata(self) -> DatasetMetadata:
        raise NotImplementedError

    def get_network_config(self) -> NetworkConfig:
        raise NotImplementedError

    def get_all_data(self) -> list[SimulationInput]:
        raise NotImplementedError

    def get_data(self, timestamp: datetime) -> SimulationInput:
        raise NotImplementedError

    def get_time_range(self) -> tuple[datetime, datetime]:
        raise NotImplementedError

    def get_quality_report(self) -> DataQualityReport:
        raise NotImplementedError
