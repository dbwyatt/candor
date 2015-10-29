<?php
	include '../includes/register.php';
	
	$firstname = $_POST['firstname']; 
	$lastname = $_POST['lastname']; 
	$email = $_POST['email'];

	$data = register($firstname, $lastname, $email);
	echo $data;
?> 