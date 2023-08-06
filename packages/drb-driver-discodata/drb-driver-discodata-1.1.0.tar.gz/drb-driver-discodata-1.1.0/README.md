# DISCODATA driver
This drb-driver-discodata module implements DISCODATA databases access with DRB data model. It is able to navigates among the database contents.

For more information about DISCODATA see:  https://discodata.eea.europa.eu/Help.html

## DISOCDATA Factory and DISCODATA Node
The module implements the basic factory model defined in DRB in its node resolver. Based on the python entry point mechanism, this module can be dynamically imported into applications.

The entry point group reference is `drb.driver`.<br/>
The driver name is `netcdf`.<br/>
The factory class `DrbDiscodataFactory` is encoded into `drb.drivers.factory`
module.<br/>


## limitations
The current version does not manage child modification and insertion. `DrbDiscodataNode` is currently read only.
The factory to build DrbDiscodataNode supports file directly opening it with path, for other implementation ByteIO or BufferedIOBase, they are manged with a local temporary file, removed when the node is closed..

## Using this module
To include this module into your project, the `drb-driver-discodata`  module shall be referenced into `requirements.txt` file, or the following pip line can be run:
```commandline
pip install drb-driver-discodata
```


