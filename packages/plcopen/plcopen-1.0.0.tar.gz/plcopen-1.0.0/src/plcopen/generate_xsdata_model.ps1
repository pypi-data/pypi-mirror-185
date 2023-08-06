# path to the virtualenv that has xsdata installed
$virtualenv = "C:\Appl\.virtualenvs\festocalctool"

# activate the virtual environment
& "$virtualenv\Scripts\activate.ps1"

# call pyxbgen to generate the schema bindings
& "$virtualenv\Scripts\xsdata.exe" --package plcopen --structure-style clusters tc6_xml_v201.xsd # --unnest-classes 