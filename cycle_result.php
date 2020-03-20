
<?php 
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // …
    $cwd = getcwd();
    $birthdate = $_POST['birthday'];
    echo $birthdate;
    $command = escapeshellcmd($cwd . '/' . 'cycle18.py ' . $birthdate . ' json');
    $output = shell_exec($command);
    // echo $output;
}

?>

<canvas id="myCanvas" width="360" height="360" style="border:1px solid #d3d3d3; z-index: 1;" />
<canvas id="background" width="360" height="360" style="z-index: 2;" />

<script>
var today = "<?php echo $today ?>";
//var data = JSON.parse(serverdata);

var data = <?=$output?>;
var today = data['today'];

console.log(today);

var c = document.getElementById("myCanvas");
var ctx = c.getContext("2d");
var i;
for(i=0; i<360; i+= 20){
    if ((i/20)==today) {
        console.log("TODAY IS THE GREATEST!");

    }
    ctx.moveTo(i+5,180);
    ctx.lineTo(i,180);
}
ctx.stroke();

var counter = 0, x=0,y=180;


//100 iterations
var increase = 90/180*Math.PI / 9;
for(i=0; i<=360; i+=9.5){
    ctx.moveTo(x,y);
    x = i;
    y =  180 - Math.sin(counter) * 120;
    counter += increase;
     
    ctx.lineTo(x,y);
    ctx.stroke();
    //alert( " x : " + x + " y : " + y + " increase : " + counter ) ;

}
</script>

