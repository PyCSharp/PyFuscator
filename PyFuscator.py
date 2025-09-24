import base64
import os
import py_compile
from random import randint
from cryptography.fernet import Fernet

def CreateJunkCode():
    if os.path.exists(f"obfuscated_{file}"):
            content = ReadFile(f"obfuscated_{file}")

    else:
        content = ReadFile(file)

    newContent = """def MainFunc():
    exec(__import__('base64').b64decode(\"\"\"TG9yZW0gaXBzdW0gZG9sb3Igc2l0IGFtZXQsIGNvbnNldGV0dXIgc2FkaXBzY2luZyBlbGl0ciwgc2VkIGRpYW0gbm9ud
    W15IGVpcm1vZCB0ZW1wb3IgaW52aWR1bnQgdXQgbGFib3JlIGV0IGRvbG9yZSBtYWduYSBhbGlxdXlhbSBlcmF0LCBzZWQgZGlhbSB2b
    2x1cHR1YS4gQXQgdmVybyBlb3MgZXQgYWNjdXNhbSBldCBqdXN0byBkdW8gZG9sb3JlcyBldCBlYSByZWJ1bS4gU3RldCBjbGl0YSBrY
    XNkIGd1YmVyZ3Jlbiwgbm8gc2VhIHRha2ltYXRhIHNhbmN0dXMgZXN0IExvcmVtIGlwc3VtIGRvbG9yIHNpdCBhbWV0LiBMb3JlbSBpc
    HN1bSBkb2xvciBzaXQgYW1ldCwgY29uc2V0ZXR1ciBzYWRpcHNjaW5nIGVsaXRyLCBzZWQgZGlhbSBub251bXkgZWlybW9kIHRlbXBvc
    iBpbnZpZHVudCB1dCBsYWJvcmUgZXQgZG9sb3JlIG1hZ25hIGFsaXF1eWFtIGVyYXQsIHNlZCBkaWFtIHZvbHVwdHVhLiBBdCB2ZXJvI
    GVvcyBldCBhY2N1c2FtIGV0IGp1c3RvIGR1byBkb2xvcmVzIGV0IGVhIHJlYnVtLiBTdGV0IGNsaXRhIGthc2QgZ3ViZXJncmVuLCBub
    yBzZWEgdGFraW1hdGEgc2FuY3R1cyBlc3QgTG9yZW0gaXBzdW0gZG9sb3Igc2l0IGFtZXQuIExvcmVtIGlwc3VtIGRvbG9yIHNpdCBhb
    WV0LCBjb25zZXRldHVyIHNhZGlwc2NpbmcgZWxpdHIsIHNlZCBkaWFtIG5vbnVteSBlaXJtb2QgdGVtcG9yIGludmlkdW50IHV0IGxhY
    m9yZSBldCBkb2xvcmUgbWFnbmEgYWxpcXV5YW0gZXJhdCwgc2VkIGRpYW0gdm9sdXB0dWEuIEF0IHZlcm8gZW9zIGV0IGFjY3VzYW0gZ
    XQganVzdG8gZHVvIGRvbG9yZXMgZXQgZWEgcmVidW0uIFN0ZXQgY2xpdGEga2FzZCBndWJlcmdyZW4sIG5vIHNlYSB0YWtpbWF0YSBzY
    W5jdHVzIGVzdCBMb3JlbSBpcHN1bSBkb2xvciBzaXQgYW1ldC4gIAoKRHVpcyBhdXRlbSB2ZWwgZXVtIGlyaXVyZSBkb2xvciBpbiBoZ
    W5kcmVyaXQgaW4gdnVscHV0YXRlIHZlbGl0IGVzc2UgbW9sZXN0aWUgY29uc2VxdWF0LCB2ZWwgaWxsdW0gZG9sb3JlIGV1IGZldWdpY
    XQgbnVsbGEgZmFjaWxpc2lzIGF0IHZlcm8gZXJvcyBldCBhY2N1bXNhbiBldCBpdXN0byBvZGlvIGRpZ25pc3NpbSBxdWkgYmxhbmRpd
    CBwcmFlc2VudCBsdXB0YXR1bSB6enJpbCBkZWxlbml0IGF1Z3VlIGR1aXMgZG9sb3JlIHRlIGZldWdhaXQgbnVsbGEgZmFjaWxpc2kuI
    ExvcmVtIGlwc3VtIGRvbG9yIHNpdCBhbWV0LCBjb25zZWN0ZXR1ZXIgYWRpcGlzY2luZyBlbGl0LCBzZWQgZGlhbSBub251bW15IG5pY
    mggZXVpc21vZCB0aW5jaWR1bnQgdXQgbGFvcmVldCBkb2xvcmUgbWFnbmEgYWxpcXVhbSBlcmF0IHZvbHV0cGF0LiAgCgpVdCB3aXNpI
    GVuaW0gYWQgbWluaW0gdmVuaWFtLCBxdWlzIG5vc3RydWQgZXhlcmNpIHRhdGlvbiB1bGxhbWNvcnBlciBzdXNjaXBpdCBsb2JvcnRpc
    yBuaXNsIHV0IGFsaXF1aXAgZXggZWEgY29tbW9kbyBjb25zZXF1YXQuIER1aXMgYXV0ZW0gdmVsIGV1bSBpcml1cmUgZG9sb3IgaW4ga
    GVuZHJlcml0IGluIHZ1bHB1dGF0ZSB2ZWxpdCBlc3NlIG1vbGVzdGllIGNvbnNlcXVhdCwgdmVsIGlsbHVtIGRvbG9yZSBldSBmZXVna
    WF0IG51bGxhIGZhY2lsaXNpcyBhdCB2ZXJvIGVyb3MgZXQgYWNjdW1zYW4gZXQgaXVzdG8gb2RpbyBkaWduaXNzaW0gcXVpIGJsYW5ka
    XQgcHJhZXNlbnQgbHVwdGF0dW0genpyaWwgZGVsZW5pdCBhdWd1ZSBkdWlzIGRvbG9yZSB0ZSBmZXVnYWl0IG51bGxhIGZhY2lsaXNpL
    iAgCgpOYW0gbGliZXIgdGVtcG9yIGN1bSBzb2x1dGEgbm9iaXMgZWxlaWZlbmQgb3B0aW9uIGNvbmd1ZSBuaWhpbCBpbXBlcmRpZXQgZ
    G9taW5nIGlkIHF1b2QgbWF6aW0gcGxhY2VyYXQgZmFjZXIgcG9zc2ltIGFzc3VtLiBMb3JlbSBpcHN1bSBkb2xvciBzaXQgYW1ldCwgY
    29uc2VjdGV0dWVyIGFkaXBpc2NpbmcgZWxpdCwgc2VkIGRpYW0gbm9udW1teSBuaWJoIGV1aXNtb2QgdGluY2lkdW50IHV0IGxhb3JlZ
    XQgZG9sb3JlIG1hZ25hIGFsaXF1YW0gZXJhdCB2b2x1dHBhdC4gVXQgd2lzaSBlbmltIGFkIG1pbmltIHZlbmlhbSwgcXVpcyBub3N0c
    nVkIGV4ZXJjaSB0YXRpb24gdWxsYW1jb3JwZXIgc3VzY2lwaXQgbG9ib3J0aXMgbmlzbCB1dCBhbGlxdWlwIGV4IGVhIGNvbW1vZG8gY
    29uc2VxdWF0LiAgCgpEdWlzIGF1dGVtIHZlbCBldW0gaXJpdXJlIGRvbG9yIGluIGhlbmRyZXJpdCBpbiB2dWxwdXRhdGUgdmVsaXQgZ
    XNzZSBtb2xlc3RpZSBjb25zZXF1YXQsIHZlbCBpbGx1bSBkb2xvcmUgZXUgZmV1Z2lhdCBudWxsYSBmYWNpbGlzaXMuICAgCgpBdCB2Z
    XJvIGVvcyBldCBhY2N1c2FtIGV0IGp1c3RvIGR1byBkb2xvcmVzIGV0IGVhIHJlYnVtLiBTdGV0IGNsaXRhIGthc2QgZ3ViZXJncmVuL
    CBubyBzZWEgdGFraW1hdGEgc2FuY3R1cyBlc3QgTG9yZW0gaXBzdW0gZG9sb3Igc2l0IGFtZXQuIExvcmVtIGlwc3VtIGRvbG9yIHNpd
    CBhbWV0LCBjb25zZXRldHVyIHNhZGlwc2NpbmcgZWxpdHIsIHNlZCBkaWFtIG5vbnVteSBlaXJtb2QgdGVtcG9yIGludmlkdW50IHV0I
    GxhYm9yZSBldCBkb2xvcmUgbWFnbmEgYWxpcXV5YW0gZXJhdCwgc2VkIGRpYW0gdm9sdXB0dWEuIEF0IHZlcm8gZW9zIGV0IGFjY3VzY
    W0gZXQganVzdG8gZHVvIGRvbG9yZXMgZXQgZWEgcmVidW0uIFN0ZXQgY2xpdGEga2FzZCBndWJlcmdyZW4sIG5vIHNlYSB0YWtpbWF0Y
    SBzYW5jdHVzIGVzdCBMb3JlbSBpcHN1bSBkb2xvciBzaXQgYW1ldC4gTG9yZW0gaXBzdW0gZG9sb3Igc2l0IGFtZXQsIGNvbnNldGV0d
    XIgc2FkaXBzY2luZyBlbGl0ciwgQXQgYWNjdXNhbSBhbGlxdXlhbSBkaWFtIGRpYW0gZG9sb3JlIGRvbG9yZXMgZHVvIGVpcm1vZCBlb
    3MgZXJhdCwgZXQgbm9udW15IHNlZCB0ZW1wb3IgZXQgZXQgaW52aWR1bnQganVzdG8gbGFib3JlIFN0ZXQgY2xpdGEgZWEgZXQgZ3ViZ
    XJncmVuLCBrYXNkIG1hZ25hIG5vIHJlYnVtLiBzYW5jdHVzIHNlYSBzZWQgdGFraW1hdGEgdXQgdmVybyB2b2x1cHR1YS4gZXN0IExvc
    mVtIGlwc3VtIGRvbG9yIHNpdCBhbWV0LiBMb3JlbSBpcHN1bSBkb2xvciBzaXQgYW1ldCwgY29uc2V0ZXR1ciBzYWRpcHNjaW5nIGVsa
    XRyLCBzZWQgZGlhbQ==\"\"\".decode("utf-8")))\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n
    \n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n
    \n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n
    \n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n
    \n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n
    \n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n
    \n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n
    \n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n
    \n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n
    \n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n
    \n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n
    \n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n
    \n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n
    \n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n
    \n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n
    \n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n
    \n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n
    \n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n
    \n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n
    \n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n""" + content
    
    try:
        with open(f"obfuscated_{file}", "w") as f:
            f.write(newContent)

    except Exception as e:
        print(f"Error: {e}")
        input()

