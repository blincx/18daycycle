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


body{color:#000;background-color:#fff;font-family:sans-serif;margin:2% 5%}

.container1 {
    width: 80%;
    margin: 0 auto;
    padding: 10px;
    background: #f0e68c;
    background: #fffdb5;
    border: 1px solid;
}

.container2 {
    width: 80%;
    margin: 0 auto;
    padding: 10px;
    background: white;
}

.wrapper {
  position: relative;
  padding-top: 56.25%; /* 16:9 Aspect Ratio */
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

.button {
  position: relative;
  float: right;
  display: inline-block;
  padding: 0.618rem 1.618rem;
  cursor: pointer;
  color: #FFF;
  letter-spacing: 1px;
  text-shadow: 0 1px 2px rgba(0, 0, 0, 0.9);
  background: #434343 none repeat scroll 0% 0%;
  border: 1px solid #242424;
  border-radius: 4px;
  box-shadow:
    0 1px 0 rgba(255, 255, 255, 0.25),
    0 1px 0 rgba(255, 255, 255, 0.25) inset,
    0 0 0 rgba(0, 0, 0, 0.5) inset,
    0 1.25rem 0 rgba(255, 255, 255, 0.08) inset,
    0 -1.25rem 1.25rem rgba(0, 0, 0, 0.3) inset,
    0 1.25rem 1.25rem rgba(255, 255, 255, 0.1) inset;

  transition: all 0.2s linear 0s;

  text-align: center;
  text-decoration: none;
  /*margin: 0.618rem;*/
}

.button.blue {
  background-color: #aff9fa;
}

</style>
</head>


<body>

<div id="outer_container" class="container1">
    <h4 style="font-size:2vw; text-align: center;">your location today in the 18 day adept's cycle</h4>
        <div id="sinewavecontainer" class="wrapper">
    </div>
</div>
<div id="second_container" class="container2">
   <button class="button blue">See Extended Schedule</button>
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

