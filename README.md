# Launchpad Pro95 - Gong Edition

## New README

Hi, Richard Gong here.

I'm using this script to customize the hell out of my Ableton Live, via my Launchpad Pro.

Forked from the original Launchpad Pro95 script.

Thank God for open source software!

## See diff

How is this different from the Official Launchpad Pro95 script?

See here for diff: https://github.com/hdavid/Launchpad_Pro95/compare/master...richgong:master


## To install

```
cd "/Applications/Ableton Live 10 Suite.app/Contents/App-Resources/MIDI Remote Scripts" # mac
cd /c/ProgramData/Ableton/Live\ 10\ Suite/Resources/MIDI\ Remote\ Scripts # windows

ln -s ~/c/Launchpad_Pro95/ Launchpad_Pro95
# then set "Control Surface" to Launchpad_Pro95 in Preferences
```

## MPK Mini

For MPK Mini, I copied the .pyc files from "MIDI Remote Scripts" and ran

```
pip install uncompyle6
uncompyle6 *.pyc
```

---

## Old README

Launchpad Pro95 : Improved Novation Launchpad Pro remote scripts with Instrument Mode, Scales, Step Sequencer and Device Controller.

These scripts are modified version of Ableton Live 9.5 scripts for Novation Launchpad and provide the same functionality but add support for editing the midi clips using a step sequencer and Device Controller. It also replaces Note Mode one with an Instrument Mode mimicking Ableton Push Instrument Mode behaviour.

It does not require any external tool like Max for Live (M4L) in order to work. This script is just a plain Live Control Surface Python Script. 

manual and download : http://motscousus.com/stuff/2015-12_Novation_Launchpad_Pro_Ableton_Live_Scripts/

