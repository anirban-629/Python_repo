import pickle
letters=['aA','bB','cC','dD','eE','fF','jJ']
fileName="lettr.pkl"
letters_object=open(fileName,"wb")
pickle.dump(letters,letters_object)
letters_object.close()