def Banner():
    banner = r"""
__________        ___________                          __                
\______   \___.__.\_   _____/_ __  ______ ____ _____ _/  |_  ___________ 
 |     ___<   |  | |    __)|  |  \/  ___// ___\\__  \\   __\/  _ \_  __ \
 |    |    \___  | |     \ |  |  /\___ \\  \___ / __ \|  | (  <_> )  | \/
 |____|    / ____| \___  / |____//____  >\___  >____  /__|  \____/|__|   
           \/          \/             \/     \/     \/                   
                                                            -by PyCSharp
"""

    print(banner)


def ReadFile(file):
    try:
        with open(file) as f:
            content = f.read()
            return content
    except Exception as e:
        print(f"Error: {e}")
        input()

def FirstObfuscationStage():
    if (os.path.exists(f"obfuscated_{file}")):
        newIntermediateContentBytes = ReadFile(f"obfuscated_{file}").encode("utf-8")

    else:
        newIntermediateContentBytes = ReadFile(file).encode("utf-8")

    intermediateBase64Bytes = base64.b64encode(newIntermediateContentBytes)
    
    intermediateContent = f"""import base64
v = {intermediateBase64Bytes}
exec(base64.b64decode(v.decode("ascii")))"""

    newContentBytes = intermediateContent.encode("utf-8")
    base64Bytes = base64.b64encode(newContentBytes)

    try:
        with open(f"obfuscated_{file}", "w") as f:
            f.write(f"""exec(__import__('base64').b64decode({base64Bytes}.decode("utf-8")))""")
    except Exception as e:
        print(f"Error: {e}")
        input()

