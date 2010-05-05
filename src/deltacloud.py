#!/usr/bin/python
#
# Python client for deltacloud which insulates users from having to deal with HTTP and REST directly.
#
# Authors: Sayli Karmarkar

import sys
import httplib
import base64
import os
import urllib
import time
import simplejson as json

class MissingEnvVarException(Exception):
    def __init__(self, envVar):
        self.envVar = envVar
    def __str__(self):
        return "Missing environment variable '%s'" % (self.envVar)

class RestlibException(Exception):
    pass

class Restlib(object):
    """
     A wrapper around httplib to make rest calls easier
    """
    def __init__(self, host, port, apihandler):
        self.host = host
        self.port = port
        self.apihandler = apihandler
        self.headers = { "Content-Type" : "application/x-www-form-urlencoded",
                         "Accept" : "application/json"}

    def _request(self, request_type, method, info=None):
        handler = self.apihandler + method
        conn = httplib.HTTPConnection(self.host, self.port)
        conn.request(request_type, handler, body=info, headers=self.headers)
        response = conn.getresponse()
	rinfo = response.read()
        if not len(rinfo):
            return None
        return json.loads(rinfo)
        
    def request_get(self, method):
        return self._request("GET", method)

    def request_post(self, method, params=""):
        return self._request("POST", method, params)


""" 
Generic deltacloud object
"""
class DeltaCloudObject(dict):
    
    def __init__(self, raw_json, connection=None):
        self.connection = connection
	for key in raw_json.keys():
            self[key] = raw_json.get(key)
   	
    def __setattr__(self, attr, value):
        self[attr] = value

    def __getattr__(self, attr):
        return self[attr]
    	
""" 
Deltacloud objects
"""
class DeltaCloudImage(DeltaCloudObject):

   def run(self, opts):
       cmd = '/instances'
       opts["image_id"] = self.id

       return DeltaCloudInstance(self.connection.conn.request_post(cmd, urllib.urlencode(opts))['instance'], self.connection)

class DeltaCloudRealm(DeltaCloudObject):
	pass

class DeltaCloudFlavor(DeltaCloudObject):
	pass	

class DeltaCloudVolume(DeltaCloudObject):
	pass

class DeltaCloudSnapshot(DeltaCloudObject):
	pass

class DeltaCloudInstance(DeltaCloudObject):

    def start(self):
       	cmd = '/instances/' + self.id + '/start'
        try:
            retcode =  self.connection.conn.request_post(cmd)
        except RestlibException, e:
            return False
        return  retcode

    def stop(self):
       	cmd = '/instances/' + self.id + '/stop'
        try:
            retcode =  self.connection.conn.request_post(cmd)
        except RestlibException, e:
            return False
        return  retcode
    
    def reboot(self):
       	cmd = '/instances/' + self.id + '/reboot'
        try:
            retcode =  self.connection.conn.request_post(cmd)
        except RestlibException, e:
            return False
        return  retcode
	

class DeltaCloud:

    def __init__(self, username, password, host='0.0.0.0', port=3001, handler="/api"):
        self.host = host
        self.port = port
        self.handler = handler
        self.conn = None

	self.username = username
	self.password = password

	# Initialize Connection
        self.setUp()

        # Setup Authentication
        encoded = base64.encodestring(':'.join((self.username,self.password)))
        basic = 'Basic %s' % encoded[:-1]
        self.conn.headers['Authorization'] = basic

    def setUp(self):
        self.conn = Restlib(self.host, self.port, self.handler)

    def shutDown(self):
        self.conn.close()

    """ 
    Flavors
    """
    def get_all_flavors(self):
	flavors = []
        for item in self.conn.request_get('/hardware_profiles')['hardware_profiles']:
	    flavor = DeltaCloudFlavor(item, self)
            flavors.append(flavor)
        return flavors


    def get_flavor(self, flavor_id):
	cmd = '/hardware_profile/' + flavor_id
        return DeltaCloudFlavor(self.conn.request_get(cmd)['hardware_profile'], self) 

    """ 
    Realms
    """

    def get_all_realms(self):
	realms = []
        for item in self.conn.request_get('/realms')['realms']:
	    realm = DeltaCloudRealm(item, self)
            realms.append(realm)
        return realms


    def get_realm(self, realm_id):
	cmd = '/realms/' + realm_id
        return DeltaCloudRealm(self.conn.request_get(cmd)['realm'], self) 

    """ 
    Images
    """
    def get_all_images(self):
	images = []
        for item in self.conn.request_get('/images')['images']:
            image = DeltaCloudImage(item, self)
            images.append(image)
        return images
        

    def get_image(self, image_id):
	cmd = '/images/' + image_id
 	return DeltaCloudImage(self.conn.request_get(cmd)['image'], self)
	

    """ 
    Instances
    """
    def get_all_instances(self):
	instances = []
        for item in self.conn.request_get('/instances')['instances']:
            instance = DeltaCloudInstance(item, self)
            instances.append(instance)
        return instances
        
    def get_instance(self, instance_id):
	cmd = '/instances/' + instance_id
 	return DeltaCloudInstance(self.conn.request_get(cmd)['instance'], self)
       
    """ 
    Storage volumes
    """	
    def get_all_storage_volumes(self):
	volumes = []
        for item in self.conn.request_get('/storage_volumes')['storage_volumes']:
            volume = DeltaCloudVolume(item, self)
            volumes.append(volume)
        return volumes

    def get_storage_volume(self, volume_id):
	cmd = '/storage_volumes/' + volume_id
 	return DeltaCloudVolume(self.conn.request_get(cmd)['storage_volume'], self)


    """ 
    Storage snapshots
    """	
    def get_all_storage_snapshots(self):
	snapshots = []
        for item in self.conn.request_get('/storage_snapshots')['storage_snapshots']:
            snapshot = DeltaCloudSnapshot(item, self)
            snapshots.append(snapshot)
        return snapshots

    def get_storage_snapshot(self, snapshot_id):
	cmd = '/storage_snapshots/' + snapshot_id
 	return DeltaCloudSnapshot(self.conn.request_get(cmd)['storage_snapshot'], self)
