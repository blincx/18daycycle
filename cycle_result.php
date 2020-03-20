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

<!--<canvas id="myCanvas" width="360" height="360" style="border:1px solid #d3d3d3; z-index: 1;" />
<canvas id="background" width="360" height="360" style="z-index: 2;" /> -->

<style>
.wrapper {
  position: relative;
  padding-top: 36.25%; /* 16:9 Aspect Ratio */
}
img {
  position: absolute;
  left: 0;
  top: 0;
  width: 100%;
  height: auto;
  max-width: 800px;
}

.centered {
  position: absolute;
  top: -50%;
  left: -50%;
  right: -50%;
  bottom: -50%;
  margin: auto;
}
</style>
</head>


<body>
<div id="container" class="wrapper">

</div>


<script>
function show_image(src, alt) {
    var img = document.createElement("img");
    img.src = src;
    img.alt = alt;
    // This next line will just add it to the <body> tag
    img.className = "img centered";
    container = document.getElementById("container");
    container.appendChild(img);
}



var data = <?=$output?>;
var today = data['today'];
var which_img_to_show = "pics/cyc_".concat(today).concat(".jpg");



window.onload = show_image(which_img_to_show, "cycle_sine");

</script>


</body>

