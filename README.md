 <h2 align="center">
  TrueNAS Scale Scripts
  </h2>
  <p align="center">
Just some scripts I use to manage/monitor my TrueNAS Scale Servers
  </p>
<h4 align="center">Be sure to  :star:  my repo so you can keep up to date on any updates and progress!</h4>
<br>
<div align="center">
    <a href="https://github.com/rjsears/truenas_scale/commits/main"><img alt="GitHub last commit" src="https://img.shields.io/github/last-commit/rjsears/truenas_scale?style=plastic"></a>
    <a href="https://github.com/rjsears/truenas_scale/issues"><img alt="GitHub issues" src="https://img.shields.io/github/issues/rjsears/truenas_scale?style=plastic"></a>
    <a href="https://github.com/rjsears/truenas_scale/blob/main/LICENSE"><img alt="License" src="https://img.shields.io/github/license/rjsears/truenas_scale?style=plastic"></a>
 <!<img alt="GitHub release (latest by date)" src="https://img.shields.io/github/v/release/rjsears/truenas_scale?style=plastic">
<img alt="GitHub contributors" src="https://img.shields.io/github/contributors/rjsears/truenas_scale?style=plastic">
</h4>
  <hr>
</div>

### <a name="overview"></a>Locate Drive

<div align="left">
<p align="left"><font size="1">
Simple python script that utilizes sas3ircu to locate the SAS controllers on your
system and then allows you to select the controller and outputs all drives on that
controller so you can blink or unblink them for location purposes. Makes finding
drives on your system easy!

Used the Rich library to output a nicely formatted table.

Works on TrueNAS Scale (Linux based) and SAS3IRCU, it might also work with
SAS2IRCU.
 
 <hr>
 <a name="locate_drives" href="https://github.com/rjsears/truenas_scale"><img src="https://github.com/rjsears/truenas_scale/blob/main/images/locate_drives_screenshot.png" alt="Locate Drives"></a><br>


### <a name="overview"></a>Installation and Usage

Download the script and chmod 755 and then simply run it. When you do it will ask you which controller and scan
that controller, outputting what you see below. You can then select `blink` or `unblink` and it will ask you what
drive. Enter the drive number, and if you are in a system supported by SAS3IRCU, it will start flashing the drive
error LED. Just rerun it again to `unblink` that drive. 



 ### <a name="dependencies"></a>Dependencies
<ul>
 <li><a href="https://support.lenovo.com/us/en/downloads/ds116901-sas3ircu-command-line-utility-for-storage-management-for-linux">SAS3IRCU Command Line Utility</a> - Required to report on SAS Controller</li>
 <li><a href="https://github.com/willmcgugan/rich">RICH</a> - Used to generate report</li>
 
 </ul>
 <hr>

## Author
**Richard J. Sears** - *richardjsears@gmail.com* - [The RS Technical Group, Inc.](http://github.com/rjsears)

## License
This project is licensed under the MIT License - see the MIT License for details

## Acknowledgments
* **My Amazing and loving family!** My wonderful wife and kids put up with all my coding and automation projects and encouraged me in everything. Without them, this project would not be possible.
* **My brother James**, who is a continual source of inspiration to me and others. Everyone should have a brother as awesome as mine!
