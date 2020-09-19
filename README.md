<p align="center">
  <h1 align="center">Tecno Timers</h1>
  <p align="center">
    Start timers with a command and show them on an overlay.
    <br />
    <a href="https://github.com/LuisSanchez-Dev/TecnoTimers/archive/master.zip">Download</a>
    ·
    <a href="https://github.com/LuisSanchez-Dev/TecnoTimers/issues">Report Bug</a>
    ·
    <a href="https://github.com/LuisSanchez-Dev/TecnoTimers/issues">Request Feature</a>
  </p>
</p>

## Table of Contents

* [About the Project](#about-the-project)
* [Getting Started](#getting-started)
  * [Prerequisites](#prerequisites)
  * [Installation](#installation)
  * [Overlay installation](#overlay-installation)
* [Usage](#usage)
  * [Timer Command](#timer-command)
  * [Custom Command Parameters](#custom-command-parameters)
* [Contact](#contact)
* [License](#license)

## About The Project
This project was born from the need of a way to track time when the viewers redeemed Streamloots cards that have challenges that lasted for X amount of time.

The way this project was built makes it easy to use and super customizable to match your stream color scheme, this script features:
* A command with a configurable permission level to start a new timer.
* A super customizable overlay!
  * Use your own background, foreground and text color to match your stream identity.
  * Show only the timers you want to save space in your scenes.
  * Custom sound effects for timer start and timer end.
* Create your own timers for each need with custom command parameters!
  * Create your own commands for predefined timers
  * Use custom colors for each individual timer

Thanks to [@Tecno_Diana](https://www.twitch.tv/tecno_diana/) for coming up with the idea.

## Getting Started

Setting this up so you can use it is super straightforward.

### Prerequisites

Have an installation of Streamlabs Chatbot, already logged in to your accounts.
* [Download Streamlabs Chatbot](https://streamlabs.com/chatbot)

Follow this tutorial to prepare your Streamlabs Chatbot installation to accept scripts.
* [[Streamlabs Chatbot] Scripts Explained by Castorr91](https://www.youtube.com/watch?v=l3FBpY-0880&t=3s)
### Installation

1. Download the latest version of the script [**here**](https://github.com/LuisSanchez-Dev/TecnoTimers/archive/master.zip).
2. If you haven't already, open your Streamlabs Chatbot and log in to your Streamer and Bot accounts.
3. On the left side, wait for the `Scripts` tab to pop up and click it.
4. On the top right corner of the window, next to the reload button is an import script button (Arrow pointing right to a box) and select the script downloaded before.
5. You will receive a message box confirming the import, accept it.
6. The window will update and show the `Tecno Timers` script, make sure to ✔️ enable the script on the right hand side.
7. Click on the `Tecno Timers` name to see the configuration pane.

### Overlay installation
You don't need to use the overlay to enjoy text-based timers!
1. Right click on the script name and select `Insert API key` and click OK.
2. Right click on the script name and select `Open Scripts Folder`.
3. Open the `TecnoTimers-master` folder.
4. Copy the folder address at the top of the window.
5. Open OBS and add a new `Browser` source.
6. Check the ✅ Local file box and click on `Browse`.
7. Paste the address on the address bar in the new window and press enter.
8. Select the `Overlay.html` file
9. Set the Width to whatever you want (350 recommended).
10. The Height option controls how many timers will be shown at the same time:
  * Every 25 pixels a new timer will be shown
  * 1 timer bar = 25
  * 2 timer bars = 50
  * 3 timer bars = 75
11. Click on `Refresh cache of current page` and click OK.

## Usage

### Timer Command
This command will start a 30s timer with the label `Hello world`.
In the first parameter you can use any number next to the time segment (h: hours, m: minutes, s: seconds).
Timers can't last less than 10 seconds (configurable).
```
!timer <duration> <label>
!timer 30s Hello world
!timer 90s Play with one hand
!timer 10m Maruchan cooking!
!timer 2h Streaming ends
```

### Custom Command Parameters
Usually if you use Streamloots you have some cards with timed challenges like playing with one hand, playing blindfolded, dancing, etc.
For those repeating timers you can create custom commands on the `Commands` tab using the following parameters:
1. Go to the `Commands` tab.
2. Click on the ➕icon to create a new command.
3. Type your parameters in the `Response` area in the same line.

#### Default Timer Parameter
The default timer parameter was made very similar to the command.
```
$ttimer("<duration>","<label>")
$ttimer("30s","Hello world")
$ttimer("90s","Play with one hand")
$ttimer("10m","Maruchan cooking!")
$ttimer("2h","Streaming ends")
```
#### [Optional] Background, foreground and text color
You can specify custom colors when creating a custom timer using any CSS compatible color.
You can learn more about CSS colors at https://www.w3schools.com/cssref/css_colors.asp.
These parameters are optional so you can change only the background color, the text color, two of them or all of them.
* `$bgtimer("<color>")`
* `$fgtimer("<color>")`
* `$texttimer("<color>")`
```
$bgtimer("#F9D")
$fgtimer("#DC3C3F")
$textcolor("white")
$bgtimer("rgb(0,50,255)")
$fgtimer("rgba(100,110,255,0.75)")
```

An example command would be:
```
$ttimer("90s","My command") $fgtimer("#0000FF") $bgtimer("rgba(255,0,255,1)") $texttimer("#FFFF00")
```

## Contact

* Discord - luissanchezdev#6247
* Fiverr - [luissanchezdev](https://fiverr.com/luissanchezdev)
* [+52 81 1716 1989](tel:+528117161989)
* luis.sanchez.dev@hotmail.com

Remember to join the [Streamlabs Chatbot Discord server](https://discordapp.com/invite/S2d4KGg) for sfx, scripts, commands and a lot more!

## License
Licensed under GPL v3
Copyright (C) 2020 Luis Sanchez