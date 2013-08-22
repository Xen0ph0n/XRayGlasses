## XRay Glasses
XRay is a quck script which was shared with me by someone who wished to remain annonymous. So this is being shared with no restrictions of any type. Hopefully it will be found to be useful. This has been implemented in the Moloch project to help visualize files and I've successfully leveraged this methodology to detect encoding methods in carrier docs and executable files. 

The Idea being heuristic, visual, detection of packing methods utilized in advanced exploit laiden files and malware. 

### Usage

```
xray.py path/to/file.exe 

python xray.py ../pathtobadness/malcode.danger 
[+] XRay Codeimage complete: malcode___IMAGE.bmp

```

### Output

Clearly visibile is the encoded payload, as evidenced by the nullspace displaying a gradient pattern:

Created from this exploit laden word doc containing a malcious back door: https://www.virustotal.com/file/E4B98573EB8E9EFBA28FEAABCF915600160E36EF3D8C40DA5E716E0A5EAEE6CD/

![Image](https://raw.github.com/Xen0ph0n/XRayGlasses/master/sample.png) 
