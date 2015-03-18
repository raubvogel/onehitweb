# onehitweb
Web server written in one file that serves one page

Why one hit? Think of a one hit wonder: this servers exactly one file,
as in you can request anything you want and will only get back the
file configured in the code (or fed to it). 

This Python script was written as a quick way to provide a 
kickstarter(RedHat/CentOS)/preseed(Debian/Ubuntu) config file without having 
to put together a proper webserver. Of course, in a large scale setup you do
use a real webserver which selects the right config file, but this is not
that.

It is also a way for me to learn a bit more of Python classes by putting
together a tiny (can't go smaller than a single page, right) website.
The original version has all arguments hard coded while the current one
allows you to enter the server's IP and port, and the filename/path from
command line.

Why would you want to enter the IP? If you enter the IP, it means it will
only listen on that interface/IP. If you enter nothing ("" so it counts
it as an argument), it will listen on all interfaces.
