# SPDX-FileCopyrightText: 2021 International Photoacoustics Standardisation Consortium (IPASC)
# SPDX-FileCopyrightText: 2021 Janek Gröhl
# SPDX-FileCopyrightText: 2021 Lina Hacker
# SPDX-License-Identifier: BSD 3-Clause License

from pacfish.core import MetadataDeviceTags
import copy
import numpy as np


class IlluminationElementCreator(object):
    """
    A IlluminationElementCreator can be used to create illumination elements for the purposes
    of a standardised device representation within the IPASC data format.

    It should be used in the following way::

        iec = IlluminationElementCreator()
        iec.set_illuminator_position(position)
        # ... set other attributes
        element = iec.get_dictionary()

    The `element` dictionary can then be added to the `DeviceMetaDataCreator`.
    """

    def __init__(self):
        """
        Instantiates a IlluminationElementCreator.
        """
        self.illuminator_element_dict = dict()

    def set_illuminator_position(self, illuminator_position: np.ndarray):
        """
        Parameters
        ----------
        illuminator_position:
            is an array of three float values that describe the position of the illumination element in the
            x1, x2, and x3 direction. The units can be found in MetadataDeviceTags.ILLUMINATOR_POSITION.unit.

        Returns
        -------
        None
        """
        self.illuminator_element_dict[MetadataDeviceTags.ILLUMINATOR_POSITION.tag] = illuminator_position

    def set_illuminator_orientation(self, orientation: np.ndarray):
        """
        Parameters
        ----------
        orientation:
            is an array of three float values that describe the orientation of the illumination element in the
            x1, x2, and x3 direction. The units can be found in MetadataDeviceTags.ILLUMINATOR_ORIENTATION.unit.

        Return
        ------
        None
        """
        self.illuminator_element_dict[MetadataDeviceTags.ILLUMINATOR_ORIENTATION.tag] = orientation

    def set_illuminator_geometry(self, shape: np.ndarray):
        """
        Parameters
        ----------
        shape:
            is an array of three float values that describe the shape of the illuminator in the
            x1, x2, and x3 direction. The units can be found in MetadataDeviceTags.ILLUMINATOR_GEOMETRY.unit.

        Return
        ------
        None
        """
        self.illuminator_element_dict[MetadataDeviceTags.ILLUMINATOR_GEOMETRY.tag] = shape

    def set_illuminator_geometry_type(self, illuminator_geometry_type: str):
        """
        Parameters
        ----------
        illuminator_geometry_type:
            The illuminator geometry type defines how to interpret the data in the illuminator geometry field. The following geometry types are currently supported:

            - “CIRCULAR” - defined by a single value that determines the radius of the circle
            - “SPHERE” - defined by a single value that determines the radius of the sphere
            - “CUBOID” - defined by three values that determine the extent of the cuboid in x, y, and z dimensions, before the position and orientation transforms.
            - “MESH” - defined by a STL-formatted string that determines the positions of points and faces before the position and orientation transforms.

        Return
        ------
        None
        """

        if illuminator_geometry_type not in ["CIRCULAR", "SPHERE", "CUBOID", "MESH"]:
            raise ValueError(f"Unsupported geometry_type: {illuminator_geometry_type}")

        self.illuminator_element_dict[MetadataDeviceTags.ILLUMINATOR_GEOMETRY_TYPE.tag] = illuminator_geometry_type

    def set_wavelength_range(self, wl_range: np.ndarray):
        """
        Parameters
        ----------
        wl_range:
            is an array of three float values that describe the minimum wavelength lambda_min,
            the maximum wavelength lambda_max and a metric for the accuracy lambda_accuracy.
            The units can be found in MetadataDeviceTags.WAVELENGTH_RANGE.unit.

        Return
        ------
        None
        """
        self.illuminator_element_dict[MetadataDeviceTags.WAVELENGTH_RANGE.tag] = wl_range

    def set_beam_energy_profile(self, energy_profile: np.ndarray):
        """
        Parameters
        ----------
        energy_profile:
            a two element array [wavelengths, laser_energy] describing the laser energy profile.
            beam energy and wavelengths are also arrays where len(laser_energy) == len(profile)
            The units can be found in MetadataDeviceTags.BEAM_ENERGY_PROFILE.unit.

        Return
        ------
        None
        """
        self.illuminator_element_dict[MetadataDeviceTags.BEAM_ENERGY_PROFILE.tag] = energy_profile
        
    def set_beam_stability_profile(self, stability_profile: np.ndarray):
        """
        Parameters
        ----------
        stability_profile:
            a two element array [wavelengths,laser_stability,] describing the laser stability profile.
            Beam stability and wavelengths are also arrays where len(stability_profile) == len(wavelengths).
            The units can be found in MetadataDeviceTags.BEAM_STABILITY_PROFILE.unit.

        Return
        ------
        None
        """
        self.illuminator_element_dict[MetadataDeviceTags.BEAM_STABILITY_PROFILE.tag] = stability_profile

    def set_pulse_width(self, pulse_width: float):
        """
        Parameters
        ----------
        pulse_width:
            a floating point value describing the pulse width of the laser
            in the units of MetadataDeviceTags.PULSE_WIDTH.unit.

        Return
        ------
        None
        """
        self.illuminator_element_dict[MetadataDeviceTags.PULSE_WIDTH.tag] = pulse_width

    def set_beam_intensity_profile(self, intensity_profile: np.ndarray):
        """
        Parameters
        ----------
        intensity_profile:
            a two element array [wavelengths, intensity_profile] describing the beam itensity profile.
            Wavelengths and intensity_profile are also arrays where len(wavelengths) == len(intensity_profile)
            The units can be found in MetadataDeviceTags.BEAM_INTENSITY_PROFILE.unit.

        Return
        ------
        None
        """
        self.illuminator_element_dict[MetadataDeviceTags.BEAM_INTENSITY_PROFILE.tag] = intensity_profile

    def set_beam_divergence_angles(self, angle: float):
        """
        Parameters
        ----------
        angle:
            a value describing the opening angle of the laser beam from the illuminator shape with respect
            to the orientation vector. This angle is represented by the standard deviation of the beam divergence.
            The units can be found in MetadataDeviceTags.BEAM_DIVERGENCE_ANGLES.unit.
                    
        Return
        ------
        None
            No return value
        """
        self.illuminator_element_dict[MetadataDeviceTags.BEAM_DIVERGENCE_ANGLES.tag] = angle

    def get_dictionary(self):
        """
        Returns a copy of a dictionary describing the created illumination element up to this point.
        Subsequent changes to the element via the `IlluminationElementCreator` will **not** alter the
        dictionary returned by this function. If changes are done this functions needs to be called
        again.

        Return
        ------
        dict
            A dictionary representing the created illumination element.

        """
        return copy.deepcopy(self.illuminator_element_dict)


