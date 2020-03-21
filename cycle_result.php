<head>
<?php 
    if ($_SERVER['REQUEST_METHOD'] === 'POST') {
        // …
        $cwd = getcwd();
        $birthdate = $_POST['birthday'];
        echo $birthdate;

        // have to switch safari date style:
        if (strpos($birthdate, '/') !== false) {
            $birthdate = str_replace("/","-",$birthdate);
            $year1 = substr($birthdate, -4,4);
            $month1 = substr($birthdate,0,2);
            $day1 = substr($birthdate,3,2);
            $newstring = $year1 . "-" . $month1 . "-" . $day1;
            $birthdate = $newstring;
        }

        // security: filter for only numbers, no letters    
        if (preg_match("/[0-9]*-[0-9]*-[0-9]*/", $birthdate))
        {
            $command = escapeshellcmd($cwd . '/' . '18daycycle.py ' . $birthdate . ' json');
            // paranoid security check  
            if (strpos($command, 'rm ') === false) {
                if (strpos($command, ';') === false) {
                    $output = shell_exec($command);
                }        
            } 
            // echo $output;
        }
    }
?>

<link rel="stylesheet" href="styles.css">
<meta name="viewport" content="width=device-width, initial-scale=1">
</head>


<body>

<div id="outer_container">
    <div id="first_container" class="container1">
        <h4 style="font-size:2vw; text-align: center;">your location today in the 18 day adept's cycle</h4>
            <div id="sinewavecontainer" class="wrapper"></div>
    </div>
    <div id="second_container" class="container2">
       <button class="button blue" id="schedule_button">See Extended Schedule</button>
    </div>
</div>

<script>
function show_image(src, alt) {
    var img = document.createElement("img");
    img.src = src;
    img.alt = alt;
    // This next line will just add it to the <body> tag
    img.className = "img centered";
    container = document.getElementById("sinewavecontainer");
    container.appendChild(img);
}



var data = <?=$output?>;
var today = data['today'];
var which_img_to_show = "pics/cyc_".concat(today).concat(".jpg");



window.onload = show_image(which_img_to_show, "cycle_sine");

</script>




<!-- The Modal -->
<div id="myModal" class="modal">

  <!-- Modal content -->
  <div class="modal-content">
    <div class="modal-header">
      <span class="close">&times;</span>
      <h2 style="text-align: center;">&#9765;</h2>
    </div>
    <div class="modal-body">
      <p>Some text in the Modal Body</p>
      <p>Some other text...</p>
    </div>
    <div class="modal-footer">
        <br/>
    </div>
  </div>

</div>


<script>
// MODAL STUFF 
// Get the modal
var modal = document.getElementById("myModal");

// Get the button that opens the modal
var btn = document.getElementById("schedule_button");

// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close")[0];

// When the user clicks on the button, open the modal
btn.onclick = function() {
  modal.style.display = "block";
}

// When the user clicks on <span> (x), close the modal
span.onclick = function() {
  modal.style.display = "none";
}

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
  if (event.target == modal) {
    modal.style.display = "none";
  }
}
</script>



</body>

