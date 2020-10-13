import sys, re
import argparse, requests

parser = argparse.ArgumentParser(description = "get js variable names from either a javascript file or a list of javascript urls.")

parser.add_argument('-u', '--url', default=False, action="store_true", help="Setting this will take a url or a list of urls from stdin, omitting it will take a javascript file on stdin.")
args = parser.parse_args()

def read_in():
	# Read contents of stdin
	return [x.strip() for x in sys.stdin.readlines()]

def get_varnames(data):
	matches = []
	for match in re.findall(r'([a-zA-Z0-9-_$]*) ?=', data):
		matches.append(match)
	return matches

params = set()

if args.url:
	urls_list = read_in()
	for url in urls_list:
		response = requests.get(url).text
		for match in get_varnames(response):
			params.add(match)
else:
	input_data = ' '.join(read_in())
	for match in get_varnames(input_data):
		params.add(match)

for param in params:
	print(param)
