from ImageAnalysis import *
path = r"C:\Users\3boody\Documents\GitHub\SeniorProject-1\Image Analysis\testingOutput\\"
outputFile= r"C:\Users\3boody\Documents\GitHub\SeniorProject-1\Image Analysis\testingOutput\output.txt"
f= open(outputFile, "w" ,encoding='utf-8')
imageName = input("Enter image name : ")
imageFile = str(path)+str(imageName)
print("imageFile ",imageFile)
jd = myReg(imageFile,"","",1)
f.writelines("\n")
f.writelines(jd)



