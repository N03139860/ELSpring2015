<?php



$db = sqlite_open("../../local.db");

// Depois usa-se o comando sqlite_query() e o sqlite_fetch_array()
$registros = sqlite_query($db, "SELECT * FROM temperature");
while ($i = sqlite_fetch_array($registros)) {
   print_r($i);
}
?>