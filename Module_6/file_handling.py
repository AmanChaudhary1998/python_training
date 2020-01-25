# File Handling....
# open file => file_object= open(filename,mode)
# Mode reading mode('r'), writting('w') and appending('a'),read and write('r+') binary_file('b')
def main():
     # Open the file name philosophers.txt
     outfile = open('aman.txt','w')
     # Write operation will perform
     outfile.write('Aman Chaudhary\n')
     outfile.write('CSE (CMC)')
     # Close the file
     outfile.close()
     # Open the file named philosophers.txt
     infile = open('aman.txt','r')
     # Read the file's contents.
     file_contents= infile.read()
     #Close the file.
     infile.close()
     #print the data that was read
     print(file_contents)
     # Open a file name philosophers.txt
     infile= open('aman.txt','r')
     line=infile.readline()
     while line!='':
          # Convert line into the float
          amount=(line)
          #Read lines from the file
          line=infile.readline()
          print(amount)
     infile.close()




main()