def SecondObfuscationStage():
    content = ReadFile(f"obfuscated_{file}")

    newIntermediateContentHex = content.encode("utf-8").hex()
    newContentHex = newIntermediateContentHex.replace("a", "m").replace("f", "x").replace("8", "j")

    newContent = f"""v = \"{newContentHex}\"
exec(bytes.fromhex(v.replace("m", "a").replace("x", "f").replace("j", "8")).decode("utf-8"))"""

    try:
        with open(f"obfuscated_{file}", "w") as f:
            f.write(newContent)
    except Exception as e:
        print(f"Error: {e}")
        input()

def ThirdObfuscationStage():
    xorKey = randint(1, 255)
    fernetKey = Fernet.generate_key()

    f = Fernet(fernetKey)

    encryptedXorKey = f.encrypt(xorKey.to_bytes(1, "big"))

    content = ReadFile(f"obfuscated_{file}")

    newContentHex = content.encode("utf-8").hex()

    newContentDec = list(bytes.fromhex(newContentHex))

    newContentDec = [i ^ xorKey for i in newContentDec]

    try:
        with open(f"obfuscated_{file}", "w") as f:
            f.write(f"""v = {newContentDec}
from cryptography.fernet import Fernet
v2 = Fernet({fernetKey})
exec(\"\"\"v = [v3 ^ int.from_bytes(v2.decrypt({encryptedXorKey}), "big") for v3 in v]
v4 = bytes(v)
exec(bytes.fromhex(v4.hex()).decode("utf-8"))\"\"\")""")
            
    except Exception as e:
        print(f"Error: {e}")
        input()
        
