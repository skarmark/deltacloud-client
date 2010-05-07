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
        username = 'AKIAJENTARYFGLVRT4QA'
	password = 'OR1KortQSjX0ZrDdOtnxwwh5C4NbSH/fWa118Xpt'

	#username = os.environ['DELTACLOUD_USERNAME']
	#password = os.environ['DELTACLOUD_PASSWORD']
	
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
                    if ((i['name'].find('ami') != -1) and (i['description'].find('fedora') != -1)):
                        print "Image %s:\n  \t%s" % (index, i)
         
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
                        
                            