class DetectionElementCreator(object):
    """
    A DetectionElementCreator can be used to create detection elements for the purposes
    of a standardised device representation within the IPASC data format.

    It should be used in the following way::

        dec = DetectionElementCreator()
        dec.set_detector_position(position)
        # ... set other attributes
        element = dec.get_dictionary()

    The `element` dictionary can then be added to the `DeviceMetaDataCreator`.
    """

    def __init__(self):
        self.detection_element_dict = dict()

    def set_detector_position(self, detector_position: np.ndarray):
        """
        Parameters
        ----------
        detector_position:
            an array of three float values that describe the position of the detection element in the
            x1, x2, and x3 direction. The units can be found in MetadataDeviceTags.DETECTOR_POSITION.unit.

        Return
        ------
        None
            No return value
        """
        self.detection_element_dict[MetadataDeviceTags.DETECTOR_POSITION.tag] = detector_position

    def set_detector_orientation(self, orientation: np.ndarray):
        """
        Parameters
        ----------
        orientation:
            a n array of three float values that describe the orientation of the detector element in the
            x1, x2, and x3 direction. The units can be found in MetadataDeviceTags.DETECTOR_ORIENTATION.unit.

        Return
        ------
        None
            No return value
        """
        self.detection_element_dict[MetadataDeviceTags.DETECTOR_ORIENTATION.tag] = orientation

    def set_detector_geometry_type(self, geometry_type: str):
        """
        Parameters
        ----------
        geometry_type:
            The detector geometry type defines how to interpret the data in the detector geometry field. The following geometry types are currently supported:

            - “CIRCULAR” - defined by a single value that determines the radius of the circle
            - “SPHERE” - defined by a single value that determines the radius of the sphere
            - “CUBOID” - defined by three values that determine the extent of the cuboid in x, y, and z dimensions, before the position and orientation transforms.
            - “MESH” - defined by a STL-formatted string that determines the positions of points and faces before the position and orientation transforms.

        Return
        ------
        None
            No return value
        """

        if geometry_type not in ["CIRCULAR", "SPHERE", "CUBOID", "MESH"]:
            raise ValueError(f"Unsupported geometry_type: {geometry_type}")

        self.detection_element_dict[MetadataDeviceTags.DETECTOR_GEOMETRY_TYPE.tag] = geometry_type

    def set_detector_geometry(self, geometry):
        """
        Parameters
        ----------
        geometry:
            a three element array [x1, x2, x3] describing the extent of the detector size in x1, x2, and x3 direction.
            The units can be found in MetadataDeviceTags.DETECTOR_SIZE.unit.

        Return
        ------
        None
            No return value
        """
        self.detection_element_dict[MetadataDeviceTags.DETECTOR_GEOMETRY.tag] = geometry

    def set_frequency_response(self, frequency_response: np.ndarray):
        """
        Parameters
        ----------
        frequency_response:
            a two element array [frequency, response] describing the frequency response of the detector.
            Frequency and response are also arrays where len(frequency) == len(response).
            The units can be found in MetadataDeviceTags.FREQUENCY_RESPONSE.unit.
        Return
        ------
        None
            No return value
        """
        self.detection_element_dict[MetadataDeviceTags.FREQUENCY_RESPONSE.tag] = frequency_response

    def set_angular_response(self, angular_response: np.ndarray):
        """
        Parameters
        ----------
        angular_response:
            a two element array [angles, response] describing the angular response of the detecor.
            Angles and response are also arrays where len(angles) == len(response).
            The units can be found in MetadataDeviceTags.ANGULAR_RESPONSE.unit.

        Return
        ------
        None
            No return value
        """
        self.detection_element_dict[MetadataDeviceTags.ANGULAR_RESPONSE.tag] = angular_response

    def get_dictionary(self):
        """
        Returns a copy of a dictionary describing the created detection element up to this point.
        Subsequent changes to the element via the `DetectionElementCreator` will **not** alter the
        dictionary returned by this function. If changes are done this functions needs to be called
        again.

        Return
        ------
        dict
            A dictionary representing the created detection element.

        """
        return copy.deepcopy(self.detection_element_dict)


