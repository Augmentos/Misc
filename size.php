<?php

$output = shell_exec("pdfinfo filename.pdf ");

// find page sizes
preg_match('/Page size:\s+([0-9]{0,5}\.?[0-9]{0,3}) x ([0-9]{0,5}\.?[0-9]{0,3})/', $output, $pagesizematches);
$width = round($pagesizematches[1]);
$height = round($pagesizematches[2]);

echo "pagecount = $pagecount <br>width = $width<br>height = $height";

?>
