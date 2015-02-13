<?php

$dir = 'sqlite:../../local.db';

$db = new PDO($dir) or die("cannot open database");

$query = "SELECT * FROM temperature";

$results = $db->query($query);

$ret = array();

foreach ($results as $row) {
$output[] = $row;
}

print_r(json_encode($output));
?>