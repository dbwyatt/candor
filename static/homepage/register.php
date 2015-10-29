<?php
	
	function register($firstname, $lastname, $email) {
		include 'settings.php';
		// Connect to server and select databse.
		// $conn = mysqli_connect("$host", "$username", "$password", "$db_name", "$port");
		// mysqli_select_db("$db_name")or die("cannot select DB");
		// $conn = new mysqli($host, $username, $password, $db_name);

		// username and password sent from form 
		// $firstname = $_POST['firstname']; 
		// $lastname = $_POST['lastname']; 
		// $email = $_POST['email'];

		$error = Array();
		if ($firstname == '') {
			$error['first-name'] = 1;
		}
		if ($lastname == '') {
			$error['last-name'] = 1;
		}
		if ($email == '') {
			$error['email'] = 1;
		}
		if (!empty($error)) {
			// var_dump($error);
			return json_encode($error);
		}
		else {
			// To protect MySQL injection (more detail about MySQL injection)
			// $firstname = stripslashes($firstname);
			// $lastname = stripslashes($lastname);
			// $email = stripslashes($email);
			
			// $firstname = mysqli_real_escape_string($firstname);
			// $lastname = mysqli_real_escape_string($lastname);
			// $email = mysqli_real_escape_string($email);
			
			// $sql = "INSERT INTO $tbl_name (first_name, last_name, email) VALUES ('$firstname', '$lastname', '$email')";
			// $result = mysqli_query($conn, $sql);

			$mysqli = new mysqli("$host", "$username", "$password", "$db_name", "$port");
			if ($mysqli->connect_errno) {
			    echo "Failed to connect to MySQL: (" . $mysqli->connect_errno . ") " . $mysqli->connect_error;
			}

			/* Prepared statement, stage 1: prepare */
			if (!($stmt = $mysqli->prepare("INSERT INTO $tbl_name (first_name, last_name, email) VALUES (?,?,?)"))) {
			     echo "Prepare failed: (" . $mysqli->errno . ") " . $mysqli->error;
			}

			/* Prepared statement, stage 2: bind and execute */
			if (!$stmt->bind_param("sss", $firstname, $lastname, $email)) {
			    echo "Binding parameters failed: (" . $stmt->errno . ") " . $stmt->error;
			}

			if (!$stmt->execute()) {
			    echo "Execute failed: (" . $stmt->errno . ") " . $stmt->error;
			}
			else {
				$result = true;
			}

			/* explicit close recommended */
			$stmt->close();
			$mysqli->close();



			// Mysql_num_row is counting table row
			// $count = mysql_num_rows($result);

			// If result is not 1
			if ($result){
				// Register $myusername, $mypassword and redirect to file "login_success.php"
				return true;
			}
			else {
				return false;
			}
		}
	}
?> 