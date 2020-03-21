<html>
<head>
<link href="http://ajax.googleapis.com/ajax/libs/jqueryui/1.8/themes/base/jquery-ui.css" rel="stylesheet" type="text/css" />
<script src="http://ajax.googleapis.com/ajax/libs/jquery/1.4/jquery.min.js"></script>
<script src="http://ajax.googleapis.com/ajax/libs/jqueryui/1.8/jquery-ui.min.js"></script>

<script type="text/javascript" src="checkdate.js"></script>


</head>
<body>



<form method="POST" action="cycle_result.php" onsubmit="return checkDate(this);">
<fieldset>
<legend>18 day cycle of the adept checker:</legend>
<label>Birthdate:<input type="date" id="birthday" name="birthday" size="20" required pattern="\d{1,2}/\d{1,2}/\d{4}" placeholder="mm/dd/yyyy"></label>
<input type="submit">
</fieldset>
</form>


<!--
<form action="cycle_result.php" method="post">
<b>Date of birth:</b>
<input type="date" id="birthday" name="birthday" size="20" pattern="[0-9]{2}/[0-9]{2}/[0-9]{4}" />
<input type="submit">

</form>
-->

<script>

var is_safari = false;
if (navigator.userAgent.indexOf('Safari') != -1 && navigator.userAgent.indexOf('Chrome') == -1) {
        is_safari = true;
}

if (!is_safari) {
    if (!document.support_date){ //if browser doesn't support input type="date", initialize date picker widget:
        jQuery(function($){ //on document.ready
            $('#birthday').datepicker();
        })
    }
} else { // Safari
    dateinput = document.getElementById("birthday");
    dateinput.value = "MM/DD/YYYY";
}
</script>

<!-- populate from cookie-->
<script>

window.getCookie = function(name) {
  var match = document.cookie.match(new RegExp('(^| )' + name + '=([^;]+)'));
  if (match) return match[2];
}

$( document ).ready(function() {
    dateinput = document.getElementById("birthday");
    abba = window.getCookie("cycle18");
    if (abba) {
        dateinput.value = abba;
    }
});
</script>




</body>
</html>
