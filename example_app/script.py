import re
import base64
import hashlib

if messageIsRequest:

	reqbytes = messageInfo.getRequest()
	req = helpers.analyzeRequest(reqbytes)
	parameters = reqbytes[(req.getBodyOffset()):].tostring()
	headers = req.getHeaders()

	val_1 = re.findall(r'input1=[^\s]*', parameters)[0].split('&')[0].split('=')[1]
	val_2 = re.findall(r'input2=[^\s]*', parameters)[0].split('&')[0].split('=')[1]

	input_val = '{"input1":"%s","input2":"%s"}' % (val_1, val_2)
	base64_val = base64.b64encode(input_val)
	output_body = r'input=%s' % base64_val

	hash_body_len = hashlib.sha256(str(len(output_body)).encode('utf-8')).hexdigest()
	sig = "Signature: " + hash_body_len
	headers.add(sig)
	
	newreq = helpers.buildHttpMessage(headers, output_body)
	messageInfo.setRequest(newreq)