def FourthObfuscationStage():
    content = ReadFile(f"obfuscated_{file}")
    fernetKey = Fernet.generate_key()

    f = Fernet(fernetKey)

    encryptedContent = f.encrypt(content.encode("utf-8"))

    try:
        with open(f"obfuscated_{file}", "w") as f:
            f.write(f"""exec(f\"\"\"from cryptography.fernet import Fernet
v2 = Fernet({fernetKey})
exec(v2.decrypt({encryptedContent}))\"\"\")""")
    except Exception as e:
        print(f"Error: {e}")
        input()

def FithObfuscationStage():
    try:
        py_compile.compile(f"obfuscated_{file}", cfile=f"obfuscated_{file}.pyc")
    except Exception as e:
        print(f"Error: {e}")
        input()
    try:
        os.remove(f"obfuscated_{file}")
    except Exception as e:
        print(f"Error: {e}")
        input()

while True:
    Banner()

    file = input("File Path: ")
    junkcodeInput = input("Add Junk Code (\"y\" = yes, \"n\" = no): ")

    if junkcodeInput == "y":
        CreateJunkCode()

    FirstObfuscationStage()
    SecondObfuscationStage()
    FirstObfuscationStage()
    ThirdObfuscationStage()
    FirstObfuscationStage()
    FourthObfuscationStage()
    FirstObfuscationStage()
    FithObfuscationStage()

    print("File Obfuscated!")
    input()

    os.system('cls' if os.name == 'nt' else 'clear')