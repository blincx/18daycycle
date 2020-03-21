<html>
<head>
<link href="http://ajax.googleapis.com/ajax/libs/jqueryui/1.8/themes/base/jquery-ui.css" rel="stylesheet" type="text/css" />
<script src="https://code.jquery.com/jquery-3.4.1.slim.min.js" integrity="sha256-pasqAKBDmFT4eHoN2ndd6lN370kFiGUFyTiUHWhU7k8=" crossorigin="anonymous"></script>


</head>
<body>



<form id="the_form" method="POST" action="cycle_result.php">
<fieldset>
<legend>18 day cycle of the adept readout:</legend>
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

if (is_safari) {
    dateinput = document.getElementById("birthday");
    dateinput.value = "MM/DD/YYYY";
}

<!-- populate from cookie-->

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

// $("#the_form").validate();
</script>




</body>
</html>
