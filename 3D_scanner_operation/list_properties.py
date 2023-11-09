
"""
Version: 1.0
Capture images using usb cameras controller by raspberry pi clutsers
Author: suxing liu
Author-email: suxingliu@gmail.com

USAGE

python list_properties.py

"""

import argparse
import subprocess, os
import sys

import common
import TIS
import cv2

from gi.repository import Tcam, Gst

import sys
import gi

import sys

gi.require_version("Tcam", "0.1")
gi.require_version("Gst", "1.0")

# list all cameras connecting to the motherboard 
def list_devices():
    
    #create a source element to retrieve a device list through it
    source = Gst.ElementFactory.make("tcambin")
    
    #retrieve all available serial numbers
    serials = source.get_device_serials()
    
    print("Available devices:")

    #output all device infos
    for single_serial in serials:

        # This returns someting like:
        # (True, name='DFK Z12GP031',
        # identifier='The Imaging Source Europe GmbH-11410533', connection_type='aravis')
        # The identifier is the name given by the backend
        # The connection_type identifies the backend that is used.
        #     Currently 'aravis', 'v4l2' and 'unknown' exist
        (return_value, model,identifier, connection_type) = source.get_device_info(single_serial)

        # return value would be False when a non-existant serial is used
        # since we are iterating get_device_serials this should not happen
        if return_value:
            
            print("Model: {} Serial: {} Type: {}".format(model, single_serial, connection_type))
    return serials



def main():
    
    Gst.init(sys.argv)  # init gstreamer

    # set this to a specific camera serial if you
    # do not want to use the default camera
    serial = None

     #retrieve a device list
    serials = list_devices()
    
    
    cam_list = []
    
    for idx, serial in enumerate(serials):
        
        #parameter_set = [x.strip() for x in resoltuion.split(',')]
        
        #initialize camera class objects
        #cam_list.append(TIS.TIS(serial, 3872, 2764, 3, 1, True))
        
        cam_list.append(TIS.TIS(serial, int(3872), int(2764), int(3), int(1), True))
        
        #Start the pipeline
        cam_list[idx].Start_pipeline()
        
        # Check, whether gain auto is enabled. If so, disable it.
        if cam_list[idx].Get_Property("Gain Auto").value:
            cam_list[idx].Set_Property("Gain Auto",False)
            #print("Gain Auto now : %s " % cam.Get_Property("Gain Auto").value)
            cam_list[idx].Set_Property("Gain",208)
        
        # we create a source element to retrieve a property list through it
        camera = Gst.ElementFactory.make("tcambin")

        # serial is defined, thus make the source open that device
        if serial is not None:
            camera.set_property("serial", serial)
        
        property_names = camera.get_tcam_property_names()

        for name in property_names:

            (ret, value,
             min_value, max_value,
             default_value, step_size,
             value_type, flags,
             category, group) = camera.get_tcam_property(name)

            if not ret:
                print("could not receive value {}".format(name))
                continue

            if value_type == "integer" or value_type == "double":
                print("{}({}) value: {} default: {} min: {} max: {} grouping: {} - {}".format(name,
                                                                                              value_type,
                                                                                              value, default_value,
                                                                                              min_value, max_value,
                                                                                              category, group))
            elif value_type == "string":
                print("{}(string) value: {} default: {} grouping: {} - {}".format(name,
                                                                                  value,
                                                                                  default_value,
                                                                                  category,
                                                                                  group))
            elif value_type == "button":
                print("{}(button) grouping is {} -  {}".format(name,
                                                               category,
                                                               group))
            elif value_type == "boolean":
                print("{}(boolean) value: {} default: {} grouping: {} - {}".format(name,
                                                                                   value,
                                                                                   default_value,
                                                                                   category,
                                                                                   group))
            elif value_type == "enum":
                enum_entries = camera.get_tcam_menu_entries(name)

                print("{}(enum) value: {} default: {} grouping {} - {}".format(name,
                                                                                   value,
                                                                                   default_value,
                                                                                   category,
                                                                                   group))
                print("Entries: ")
                for entry in enum_entries:
                    print("\t {}".format(entry))
            else:
                print("This should not happen.")
       
  


if __name__ == "__main__":
    
    
    sys.exit(main())


    
    
