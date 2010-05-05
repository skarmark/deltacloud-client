import os
import sys

sys.path.append("../src")

import deltacloud
from deltacloud import DeltaCloud

username = os.environ['DELTACLOUD_USERNAME']
password = os.environ['DELTACLOUD_PASSWORD']

#username = 'mockuser'
#password = 'mockpassword'

#username = os.environ['AWS_ACCESS_KEY']
#password = os.environ['AWS_SECRET_ACCESS_KEY']

dc  = DeltaCloud(username, password)

print "\n Flavors:"
print "====================="
flavors = dc.get_all_flavors()
for index, i in enumerate(flavors):
	print "Flavor %s:\n  \t%s" % (index, i)


print "\n Realms:"
print "====================="
realms = dc.get_all_realms()
for index, i in enumerate(realms):
	print "Realm %s:\n  \t%s" % (index, i)


print "\n Images:"
print "====================="
images = dc.get_all_images()
for index, i in enumerate(images):
	print "Image %s:\n  \t%s" % (index, i)
'''
print "\n Volumes:"
print "====================="
volumes = dc.get_all_storage_volumes()
for index, i in enumerate(volumes):
	print "Volume %s:\n  \t%s" % (index, i)
'''
print "\n Instances:"
print "====================="
instances  = dc.get_all_instances()
for index, i in enumerate(instances):
	print "Instance %s:\n  \t%s" % (index, i)

print "\n Flavor SILVER-i386:"
print "====================="
flavor = dc.get_flavor('SILVER-i386')
print flavor

print "\n Image 10005496:"
print "====================="
image = dc.get_image('10005496')
print image

print "\n Creating an instance named testclient from image 10005496: \n"
instance = image.run(name='foobar', flavor_id='BRONZE-x86_64', realm_id='2', public_key='cloudekey')
print instance

instance = dc.get_instance('28626')
print instance

ret = instance.stop()
print ret

