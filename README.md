# onehitweb
Web server written in one file that serves one page

Why one hit? Think of a one hit wonder: this servers exactly one file,
as in you can request anything you want and will only get back the
file configured in the code (or fed to it). 

This was written as a quick way to provide a 
kickstarter(RedHat/CentOS)/preseed(Debian/Ubuntu) config file without having 
to put together a proper webserver. Of course, in a large scale setup you do
use a real webserver which selects the right config file, but this is not
that.


