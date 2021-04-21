<html>
	<head>
		<title>Test</title>
	</head>
	<body>
	<?php 

	$headers = getallheaders();
	$sig = $headers['Signature'];

	$size = (int) $_SERVER['CONTENT_LENGTH'];
	
	if ($sig === hash('sha256', $size)) {

		$data = json_decode(base64_decode($_POST['input']));

		echo "input1: ";
		echo $data->input1;
		echo "\r\n";
		echo "input2: ";
		echo $data->input2;
	} else {
		echo 'Incorrect signature';
	}
	?> 
	</body>
</html>
