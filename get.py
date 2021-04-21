import re
import base64

if messageIsRequest:

	###--------------define scope below--------------###

	url_pattern = r'example.php' # set endpoint
	target_param = 'input' # set target parameter we want to modify the value of e.g. injecting into input=test set to input

	###--------------define scope above--------------###

	#check to see if the request is in scope
	url = messageInfo.url.toString()
	if re.search(url_pattern, url):

		#retrieve req information using the burp extender api 
		reqbytes = messageInfo.getRequest()
		req = helpers.bytesToString(reqbytes)
		
		#build regex string from target parameter, does not need to be modified
		regex = r'%s=[^\s]*' % target_param
		
		#get the target parameter and value from the request body
		input_param = re.findall(regex, req)[0].split('&')[0]
		input_val = input_param.split('=')[1]

		###--------------modify below--------------###
		#print(input_val)

		#modify the input value in some way, here it is just base64 decoding
		output_val = base64.b64encode(input_val)

		#print(output_val)
		###--------------modify above--------------###
		
		#create output request parameter value pair e.g. input=base64(test)
		output_param = r'%s=%s' % (target_param, output_val)

		#create output request body, e.g. combine output param with the other parameters in the original request
		output_req = req.replace(input_param, output_param)
		
		#send off the modified request
		newreq = helpers.stringToBytes(output_req)
		messageInfo.setRequest(newreq)
