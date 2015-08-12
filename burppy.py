#!/usr/bin/env python
######################

import xml.etree.cElementTree as et
import re
import sys
import base64

def init_file(in_file):

	print "\033[1;32m[+]\033[0m Initialising '%s'" % in_file

	try:
		content = open(in_file).read()
		return et.XML(content)
	except:
		print "\033[1;31m[!]\033[0m Could not access file: %s" % in_file
		exit(1)

def parse_req_resp(xml):
	
	resp_reqs = []
	print "\033[1;32m[+]\033[0m Parsing requests..."

	for item in xml:
		tmp = []

		for request in item.findall("request"):
			try:
				tmp.append(base64.b64decode(request.text).split("\r")[0])
			except:
				tmp.append("{empty}")

		for response in item.findall("response"):
			try:
				tmp.append(base64.b64decode(response.text))
			except:
				tmp.append("{empty}")

		resp_reqs.append(tmp)
		tmp = []

	return resp_reqs

def get_header_content(r, hdr, verbose):

	req = []
	hdrs = []

	for p in r:
		if hdr.strip() in p[1]:
			try:
				pattern = re.compile(".*%s:.*" % hdr)
				t = re.findall(pattern, p[1])[0].strip()
			except:
				continue

			if verbose:
				hdrs.append(t)
				req.append(p[0])
			else:	
				if t not in hdrs:
					hdrs.append(t)
					req.append(p[0])

	if not verbose:
		print "\033[1;32m[+]\033[0m Unique header responses for: '%s'" % hdr
		for h in hdrs:
			print h
	else:
		print "\033[1;31m[+]\033[0m Header requests and responses for: '%s'\n" % hdr
		for h in hdrs:
			print "\033[1;32m[Request  >]\033[0m %s" % req[hdrs.index(h)]
			print "\033[1;32m[Response ?]\033[0m %s\n" % h

def usage():

	print "Usage: %s\n\nOptions:\n\t-i\tInput file\n\t-H\tHeader to search (This is case sensitive! I.E 'Server' not 'server')\n\t-v\tVerbose (This is a lot of output)\n" % sys.argv[0]

if __name__ == "__main__":

	if len(sys.argv) > 4:
		verbose = False
		if "-i" in sys.argv:
			in_file = sys.argv[sys.argv.index("-i")+1]
			xml = init_file(in_file)
			req_resp = parse_req_resp(xml)
		
		if "-H" in sys.argv:
			header = sys.argv[sys.argv.index("-H")+1]

		if "-v" in sys.argv:
			verbose = True

		get_header_content(req_resp, header, verbose)
	else:
		usage()
		exit(1)
	
