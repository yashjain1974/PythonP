
import os
# path=str(input("Enter file Path"))
# file=str(input("Enter File Name which is not Changed"))
# format=str(input("Enter Format of File"))

# def soldier(path,file,format):
#     i=0
#     os.chdir(path)
#     g = os.listdir()
#     with open(file) as f:
#         filelist=f.read().split("/n")
#
#     for file in g:
#         if file not in filelist:
#          os.rename(file,file.capitalize())
#
#         if file.endswith(format):       #We also use 'os.path.splitext(file)[1]==format:'
#             os.rename(f'{file}',f'{i}{format}')
#             i+=1
# soldier(r'C:\Users\yash.JAIN-PC\Desktop\New fsh.JAIN-PC\Desktop\New folder',r'.jpg')
def Change(path,format):
   os.chdir(path)
   i=1
   files=os.listdir()

   for file in files:

      os.rename(file,file.capitalize())

      if file.endswith(format):
        os.rename(file,f'{i}.{file}.{format}')
        i += 1

Change(r'E:\yash programming Chapters\C programming',r'.mp4')













