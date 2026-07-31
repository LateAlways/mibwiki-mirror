import sys
import time
from java.lang import Boolean
from java.math import BigInteger
from java.util import HashMap
from java.util import ArrayList
from de.volkswagen.odis.vaudas.vehiclefunction.automation import IDiagnosticInterface
from de.volkswagen.odis.vaudas.vehiclefunction.automation.types import IDiagResultConnectEcu
from de.volkswagen.odis.vaudas.vehiclefunction.automation import ITotalSystemsInterface

diagnosticInterface = IDiagnosticInterface.Factory.getInstance()
diagnosticInterface.configureSetting("Multilink.MaxNumberOfLogicalLinks", "1")
resultConnectToEcu = diagnosticInterface.connectToEcu(0x17)
diagnosticInterface.openConnection(resultConnectToEcu.getConnectionHandle())
diagnosticInterface.switchSession(resultConnectToEcu.getConnectionHandle(), "DiagnServi_DiagnSessiContrDevelSessi")
diagnosticInterface.securityAccess(resultConnectToEcu.getConnectionHandle(), "20103", "Login")

resp = diagnosticInterface.sendRawService(resultConnectToEcu.getConnectionHandle(), "3D 14 03 00 3C 09 02 03 57")
if (resp[0] == 0x7F): 
  print "Error"
else:  
  print "Upload Sport Layout complete!"
  time.sleep(2)
  print "Now rebooting..."
  diagnosticInterface.sendRawService(resultConnectToEcu.getConnectionHandle(), "11 01")