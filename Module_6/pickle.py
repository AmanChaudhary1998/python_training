#Record: set of data that dexscribes one item
# Feild: single piece of data in the record
# Searilizing a object is the process of converting the object to a stream of bytes
#that can be saved to a file for later retrieval
# In python, Object serialization is called pickling
import pickle
phonebook={'Chris':'5551111','Katie':'5552222','Joanne':'5553333'}
output_file= open('phonebook.dat','wb')
pickle.dump(phonebook,output_file)
"""print(output_file)"""
output_file.close()
in_file=open('phonebook.dat','rb')
pb=pickle.load(in_file)
in_file.close()
print(pb)
