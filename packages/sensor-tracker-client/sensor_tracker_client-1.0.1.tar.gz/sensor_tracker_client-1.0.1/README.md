
Sensor Tracker Client Library
=============

This library provides a pure Python interface for the Sensor Tracker Client


Installing
----------

Install through pip:

    pip install git+https://gitlab.oceantrack.org/ceotr/metadata-tracker/sensor_tracker_client.git


Usage Examples
--------------
 
The API is exposed via the ``sensor_tracker_client``  class.

For starters, the library is using singleton pattern. The object will be instantiated as soon as you import the class.

    >>> from sensor_tracker_client import sensor_tracker_client as stc

Make sure to set up the basic configurations before using the other functions. It needs to be configured only once at the beginning of the script.

    >>> # Basic setup
    >>> stc.HOST = "your sensor tracker host url"
    >>> stc.basic.DEBUG = True # Turn on the debug mode, the default is False
    >>> # When debug mode is on, the HOST link will point to DEBUG HOST.
    >>> stc.basic.DEBUG_HOST = 'http://127.0.0.1:8000/' # Default DEBUG HOST is "http://127.0.0.1:8000/"

**NOTE**: As the debug mode is off, ``sensor_tracker_api`` is pointed to the CEOTR [Sensor Tracker API server](http://bugs.ocean.dal.ca/sensor_tracker/)


The sensor tracker api requires the use of token or username and password for POST and PUT operations. GET doesn't require authentication.

    >>> stc.authentication.token = "your_token"
    >>> # or
    >>> stc.authentication.username = "your_username"
    >>> stc.authentication.password = "your_password"

To see if your credentials are successful:

    >>> # To verify the username and password
    >>> stc.authentication.username = "your_username"
    >>> stc.authentication.password = "your_password"
    >>> print(stc.authentication.is_username_and_password_valid())
    >>>
    >>> # To verify the token
    >>> stc.authentication.token = "your_token"
    >>> try:
    >>>     print(stc.authentication.token)
    >>> except AuthenticationError:
    >>>     print("token is incorrect")
    
### cache
    
    # sta.cache_on = True

### GET Operations

The usage format of get operation:

    # For full list
    response_data = stc.target_model.get()
    # For filter
    response_data = stc.target_model.get({"filter name":"filter value"})
    # get object by pk
    response_data = stc.target_model.get(pk)

##### Institutions

To fetch full list of institutions

    >>> institution_res = stc.institution.get()

To fetch institutions with name OTN

    >>> institution_res2 = stc.institution.get({"name": "OTN"})
    
To fetch institution obj with primary key 1
    
    >>> institution_res3 = stc.institution.get(1)


##### Response data

All GET operations will return a ``response_data`` object, which contains results and can be converted into
different format such as dictionary
   
    >>> institution_res_dict = institution_res.dict
   
##### Project

To fetch full list of project

    >>> project_res = stc.project.get()

To fetch project with name "Gulf of St. Lawrence Animal Tracking for OTN"

    >>> project_res2 = stc.project.get({"name": "Gulf of St. Lawrence Animal Tracking for OTN"})
   
To fetch project obj with primary key 1
    
    >>> project_res3 = stc.project.get(1)

##### Manufacturer

To fetch full list of manufacturers

    >>> manufacturer_res = stc.manufacturer.get()

To fetch manufacturer with name "Teledyne Webb"

    >>> manufacturer_res2 = stc.manufacturer.get({"name": "Teledyne Webb"})
    
To fetch manufacturer obj with primary key 1
    
    >>> manufacturer_res3 = stc.manufacturer.get(1)

##### Instrument

To fetch full list of instruments

    >>> instrument_res = stc.instrument.get()

To fetch instrument with identifier "c"

    >>> instrument_res2 = stc.instrument.get({"identifier": "c"})

To fetch instrument on a platform

    >>> instrument_res3 = stc.instrument.get({"platform_name": "otn200"})

To fetch instrument by deployment

    >>> instrument_res4 = stc.instrument.get({"platform_name": "otn200", "start_time": "2017-08-02 19:37:38"})
    >>> instrument_res5 = stc.instrument.get({"platform_name": "otn200", "start_time": "2017-08-02"})

To fetch instrument obj with primary key 1
    
    >>> instrument_res6 = stc.instrument.get(1)
    
##### Instrument_on_platform

To fetch full list of instrument on platform

    >>> instrument_on_platform_res = stc.instrument_on_platform.get()

To fetch instrument on platform by platform name

    >>> instrument_on_platform_res2 = stc.instrument_on_platform.get({"platform_name": "otn200"})

To fetch instrument on platform by instrument identifier

    >>> instrument_on_platform_res5 = stc.instrument_on_platform.get({"identifier": "c"})


To fetch instrument_on_platform obj with primary key 1
    
    >>> instrument_on_platform_res6 = stc.instrument_on_platform.get(1)
    
##### Sensor

To fetch full list of sensor

    >>> sensor_res = stc.sensor.get({"output": "all"})

To fetch all sensors which are included in output

    >>> sensor_res = stc.sensor.get({"output": True}) # output:False means not include in output

Sensors can be filter by identifier, short_name, and long_name

    >>> sensor_res2 = stc.sensor.get({"identifier": "RMSe", "output": True})
    >>> sensor_res2 = stc.sensor.get({"short_name": "short_name"})
    >>> sensor_res2 = stc.sensor.get({"long_name": "long_name"})

Sensors can be filtered by platform or deployment

    >>> sensor_res3 = stc.sensor.get({"platform_name": "otn200", "start_time": "2017-08-02 19:37:38"})
    >>> sensor_res4 = stc.sensor.get({"platform_name": "otn200"})
    >>> sensor_res5 = stc.sensor.get({"platform_name": "otn200", "start_time": "2017-08-02"})


To fetch sensor obj with primary key 1
    
    >>> sensor_res6 = stc.sensor.get(1)
    
##### Sensor on Instrument

To fetch a full list of sensor_on_instrument

    >>> ret = stc.sensor_on_instrument.get()

To fetch sensor on instrument for a deployment

    >>> ret = stc.sensor_on_instrument.get({"platform_name": "otn200", "deployment_start_time": "2017-08-02 19:37:38"})

To fetch sensor_on_instrument obj with primary key 1
    
    >>> sensor_on_instrument_res = stc.sensor_on_instrument.get(1)

##### platform type

To fetch a full list of platform type

    >>> platform_type_res = stc.platform_type.get()

To fetch platform type by model name

    >>> platform_type_res2 = stc.platform_type.get({"model": "Mooring"})

By default, the given model name should be match the target platform name; alternatively, you can specific filter "how" which can be "contains" or "regex"

    >>> platform_type_res3 = stc.platform_type.get({"model": "slocum", "how": "contains"}) # return all platform type which model contains word "slocum", case in sensitive
    >>> platform_type_res4 = stc.platform_type.get({"model": "Slocum Glider G\d", "how": "regex"}) # return all platform types which model match the regular expression

To fetch platform_type obj with primary key 1
    
    >>> platform_type5 = stc.platform_type.get(1)


###### Power

To fetch the full list of power type

    >>> power_res = stc.power.get()

To filter sensor list by power name

    >>> power_res2 = stc.power.get({"name":"power_name"})
    
To fetch power obj with primary key 1
    
    >>> power3 = stc.power.get(1)

##### Deployment

To fetch the full list of deployment

    deployment_res = stc.deployment.get()

To get the deployments by platform name

    >>> deployment_res = stc.deployment.get({"platform_name": "otn200"})

To get the deployment by platform_type

    >>> deployment_res2 = stc.deployment.get({"model": "Slocum Glider G\d", "how": "regex"})
    >>> deployment_res3 = stc.deployment.get({"model": "Slocum", "how": "contains"})

To fetch deployment obj with primary key 1
    
    >>> deployment4 = stc.deployment.get(1)
    
##### Deployment comment

To get full list of deployment comment

    >>> deployment_comment = stc.deployment_comment.get()


    # user detail were hidden
    >>> deployment_comment = stc.deployment_comment.get({"platform_name": "dal556", "depth": 1})
    >>> deployment_comment_res2 = stc.deployment_comment.get({"platform_name": "dal556", "depth": 0})

To fetch deployment_comment obj with primary key 1
    
    >>> deployment_comment3 = stc.deployment_comment.get(1)


### POST Operations

To create an new object on sensor tracker database

The credential must be provided before using any POST operations otherwise it will throw an exception,
POST operations' format is similar to GET operations

    res = stc.target_model.post({"a_data_file": "field_value"})

### PATCH Operations
PATCH is used for "modify" capabilities. The PATCH request only needs to contain the changes to the resource, not the complete resource

patch operation is available for institution, project, manufacturer, instrument, instrument_on_platform, sensor, platform_type, platform, power,
deployment, sensor_on_instrument

usage format:
sta.target_model.patch(instance_id, content_dict)

### Author

![alt text](http://ceotrstg.ocean.dal.ca/static/images/logos/CEOTR-Logo-Port-sm.png?v=23)

[CEOTR data](http://ceotr.ocean.dal.ca)

### License
[The License](./LICENSE.md)
