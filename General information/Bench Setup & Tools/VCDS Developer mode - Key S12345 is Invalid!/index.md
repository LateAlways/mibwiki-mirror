# VCDS Developer mode - Key S12345 is Invalid!

If S12345 script for Developer mode doesn't work and you get error "*Key S12345 is Invalid!*"

It's because VCDS can't match correct label file with FW version and unit.

 ![](attachments/6285c3ef-787d-4f64-8886-09c4ed75d007.JPG)

 \n  \n And in 5F > Advanced ID > is on bottom Labels: None

 ![](attachments/9ed0369c-e173-43e2-8fbb-2ddcc65bfd33.jpeg)

 \n In folder C:\\Ross-Tech\\VCDS\\Labels are labels named: \n 3V0-035-MIB-STD2.clb  for Skoda MIB2 STD units \n 5G0-035-MIB-STD2.clb  for VW MIB2 STD units \n 5F0-035-MIB-STD2.clb   for Seat MIB2 STD units \n  \n 3V0-035-MIB-HGH2.clb   for Skoda MIB2 HIGH units \n 5G0-035-MIB-HGH2.clb   for VW MIB2 HIGH units \n 5F0-035-MIB-HGH2.clb   for Seat MIB2 HIGH units

 ![](attachments/1c8a906a-99c9-4806-a5d6-b32130d231ad.JPG)

 \n Copy file (depend on your unit) to somewhere else (let say Desktop), rename it to part number of your unit (example 5NA-035-043.clb) and place it back to C:\\Ross-Tech\\VCDS\\Labels\\ and try to connect to MIB2 unit once again. Now you should see label in Advanced ID and S12345 script for developer mode should work. \n 

 ![](attachments/ad32c9e2-49b3-40f9-8866-9a73e2b43ac5.JPG)

 ![](attachments/7667bb2d-1f97-4152-b0a6-6bf8e0ecd369.JPG)