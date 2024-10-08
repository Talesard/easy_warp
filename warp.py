import os
import urllib.request

print ("amnezia...")
urllib.request.urlretrieve ("https://github.com/amnezia-vpn/amneziawg-windows-client/releases/download/1.0.0/amneziawg-amd64-1.0.0.msi", "amneziawg.msi")
print("wgcf (warp cli)...")
urllib.request.urlretrieve ("https://github.com/ViRb3/wgcf/releases/download/v2.2.22/wgcf_2.2.22_windows_amd64.exe", "wgcf.exe")
print ("Turn on any VPN!")
os.system ("pause")
print ("Press enter a little later")
os.system ("wgcf register")
os.system ("wgcf generate")

with open("wgcf-profile.conf", 'r') as f:
    for line in f:
        if "PrivateKey" in line:
            privatekey = line.split(" ")[2]
        if "PublicKey" in line:
            publickey = line.split(" ")[2]
text = f"[Interface]\nPrivateKey = {privatekey}Jc = 120\nJmin = 23\nJmax = 911\nH1 = 1\nH2 = 2\nH3 = 3\nH4 = 4\nAddress = 172.16.0.2/32, 2606:4700:110:81dd:e13c:3b13:c4e7:855f/128\nDNS = 1.1.1.1, 2606:4700:4700::1111, 1.0.0.1, 2606:4700:4700::1001\nMTU = 1420\n\n[Peer]\nPublicKey = {publickey}AllowedIPs = 0.0.0.0/0, ::/0\nEndpoint = 162.159.193.5:2408"
with open('WARP.conf', 'w') as f:
    f.write(text)

print ("Add WARP.conf to amnezia via GUI")
os.system ("amneziawg.msi")
