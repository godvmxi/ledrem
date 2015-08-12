# Introduction #
SOX is, as per its [home page](http://sox.sourceforge.net/), "the swiss army knife of sound processing programs".
Download the proper version for your O.S. . Available versions are:

-Redhat RPM package: i386 binary (Also available for other targets and as Source Code)

-Debian package: Debian's SoX page

-Win32 Binary (Win95/98/NT/XP/Vista): sox-14.0.1.zip

-Win32 Cygwin Binary (With Audio support): sox-14.0.1-cygwin.zip

-NetBSD: Various Binaries

-OS/2 binary: sox-12.17.1.zip

-BeOS Binary: sox-12.18.2-beos-x86-ogg.zip (with MP3 and Ogg), sox-12.18.2-beos-x86.zip and sox-12.18.2-beos-ppc.zip (from [PlanetMir](http://www.planetmir.de/html/softw.htm))

-Atari ST binary: sox12.17.2-m68k-atari.tgz (from [PlanetMir](http://www.planetmir.de/html/softw.htm)) )

-DGJPP DOS Binary


# Details #

Once you download SOX, put it into your favourite folder, open a console window, and call SOX with proper parameters to have it creating the WAV file you need.

I'll explain how to call it from DOS box as t is the system I have; you should change what's needed to get commands working on your system.

C:> sox -c1 -[r48000](https://code.google.com/p/ledrem/source/detail?r=48000) -n -t raw - synth 0.100   sine 18000  vol 1 > base.raw

This command creates a raw audio file containing a 0.100 ms long sinusoid at 18000 Hz; file has 48000 bytes per sample, but this should not affect performance; I did'nt test it, but a standard 44100Hz file should work as well.

"vol 1" means the sinusoid must have maximum amplitude; by specifying "vol 0" you get silence.

NOTE: the ">" sign means **create** the file. It must be used only in **first** line of batch file; following ones must use ">>", which means "**append**" data to existing file.
By alternating "vol 1" lines to "vol 0" lines you obtain a raw audio file made up of burst of 18000 Hz carrier interlaced by silence, which all together form your remote control signal.

The last line of the file must be something like:

sox -s2 -c1 -[r48000](https://code.google.com/p/ledrem/source/detail?r=48000) base.raw  sky000_.wav_

It converts the raw file to a stabdard WAV file at 48000 bytes/sample.


A very short example file would be:

> sox -c1 -[r48000](https://code.google.com/p/ledrem/source/detail?r=48000) -n -t raw - synth 0.000409 sine 18000 vol 0 > base.raw

> sox -c1 -[r48000](https://code.google.com/p/ledrem/source/detail?r=48000) -n -t raw - synth 0.000431 sine 18000 vol 1 >> base.raw

> sox -c1 -[r48000](https://code.google.com/p/ledrem/source/detail?r=48000) -n -t raw - synth 0.000431 sine 18000 vol 0 >> base.raw

> sox -c1 -[r48000](https://code.google.com/p/ledrem/source/detail?r=48000) -n -t raw - synth 0.000431 sine 18000 vol 1 >> base.raw

> sox -c1 -[r48000](https://code.google.com/p/ledrem/source/detail?r=48000) -n -t raw - synth 0.004318 sine 18000 vol 0 >> base.raw

> sox -s2 -c1 -[r48000](https://code.google.com/p/ledrem/source/detail?r=48000) base.raw  sky000_.wav_

# Example #
Download [this file](http://code.google.com/p/ledrem/source/browse/trunk/ledrem/sky_SKY(on).zip) to look at an example. It contains:

**sky-SKY(on).wav** - remote control sample

**Provalirc.conf** - corresponding LIRC file

**sky-SKY(on).bat** - DOS batch files which creates the final WAV file using SOX program

_sky-SKY(on)**.wav** - the final WAV file (to turn on Italian SKY Satellite receiver)_

Please check [this link](http://jumpjack.wordpress.com/2008/05/20/worlds-cheapest-remote-control-replicator-just-1/) for further details about how to create a WAV file which replicates your remote.