<?php

include("connection.php");
$query = "select * from record";
$data = mysqli_connect($conn, $query);
$total = mysqli_num_rows($data);
echo "$total";

if($total != 0)
{
    echo "Table has records";
}
else{
    echo "No records found";
}
?>