# coding: latin-1
import sys
reload(sys)
sys.setdefaultencoding("latin-1")
from java.lang import Boolean
from java.math import BigInteger
from java.util import HashMap
from java.util import ArrayList
from de.volkswagen.odis.vaudas.vehiclefunction.automation import IDiagnosticInterface
from de.volkswagen.odis.vaudas.vehiclefunction.automation.types import IDiagResultConnectEcu
from de.volkswagen.odis.vaudas.vehiclefunction.automation import ITotalSystemsInterface
from de.volkswagen.odis.vaudas.vehiclefunction.automation import ISecurityAccessInterface
diagnosticInterface = IDiagnosticInterface.Factory.getInstance()
diagnosticInterface.configureSetting("Multilink.MaxNumberOfLogicalLinks", "1")
diagnosticInterface.startProtocol()
print "Coding Instrument Cluster"
resultConnectToEcu = diagnosticInterface.connectToEcu(0x17)
diagnosticInterface.openConnection(resultConnectToEcu.getConnectionHandle())
diagnosticInterface.securityAccess(resultConnectToEcu.getConnectionHandle(), "20103", "Login")
diagnosticInterface.readCoding(resultConnectToEcu.getConnectionHandle())
codingValues = HashMap()
codingValues.put("Param_TraffSignDisplBAP", "yes")
codingValues.put("Param_TraffSignDetec", "yes")
diagnosticInterface.writeTextCoding(resultConnectToEcu.getConnectionHandle(), "master", codingValues)
doEcuReset = Boolean.FALSE
print "Coding MMI"
resultConnectToEcu = diagnosticInterface.connectToEcu(0x5F)
diagnosticInterface.openConnection(resultConnectToEcu.getConnectionHandle())
diagnosticInterface.switchSession(resultConnectToEcu.getConnectionHandle(), "DiagnServi_DiagnSessiContrDevelSessi")
diagnosticInterface.securityAccess(resultConnectToEcu.getConnectionHandle(), "20103", "Login")
diagnosticInterface.readCoding(resultConnectToEcu.getConnectionHandle())
codingValues = HashMap()
codingValues.put("Param_Byte24NavigSyste", "active")
codingValues.put("Param_Byte24Vza", "active")
codingValues.put("Param_Byte24Psd", "active")
diagnosticInterface.writeTextCoding(resultConnectToEcu.getConnectionHandle(), "master", codingValues)
diagnosticInterface.readAdaptation(resultConnectToEcu.getConnectionHandle(), "Vehicle_configuration")
adaptationValues = HashMap()
adaptationValues.put("Param_VZAPr", "on")
diagnosticInterface.writeAdaptation(resultConnectToEcu.getConnectionHandle(), "Vehicle_configuration", adaptationValues)
diagnosticInterface.readAdaptation(resultConnectToEcu.getConnectionHandle(), "Car_Function_Adaptations_Gen2")
adaptationValues = HashMap()
adaptationValues.put("Param_MenuDisplRoadSignIdent", "activated")
adaptationValues.put("Param_MenuDisplRoadSignIdentOverThresHigh", "activated")
diagnosticInterface.writeAdaptation(resultConnectToEcu.getConnectionHandle(), "Car_Function_Adaptations_Gen2", adaptationValues)
diagnosticInterface.readAdaptation(resultConnectToEcu.getConnectionHandle(), "Car_Function_List_BAP_Gen2")
adaptationValues = HashMap()
adaptationValues.put("Param_TraffSignRecog0x21", "activated")
adaptationValues.put("Param_TraffSignRecog0x21MsgBus", "CAN_Extended")
diagnosticInterface.writeAdaptation(resultConnectToEcu.getConnectionHandle(), "Car_Function_List_BAP_Gen2", adaptationValues)
doEcuReset = Boolean.TRUE
print "Coding Camera"
resultConnectToEcu = diagnosticInterface.connectToEcu(0xA5)
diagnosticInterface.openConnection(resultConnectToEcu.getConnectionHandle())
diagnosticInterface.switchSession(resultConnectToEcu.getConnectionHandle(), "DiagnServi_DiagnSessiContrDevelSessi")
diagnosticInterface.securityAccess(resultConnectToEcu.getConnectionHandle(), "20103", "Login")
diagnosticInterface.readCoding(resultConnectToEcu.getConnectionHandle())
codingValues = HashMap()
codingValues.put("Param_CodinVZE", "coded")
codingValues.put("Param_VZERSRRegio", "Westeurope")
codingValues.put("Param_VZECamType", "MQB_MFK")
codingValues.put("Param_VZENavig", "MIB2 High PSD 1.4")
diagnosticInterface.writeTextCoding(resultConnectToEcu.getConnectionHandle(), "master", codingValues)
diagnosticInterface.readAdaptation(resultConnectToEcu.getConnectionHandle(), "Road_sign_recognition_fusion_mode")
adaptationValues = HashMap()
adaptationValues.put("Param_Data", "Road_Sign_Fusion")
diagnosticInterface.writeAdaptation(resultConnectToEcu.getConnectionHandle(), "Road_sign_recognition_fusion_mode", adaptationValues)
print "Erasing DTC entries"
diagnosticInterface.resetEventMemories(True, True, True, 5, [])
diagnosticInterface.stopProtocol()