# Readme

An example of how to use tensorflow as a C api from c++.

Setup:
* Download [tensorflow C api](https://www.tensorflow.org/install/lang_c)  to tensorflow/3dParty
* Create lib file from dll
* Download [example model](https://storage.googleapis.com/download.tensorflow.org/models/inception5h.zip)


## Create lib from dll

Open the Visual Studio Command Prompt, you find its shortcut in Start->Programs->Microsoft Visual Studio->Tools. Now run the dumpbin command to get a list of all exported functions of your dll:

```
dumpbin /exports C:\yourpath\yourlib.dll > tensorflowTemp.def
```

This will print quite a bit of text to the console. However we are only interested in the functions:

```
ordinal hint RVA      name

1    0 00017770 jcopy_block_row
2    1 00017710 jcopy_sample_rows
3    2 000176C0 jdiv_round_up
4    3 000156D0 jinit_1pass_quantizer
5    4 00016D90 jinit_2pass_quantizer
6    5 00005750 jinit_c_coef_controller
```

Now copy all those function names (only the names!) and paste them into a new textfile. Name the nextfile yourlib.def and put the line “EXPORTS” at its top. My yourlib.def file looks like this:

```
EXPORTS
jcopy_block_row
jcopy_sample_rows
jdiv_round_up
jinit_1pass_quantizer
jinit_2pass_quantizer
jinit_c_coef_controller
...
```

Now from that definition file, we can finally create the .lib file. We use the “lib” tool for this, so run this command in your Visual Studio Command Prompt:

```
lib /def:C:\mypath\mylib.def /OUT:C:\mypath\mylib.lib \MACHINE:x64
```

A script for creating tensorflow.def exists in script/parsedef.py