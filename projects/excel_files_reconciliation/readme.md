## Original job description from Upwork

### Create a small piece of software to compare two excel files

Purpose of this software:

Our company performs inventory audits for public schools. We start with their original inventory file in a spreadsheet form (Reference File), we then go through their building and record an inventory of everything that we find by scanning barcode stickers on all the items. The file of the items that we scanned creates the Scan File spreadsheet.

We then need to reconcile the Scan File with the Reference File to produce a final Export File. The purpose of the reconciliation is to identify any items from the Reference File that were Missing (not scanned during the inventory), Found (scanned during the inventory an no change to any of the data fields), Changed (scanned during the inventory but one or more of the datafields/columns has new data in it. We also want to record which data fields/columns had the change and what the original data was from the Reference File and what the new data is from the Scan File) or New (item that was scanned during the inventory, but has no match in the Reference File so it is a new item being added to the database).

We primarily reconcile the two files by checking the Barcode Number between the two files. If a Barcode Number from the Scan File matches a Barcode Number from the Reference file, then we check to see if the data in any of the other columns for that row has changed. If there is a change in any of the other columns then the data from the Scan File is what is used for the Export File for that Barcode number. That row will receive a status of “C”. If there is a match in Barcode Numbers between the Reference File and the Scan File and all the columns are the same, that row will receive a status of “F”

If there is a Barcode Number in the Reference file that does not have a match in the Scan File, that Barcode Number row is put into the Export File and the row receives a status of “M”.

If there is a Barcode Number in the Scan File that does not have a match in the Reference File, that Barcode Number row is put into the Export File and the row receives a status of “N”.

I would like this to have at least a basic GUI so that it is user friendly. I don’t know enough about software development to know if this should be a python script or written in some other language. I only care that it can perform the task of comparison correctly.

It needs to be able to hand Reference and Scan file spreadsheets that may have up to 50,000 rows of data each. Also the Reference File and the Scan File will always each have a Barcode Number column to compare against, but there may not always be the same number of columns in the files, for example one Reference file might have 10 columns and another Reference file might have 15 columns, so the software needs to be flexible to adjust to however many columns are in the files and check all columns for changed data when there is a Barcode Number match.

Fixed price: $750.00