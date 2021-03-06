import math

from coefficients import Coefficients, Constants
from data_models import States


def canopy_heat_capacity(states: States) -> float:
    """The heat capacity of the canopy
    Equation 8.20

    :return: [J K^(-1) m^(-2)]
    """
    return Constants.cap_Leaf * states.leaf_area_index


def internal_external_canopy_heat_capacity(lumped_cover_heat_capacity: float) -> float:
    """The heat capacity of the canopy
    Equation 8.21

    :param lumped_cover_heat_capacity: the total heat capacity of the lumped cover
    :return: [J K^(-1) m^(-2)]
    """
    return 0.1 * lumped_cover_heat_capacity


def heating_pipe_heat_capacity():
    # Equation 8.22
    pipe_length = Coefficients.Heating.pipe_length
    phi_external_pipe = Coefficients.Heating.phi_external_pipe
    phi_internal_pipe = Coefficients.Heating.phi_internal_pipe
    steel_density = Constants.steel_density
    water_density = Constants.water_density
    c_pSteel = Constants.c_pSteel
    c_pWater = Constants.c_pWater
    return 0.25 * math.pi * pipe_length(
        (phi_external_pipe ** 2 - phi_internal_pipe ** 2) * steel_density * c_pSteel + phi_internal_pipe ** 2 * water_density * c_pWater)


def remaining_object_heat_capacity(h_obj, rho_obj, c_p_obj):
    # Equation 8.23
    return h_obj * rho_obj * c_p_obj


def air_compartment_water_vapor_capacity(states: States):
    # Equation 8.25
    M_Water = Constants.M_Water
    air_height = Coefficients.Construction.air_height
    M_Gas = Constants.M_Gas
    air_t = states.air_t
    return M_Water * air_height / ((air_t + 273.15) * M_Gas)
