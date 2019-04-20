""" Package constants """

__author__ = "Vince Reuter"
__email__ = "vreuter@virginia.edu"


# Compute-related
COMPUTE_SETTINGS_VARNAME = ["DIVCFG", "PEPENV"]
DEFAULT_COMPUTE_RESOURCES_NAME = "default"
OLD_COMPUTE_KEY = "compute"
NEW_COMPUTE_KEY = "compute_packages"
COMPUTE_CONSTANTS = ["COMPUTE_SETTINGS_VARNAME",
                     "DEFAULT_COMPUTE_RESOURCES_NAME"]

# Project-related
DERIVATIONS_DECLARATION = "derived_attributes"
IMPLICATIONS_DECLARATION = "implied_attributes"
SAMPLE_INDEPENDENT_PROJECT_SECTIONS = ["metadata", DERIVATIONS_DECLARATION,
                                       IMPLICATIONS_DECLARATION, "trackhubs"]
PROJECT_CONSTANTS = ["IMPLICATIONS_DECLARATION",
                     "SAMPLE_INDEPENDENT_PROJECT_SECTIONS"]

# Other
GENERIC_PROTOCOL_KEY = "*"
OTHER_CONSTANTS = ["GENERIC_PROTOCOL_KEY"]


__all__ = COMPUTE_CONSTANTS + PROJECT_CONSTANTS + OTHER_CONSTANTS
