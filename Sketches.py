import win32com.client

# Connect to SolidWorks
swApp = win32com.client.Dispatch("SldWorks.Application")
swModel = swApp.ActiveDoc

print(swModel.GetTitle)

sketch_manager = swModel.SketchManager

sketches = swModel.GetSketches