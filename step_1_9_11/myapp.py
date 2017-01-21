def app(environ, start_response):
	data_ = [s.split("=") for s in environ["QUERY_STRING"].split("&")]
	data = ""
	for qstr in data_:
		if len(qstr) == 2:
			data += qstr[0] + "=" + qstr[1] + "\n"
	start_response("200 OK", [
			("Content-Type", "text/plain"),
			("Content-Length", str(len(data)))
		])
	return [bytes(data, "UTF-8")] # if python 2.7 - no bytes() function here