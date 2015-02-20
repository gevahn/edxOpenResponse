var Grader = (function(document) {
	var radio_value;

		function handleClick(radioButton) {
			radio_value = radioButton.value;
		}
   
    function getGrade() {
        return JSON.stringify({"Answer":radio_value});
    }

    function getState() {
        return JSON.stringify({"Answer":5});
    }


    function setState() {
    }

    return {
        getState: getState,
        setState: setState,
        getGrade: getGrade
    };
})(document);


