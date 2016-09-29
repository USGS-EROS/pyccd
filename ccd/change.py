from collections import namedtuple
"""Comprehensive data model of the domain is captured in detections,
observation and observations.  Do not modify these data models unless the
actual domain changes.  Data filtering & transformation should take place
in another module AFTER the functions in change.py have run... as
post-processing steps
"""
# this and all other parameters for the model go into ~/.config/ccd_config.py
# minimum_clear_observation_count = 12
#
# 2 for tri-modal; 2 for bi-modal; 2 for seasonality; 2 for linear
# coefficient_categories = {min:4, mid:6, max:8}
#
# number of clear observation / number of coefficients
# clear_observation_threshold = 3
#
# qa_confidence_failure_threshold = 0.25
# permanent_snow_threshold = 0.75


detections = namedtuple("Detections", ['is_change', 'is_outlier',
                                       'rmse', 'magnitude',
                                       'is_curve_start',
                                       'is_curve_end',
                                       'coefficients',
                                       'category'])

observation = namedtuple('Observation', ['coastal_aerosol', 'red', 'green',
                                         'blue', 'nir', 'swir1',
                                         'swir2', 'panchromatic',
                                         'is_cloud', 'is_clear', 'is_snow',
                                         'is_fill', 'is_water',
                                         'qa_confidence'])

observations = namedtuple('Observations', ['date',
                                           'observation',
                                           'detections'])


def is_change():
    pass


def is_outlier():
    pass


def in_expected_range():
    pass


def regress(observation):
    pass


# def detect(observations):
#     """Runs the core ccd algorithm to detect change in the supplied data
#     """
#     [regress(o) for o in sorted(observations, reverse=True)]


def detect(times, observations, fitter_fn, change_detect_fn, meow_size=16, peek_size=3):
    """Runs the core ccd algorithm to detect change in the supplied data

    Args:
        observations: a list of acquisition day numbers, and a list
            for each spectra.
        fitter: a function used to fit observation values and
            acquisition dates for each spectra.
        changer: a function used to detect change; expects a model
            and an observation.
        meow_size: minimum expected observation window needed to
            produce a fit.
        peek_size: number of observations to consider when detecting
            a change.

    Returns:
        Change models for each observation of each spectra.
    """

    # Array index of the model start. Obviously this starts at
    # zero, but as changes are detected, this will be updated
    # with a value of the array index, the new model's start.
    start_ix = 0

    # Array index of where to begin peeking at new observations.
    # Initially, this is the end minimum expected observation
    # window.
    peek_ix = meow_size

    # Result accumulator. Each observation of each spectra has an
    # updated model.
    models = []

    while False: # there are more observations to consider

        # Build a model for each spectra
        times = times[start_ix:meow_size]
        values = observations[:,start_ix:meow_size]

        # If there are enough observations
        if len(meow_values) >= meow_size:
            for spectra in observations:
                model = fitted_model(meow_times, spectra)
        else:
            return results

        # Update models while things appear stable, none of the
        # spectra's peek-windows exhibit change.
        while False:
            # update each spectra's model with peeked values
            # slide the window (increase peek_ix by one)
            # capture model
            results.append(model)

        # ...a change has been detected:
        # - set the new starting index
        # - set the peek index

    return models
