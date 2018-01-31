<?php
$handleEng = fopen("English.txt", "r");
$handleChin = fopen("Chinese.txt", "r");
$writer = fopen('combine.txt', 'w');

if ($handleEng && $handleChin) {
    while ((($lineEng = fgets($handleEng)) !== false) && (($lineChin = fgets($handleChin)) !== false) ) {
        $lineEng = trim(preg_replace('/\s\s+/', ' ', $lineEng));
        $lineChin = trim(preg_replace('/\s\s+/', ' ', $lineChin));
        echo $lineEng ." =>  ".$lineChin;
        fwrite($writer,"'".$lineEng."'" ." =>  '".$lineChin."',\n" );
    }

    fclose($handleEng);
    fclose($handleChin);
    fclose($writer);
} else {
    // error opening the file.
} 

?>