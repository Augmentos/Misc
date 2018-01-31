<?php 
	require 'db.php';
	$basePath = "./filesFolder";
	$sql = "SELECT `id`, `date`, `fileName`, `flag` FROM files";
	$result = mysqli_query($conn, $sql);
	if (mysqli_num_rows($result) > 0) {
	    // output data of each row
	    while($row = mysqli_fetch_assoc($result)) {
	        if(file_exists($basePath.'/'.$row["fileName"])) {
	        	if( is_dir($basePath.'/'.$row["date"]) === false ) {			
				 echo "Creating directory...";
				 $dirName = str_replace("-", "", $row['date']);
	    		 mkdir($basePath.'/'.$dirName,0777);
			 }
	        	rename($basePath.'/'.$row["fileName"],  $basePath.'/'.$dirName.'/'.$row["fileName"]);
	        	$check = "UPDATE `files` SET `flag` = 1 WHERE `id` = ". $row['id'];
	        	mysqli_query($conn, $check);
	        	echo "File Moved.";
	        }
	        else { 
	        	$check = "UPDATE `files` SET `flag` = 0 WHERE `id` = ". $row['id'];
        		if (mysqli_query($conn, $check)) {
				    echo "Record updated successfully";
				} 
				else {
				    echo "Error updating record: " . mysqli_error($conn);
				}
	        }
		}
	} 
	else {
	echo "0 results";
	}

 ?>