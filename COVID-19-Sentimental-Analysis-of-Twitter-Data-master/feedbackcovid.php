<?php
error_reporting(E_ALL ^ E_NOTICE);
$con = mysqli_connect("localhost","root","","sata"); //connecting to database
if ($con==false)
  {
  die('Could not connect: ' . mysqli_connect_error()); //if connection is unsuccessful it give a message 'could not connect'
  }

mysqli_select_db($con,"sata");
$sql="INSERT INTO fbinput (intext)
VALUES
('$_POST[DETAILS]')";
$a = $_POST['DETAILS'];

$link_address="E:\IBM hack\categ\COVID-19-Sentimental-Analysis-master\index.html";
if (mysqli_query($con, $sql)) {
   //header('Location: https://www.google.com'); exit();
   header('Location: index.html'); exit();
echo "<a href='E:/IBM hack/categ/COVID-19-Sentimental-Analysis-master/index.html'>";exit();
echo "</a>";
} else {
    echo "Error: " . $sql . "<br>" . mysqli_error($con);
}

echo "Thank you for entering the needed information";
mysqli_close($con); //closing connection to database
?>