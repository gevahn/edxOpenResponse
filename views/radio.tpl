<head>
<script src=jschannel1.js></script>
<link rel="stylesheet" type="text/css" href="https://files.edx.org/fonts/edx-fonts/open-sans/open-sans.css">
<style>
h1 {
	font-family: "Open Sans";
	font-size: 20px;
    font-weight: normal;

}
p {
	font-family: "Open Sans";
	font-size: 16px;
}
textarea {
	font-family: "Open Sans";
	font-size: 16px;
}
input {
	font-family: "Open Sans";
	font-size: 16px;
}
</style>
</head>
<body>
	<h1>What is Entropy?</h1>
    <form action="/" method="post">
        <textarea name="ans" rows="5" cols="50">
{{textarea}}
		</textarea><br><br>
        <input value="Parse" type="submit" />
    </form>
<div id = "radioButtonAnswers" style={{style}}>
	<h1>Choose the answer that most closely resembles yours:</h1>
	<form action="">
		<p><input type="radio" id="ans0" name="ans" value={{scores[0]}} onclick="handleClick(this);">{{responses[0]}}</p>
		<p><input type="radio" id="ans1" name="ans" value={{scores[1]}} onclick="handleClick(this);">{{responses[1]}}</p>
		<p><input type="radio" id="ans2" name="ans" value={{scores[2]}} onclick="handleClick(this);">{{responses[2]}}</p>
	</form>
</div>
    <script>
		var radio_value = 5;
		var channel;

    // Establish a channel only if this application is embedded in an iframe.
    // This will let the parent window communicate with this application using
    // RPC and bypass SOP restrictions.
    if (window.parent !== window) {
        channel = Channel.build({
            window: window.parent,
            origin: "*",
            scope: "JSInput"
        });

        channel.bind("getGrade", getGrade);
        channel.bind("getState", getState);
        channel.bind("setState", setState);
    }


		function handleClick(radioButton) {
			radio_value = radioButton.value;

		}
	   
		function getGrade() {
			console.log(radio_value);
			if (radio_value == 2) {
				console.log(JSON.stringify({"Answer":true}));
			    return JSON.stringify({"Answer":true});
			}
			else {
				console.log(JSON.stringify({"Answer":false}));
			    return JSON.stringify({"Answer":false});				
			}
		}

		function getState() {
		    return JSON.stringify({"Answer":radio_value});
		}


		function setState() {
		}

</script>
	
</body>
