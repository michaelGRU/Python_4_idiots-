Option Explicit

Dim oPlayer, chloe, cmd 
Set oPlayer = CreateObject("WMPlayer.OCX")
Set chloe = CreateObject("SAPI.spvoice")

Set chloe.Voice = chloe.GetVoices.Item(1)

chloe.speak "Incoming transmission. Standby."
wscript.sleep 2000

oPlayer.URL = "C:\icons\welcome_aboard.mp3"
oPlayer.controls.play 
While oPlayer.playState <> 1 
  WScript.Sleep 100
Wend
oPlayer.close
oPlayer.URL = "C:\icons\win95.wav"
oPlayer.controls.play 
While oPlayer.playState <> 1 
  WScript.Sleep 100
Wend
oPlayer.close

Set cmd = CreateObject("wscript.shell")
cmd.run "C:\Cmder.exe"


