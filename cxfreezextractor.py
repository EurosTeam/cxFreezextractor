from zipfile import ZipFile
import os,sys,glob,time

try:
	path = os.path.dirname(sys.argv[1])
	filename = os.path.basename(sys.argv[1])[0:-4] # get the filename and remove the .exe extension
	os.chdir(path)
	for file in glob.glob("*.exe"):
		with ZipFile(path+"\\lib\\library.zip","r") as zip:
			nameoflib = zip.namelist()
			for i in range(0,len(nameoflib)): # list all file of the library.zip
				if(nameoflib[i] == filename+"__main__.pyc"):
					zip.extract(filename+"__main__.pyc",path=os.getcwd()+"\\")
					print("SuccessFully unpacked !")
					time.sleep(2)
				elif(nameoflib[i] == filename+".pyc"):
					zip.extract(filename+".pyc",path=os.getcwd()+"\\")
					print("SuccessFully unpacked !")
					time.sleep(2)

except IndexError:
	print("[*]cxinstxtractor.py <path>")