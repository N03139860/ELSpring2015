< ?php
$db = new SQLite3('../../misc/local.db');
$results = $db->query('SELECT * FROM temperature');
while ($row = $results->fetchArray()) {
var_dump($row);
}
?>