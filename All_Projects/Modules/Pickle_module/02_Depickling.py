import pickle
file_name="lettr.pkl"
file_obj=open(file_name,"rb")
lttr=pickle.load(file_obj)
print(lttr)