<?php 
	require 'dbPDO.php';
	$basePath = "./filesFolder";
	$sql = "SELECT `id`, `date`, `fileName`, `flag` FROM files";
	$result = $pdo->query($sql);

	    while($row = $result->fetch()) {
	        if(file_exists($basePath.'/'.$row["fileName"])) {
	        	if( is_dir($basePath.'/'.$row["date"]) === false ) {			
				 echo "Creating directory...";
				 $dirName = str_replace("-", "", $row['date']);
	    		 mkdir($basePath.'/'.$dirName,0777);
			 }
	        	rename($basePath.'/'.$row["fileName"],  $basePath.'/'.$dirName.'/'.$row["fileName"]);
	        	
	        	$stmt = $pdo->prepare("UPDATE `files` SET `flag` = 1 WHERE `id` = ?");
	        	$stmt->execute([$row['id']]);	        	
	        	echo "File Moved.";
	        }
	        else { 
	        	$stmt = $pdo->prepare("UPDATE `files` SET `flag` = 0 WHERE `id` = ?");
	        	
        		if ($stmt->execute([$row['id']])) {
				    echo "Record updated successfully";
				} 
				else {
				    echo "Error updating record: ";
				}
	        }
		}
 ?>