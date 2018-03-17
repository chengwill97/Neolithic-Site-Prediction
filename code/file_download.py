import os
import urllib
from multiprocessing import Pool
import time
import urllib2
import zipfile
import webbrowser

class srtmDownloader(object):
    def downloadFileL1(self,target):
        url = "http://e4ftl01.cr.usgs.gov/SRTM/SRTMGL1.003/2000.02.11/" + target + ".SRTMGL1.hgt.zip"
        file = urllib.urlretrieve(url, "file.zip")
        # zipfile.ZipFile('file.hgt.zip').extractall()
    def downloadFileL3(self,target):
        url = "http://e4ftl01.cr.usgs.gov/SRTM/SRTMGL3.003/2000.02.11/" + target + ".SRTMGL3.hgt.zip"
        file = urllib.urlretrieve(url, "file.zip")
        # zipfile.ZipFile('file.hgt.zip').extractall()

def targetExtract(url):
	token1 = url.split('/')
	target = ''
	for token in token1:
		if '.hgt.zip' in token:
			token2 = token.split('.')
			target = token2[0]
	return target

def downloadSRTM(filename):
	# if '2' in filename:
	# 	time.sleep(5)
	# if '3' in filename:
	# 	time.sleep(5)
	_FOLDER = 'britain-srtm'
	_PATH   = os.path.join(os.getcwd(), _FOLDER)

	username = 'chengwill97'
	password = 'VAp-6o2-JP2-Wz7'

	filepath = os.path.join(_PATH, filename)
	file = open(filepath, 'r')
	for temp_url in file.readlines():
		if 'zip' in temp_url:
			try:
				if '.zip' in temp_url[:-1]:
					url = temp_url[:-1]
				else:
					url = temp_url

				downloadname = url.split('/')[-1]
				downloadname = os.path.join(_PATH, downloadname)

				print ' [x] Unzipping %s' % url
				# getunzipped(url, _PATH, downloadname[:-4])
				

				webbrowser.open(url)
				print ' [x] Finished Unzipping %s' % downloadname[:-4]

				# urllib.urlretrieve(url, downloadname[:-4])
			except IOError:
				continue

		# break
	# break
# chengwill97
# VAp-6o2-JP2-Wz7
if __name__ == '__main__':
	_FOLDER = 'britain-srtm'
	_PATH = os.path.join(os.getcwd(), _FOLDER)
	files = os.listdir(_PATH)

	for i in files:
		downloadSRTM(i)
