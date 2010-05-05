#!/usr/bin/python
import os
import sys

sys.path.append("../src")

import deltacloud
from deltacloud import DeltaCloud

def usage():
    print "Usage: client-test.py <action: realms|images|instances|volumes|snapshots >"

if __name__ == "__main__":
   
	# Arguments           
	if len(sys.argv) < 2:
        	usage()
        	sys.exit(0)

	#username = os.environ['DELTACLOUD_USERNAME']
	#password = os.environ['DELTACLOUD_PASSWORD']

	#username = 'mockuser'
	#password = 'mockpassword'

	username = 'AKIAJENTARYFGLVRT4QA'
	password = 'OR1KortQSjX0ZrDdOtnxwwh5C4NbSH/fWa118Xpt'

	dc  = DeltaCloud(username, password)
        action = sys.argv[1]
        
	if action == 'realms':
		print "\n Realms:"
		print "====================="
		realms = dc.get_all_realms()
		for index, i in enumerate(realms):
			print "Realm %s:\n  \t%s" % (index, i)

	if action == 'images':
		print "\n Images:"
		print "====================="
		images = dc.get_all_images()
		for index, i in enumerate(images):
			if ((i['name'].find('ami-205fba49') != -1) and (i['description'].find('fedora') != -1)):
				print "Image %s:\n  \t%s" % (index, i)
                		image = i
                opts = {}
                opts['realm_id'] = 'us-east-1a'
                opts['hwp_id'] = 'm1-small'
                #opts['name'] = 'testfoobar'
                opts['key_name'] = 'cloude-key'
                print "\n Creating an instance named testclient from image 10005496: \n"
                instance = image.run(opts)
                print instance               

	if action == 'volumes':
		print "\n Volumes:"
		print "====================="
		volumes = dc.get_all_storage_volumes()
		for index, i in enumerate(volumes):
			print "Volume %s:\n  \t%s" % (index, i)

	if action == 'snapshots':
		print "\n Snapshots:"
		print "====================="
		snapshots = dc.get_all_storage_snapshots()
		for index, i in enumerate(snapshots):
			print "Snapshot %s:\n  \t%s" % (index, i)

	if action == 'instances':
		print "\n Instances:"
		print "====================="
		instances  = dc.get_all_instances()
		for index, i in enumerate(instances):
			print "Instance %s:\n  \t%s" % (index, i)
                        if (i['id'].find('i-7b8bc610') != -1):
                            print 'rebooting\n'
                            ret = i.reboot()
                            print ret
                            
'''
print "\n Flavors:"
print "====================="
flavors = dc.get_all_flavors()
for index, i in enumerate(flavors):
	print "Flavor %s:\n  \t%s" % (index, i)
'''

'''
print "\n Flavor SILVER-i386:"
print "====================="
flavor = dc.get_flavor('SILVER-i386')
print flavor
'''
'''
print "\n Image 10005496:"
print "====================="
image = dc.get_image("ami-02d93c6b")
print image
'''
'''
opts = {} 
opts['realm_id'] = 'us-east-1b'
#opts['hwp_id'] = 'c1.medium'
opts['key_name'] = 'cloude-key'
print "\n Creating an instance named testclient from image 10005496: \n"
instance = image.run(opts)
#instance = image.run(name='foobar')
print instance
'''
'''
instance = dc.get_instance('29269')
print instance

ret = instance.stop()
print ret
'''
