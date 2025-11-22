# FecContainer.fec - decoded

\

```
• Byte 1 = number of FECs in containers
	○ SingleFEC and MultiFEC each count as one
• Byte 2 - 9 1st SingleFEC /MultiFEC identifier
	○ SingleFEC: 000000AB0000001102 
		§ Byte: 10 - 13: FEC
	○ MultiFEC: 000000XX0000001107 
		§ Byte: 10-13 : ffffffff -> for MultiFec
• Byte 5: length of that SingleFEC (always AB)/MultiFEC
• Byte 14 + 28: VIN, VCNR and TIME
• More complicated now:
	○ SingleFEC: 000000000000000000
		§ followed by SIGNATURE
	○ MultiFEC: 
		§ Byte 43 number of FECs in MultiFEC
		§ FEC List in big endian -> byte length depending on number of fecs
		§ Followed by SIGNATURE
		§ Followed by number of Fecs
		§ Followed by Fecs in little endian
• Add to finish SingleFEC/MultiFEC
	○ 0100000003000000FF000000
```


Normally you only have SingleFEC (ODIS) or MultiFEC (Factory), but this can be mixed…