<?php

$postParam = $_POST['name'];

$file_name = "/var/www/html/BDA_clusterizacao/hotel_tweepy_collections.txt";
$finalJson = " ";
$array = [];

$file = fopen($file_name, "r") or exit("Unable to open file!");

$finalJson .= "{\"type\": \"GeometryCollection\",\"geometries\": [";

while(!feof($file))
  {
    $string =  fgets($file);
    $array = explode("|_|", $string);
    $array[0] = str_replace("\""," ",$array[0]);
    $array[0] = str_replace("''"," ",$array[0]);
    $array[1] = str_replace("u'","'",$array[1]);
    $array[1] = str_replace("'","\"",$array[1]);
    $array[1] = str_replace("{"," ",$array[1]);
    $array[1] = str_replace("}"," ",$array[1]);

    $finalJson .= "{ " . $array[1] . ", \"text\":\" " . $array[0] . "\" },";
  }

  $finalJson = str_replace(",{ , \"text\":\" \" }", " ", $finalJson);
//  $finalJson = str_replace("\",}", "\"}", $finalJson);
//  $finalJson = str_replace("\"},{ \"textJson\": \"", " ", $finalJson);
  $finalJson = str_replace("#", " ", $finalJson);
  $finalJson = str_replace("\n", " ", $finalJson);

  $finalJson = substr($finalJson, 0, -1);
  $finalJson .= "]}";

fclose($file);

echo $finalJson;

?>
