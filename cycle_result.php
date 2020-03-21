<head>
<?php 
    if ($_SERVER['REQUEST_METHOD'] === 'POST') {
        // …
        $cwd = getcwd();
        $birthdate = $_POST['birthday'];
        echo $birthdate;

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

</head>


<body>

<div id="outer_container">
    <div id="first_container" class="container1">
        <h4 style="font-size:2vw; text-align: center;">your location today in the 18 day adept's cycle</h4>
            <div id="sinewavecontainer" class="wrapper"></div>
    </div>
    <div id="second_container" class="container2">
       <button class="button blue">See Extended Schedule</button>
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


</body>