class DeviceMetaDataCreator(object):
    """
    A helper class to create a dictionary that describes a digital device twin according to the
    IPASC data format. In the interplay with the `DetectionElementCreator` and the `IlluminationElementCreator`,
    elements can be added to the representation.

    Example::

        dmdc = DeviceMetaDataCreator()
        dmdc.set_general_information(uuid, fov)
        for _ in range(num_detection_elements):
            dec = DetectionElementCreator()
            dec.set_detector_position(position)
            # ... set other attributes
            element = dec.get_dictionary()
            dmdc.add_detection_element(element)
        for _ in range(num_illuminators):
            iec = IlluminationElementCreator()
            iec.set_illuminator_position(position)
            # ... set other attributes
            element = iec.get_dictionary()
            dmdc.add_detection_element(element)
        device_metadata_dict = dmdc.finalize_device_meta_data()

    """

    def __init__(self):
        """
        Initialises the DeviceMetaDataCreator.
        """
        self.GENERAL = MetadataDeviceTags.GENERAL.tag
        self.ILLUMINATORS = MetadataDeviceTags.ILLUMINATORS.tag
        self.DETECTORS = MetadataDeviceTags.DETECTORS.tag
        self.device_dict = dict()
        self.device_dict[self.GENERAL] = dict()
        self.device_dict[self.ILLUMINATORS] = dict()
        self.device_dict[self.DETECTORS] = dict()
        self.next_detector_uid = 0
        self.next_illuminator_uid = 0

    def set_general_information(self, uuid: str, fov: np.ndarray):
        """
        Parameters
        ----------
        uuid:
            is a string that uniquely identifies the photoacoustic device
        fov:
            is an array of six float values that describe the extent of the field of view of the device in the
            x1, x2, and x3 directions: [x1_start, x1_end, x2_start, x2_end, x3_start, x3_end].

        Return
        ------
        None
            No return value
        """
        self.device_dict[self.GENERAL][MetadataDeviceTags.UNIQUE_IDENTIFIER.tag] = uuid
        self.device_dict[self.GENERAL][MetadataDeviceTags.FIELD_OF_VIEW.tag] = fov

    def add_detection_element(self, detection_element: dict):
        """
        Parameters
        ----------
        detection_element:
            is a dictionary for the detection element specific parameters

        Return
        ------
        None
            No return value
        """
        self.device_dict[self.DETECTORS][str(self.next_detector_uid).zfill(10)] = detection_element
        self.next_detector_uid += 1

    def add_illumination_element(self, illumination_element: dict):
        """
        Parameters
        ----------
        illumination_element:
            is a dictionary for the illumination element specific parameters

        Return
        ------
        None
            No return value
        """
        self.device_dict[self.ILLUMINATORS][str(self.next_illuminator_uid).zfill(10)] = illumination_element
        self.next_illuminator_uid += 1

    def finalize_device_meta_data(self):
        """
        Returns a copy of a dictionary describing the created device up to this point.
        Subsequent changes to the element via the `DeviceMetaDataCreator` will **not** alter the
        dictionary returned by this function. If changes are done this functions needs to be called
        again.

        Return
        ------
        dict
            A dictionary representing the created digital device twin.

        """

        self.device_dict[self.GENERAL][MetadataDeviceTags.NUMBER_OF_DETECTION_ELEMENTS.tag] = len(
            self.device_dict[self.DETECTORS])
        self.device_dict[self.GENERAL][MetadataDeviceTags.NUMBER_OF_ILLUMINATION_ELEMENTS.tag] = len(
            self.device_dict[self.ILLUMINATORS])

        return copy.deepcopy(self.device_dict)
