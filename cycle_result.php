
<?php 
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // …
    $cwd = getcwd();
    $birthdate = $_POST['birthday'];
    echo $birthdate;
    $command = escapeshellcmd($cwd . '/' . 'cycle18.py ' . $birthdate . ' json');
    $output = shell_exec($command);
    echo $output;
}

?>




