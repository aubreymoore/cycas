from ij import IJ
from time import sleep

image_list = ['PB020021','PB020023','PB020026','PB020028',
              'PB020031','PB020032','PB020035','PB020037']

for image in image_list:
	imp = IJ.openImage("/home/aubreymoore/cycas/leaflets-2017-11-02/originals/{}.JPG".format(image))
	imp.show()
	print imp
	IJ.run(imp, "Enhance Contrast...", "saturated=0.3")
	sleep(1)
	imp.close()
print 'FINISHED'
