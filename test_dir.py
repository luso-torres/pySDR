
def path_dir()
path = os.path.dirname(__file__) #receives the information of the path.
#print(path)
i=0
for module in os.listdir(path):
    print("Module name: \n", module)
    #print("Path:\n",path)
    if module.endswith(".py") and module != "__init.py__" and module != "__main.py__":
         module_name = module[:-3]
         #print(module_name)
         try:
            # Use the current package as the base for relative imports
            imported_module = importlib.import_module(f"pySDR.{module_name}", package="pySDR")
            globals()[module_name] = imported_module
            print(f"globals(): {globals()}")
            print(f"Successfully imported {module_name}") 
         except Exception as e:
            print(f"Failed to import {module_name}: {e}")
