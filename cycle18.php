<html>

<script type="text/javascript">
    var datefield=document.createElement("input")

  

    datefield.setAttribute("type", "date")
    if (datefield.type!="date"){ //if browser doesn't support input type="date", load files for jQuery UI Date Picker
        document.write('<link href="http://ajax.googleapis.com/ajax/libs/jqueryui/1.8/themes/base/jquery-ui.css" rel="stylesheet" type="text/css" />\n')
        document.write('<script src="http://ajax.googleapis.com/ajax/libs/jquery/1.4/jquery.min.js"><\/script>\n')
        document.write('<script src="http://ajax.googleapis.com/ajax/libs/jqueryui/1.8/jquery-ui.min.js"><\/script>\n') 
    }
</script>
 


<body>

<form action="cycle_result.php" method="post">
<b>Date of birth:</b>
<input type="date" id="birthday" name="birthday" size="20" pattern="[0-9]{2}/[0-9]{2}/[0-9]{4}" />
<input type="submit">

</form>

<script>

var is_safari = false;
if (navigator.userAgent.indexOf('Safari') != -1 && navigator.userAgent.indexOf('Chrome') == -1) {
        is_safari = true;
    }

if (!is_safari) {
    if (datefield.type!="date"){ //if browser doesn't support input type="date", initialize date picker widget:
        jQuery(function($){ //on document.ready
            $('#birthday').datepicker();
        })
    }
} else { // Safari
    dateinput = document.getElementById("birthday");
    dateinput.value = "MM/DD/YYYY";
}
</script>


</body>
</html>
