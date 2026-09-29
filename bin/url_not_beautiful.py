#!/usr/bin/env python3
import sys
from urllib.parse import parse_qsl, urlparse, unquote, unquote_plus

def unnecessary_pct(encoded, reserved_ok):
	unreserved = set(
		"ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-._~"
	)
	out = []
	i = 0
	while i < len(encoded):
		if encoded[i] == "%" and i + 2 < len(encoded):
			hexpart = encoded[i + 1 : i + 3]
			try:
				byte = int(hexpart, 16)
			except ValueError:
				i += 1
				continue
			ch = bytes([byte]).decode("latin1")
			if ch in unreserved:
				out.append("%" + hexpart + " encodes unreserved " + repr(ch))
			i += 3
			continue
		i += 1
	return out

def reasons_for(url):
	if "%" not in url and "+" not in url.split("?", 1)[-1]:
		return []
	reasons = []
	parsed = urlparse(url, allow_fragments=True)
	path_dec = unquote(parsed.path)
	if path_dec != parsed.path and path_dec.split("/") == parsed.path.split("/"):
		reasons.extend(unnecessary_pct(parsed.path, set("/")))
		if "%" in parsed.path:
			reasons.append("path can be stored decoded")
	if parsed.query:
		naive = unquote_plus(parsed.query)
		decoded_ok = (
			naive.count("&") == parsed.query.count("&")
			and naive.count("=") == parsed.query.count("=")
		)
		if decoded_ok:
			for raw in parsed.query.split("&"):
				reasons.extend(unnecessary_pct(raw, set("=&")))
			if "%" in parsed.query or "+" in parsed.query:
				reasons.append("query can be stored decoded")
	if parsed.fragment and "%" in parsed.fragment:
		if unquote(parsed.fragment).count("?") == parsed.fragment.count("?"):
			reasons.append("fragment can be stored decoded")
	if parsed.netloc and "xn--" in parsed.netloc:
		reasons.append("host uses punycode; prefer the decoded hostname")
	seen = []
	for r in reasons:
		if r not in seen:
			seen.append(r)
	return seen

if __name__ == "__main__":
	url = sys.argv[1] if len(sys.argv) > 1 else ""
	for line in reasons_for(url):
		print(line)

