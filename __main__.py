## creating a new vector

import numpy as np
import os, importlib
#import script2,script1

path = os.path.dirname(__file__) #receives the information of the path.
print(path)
i=0
for module in os.listdir(path):
    print("Module name: \n", module)
    print("Path:\n",path)
    if module.endswith(".py") and module != "__init.py__":
         module_name = module[:-3]
         #print(module_name)
         try:
            # Use the current package as the base for relative imports
            imported_module = importlib.import_module(f".{module_name}", package="pySDR")
            globals()[module_name] = imported_module
            print(f"globals(): {globals()}")
            print(f"Successfully imported {module_name}") 
         except Exception as e:
            print(f"Failed to import {module_name}: {e}")


a = np.array([2,3,4,5])
mylist = [2,3,4,5]
if __name__ == "__main__":
    script1.introFunction()
    print(a, mylist)
    script.randomMatrices
    script2.finishTest()

def main():
    if __name__ == "__main__":
        main()
       

