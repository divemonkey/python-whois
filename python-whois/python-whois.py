#
# Python 3 whois class
# 
# Released as open source by Matt Summers
# 
# Developed by Matt Summers
#
# http://www.github.com/divemonkey/python-whois
#
# Released under AGPL see LICENSE for more information#
#

import socket
import sys

class WhoisClient(object):

	WHOIS_SERVER[0][0] = [
	[".com", "whois.internic.net"],
	[".net", "whois.internic.net"],
	[".org", "whois.internic.net"]
	]
	
#---- END OF WhoClient class def ----