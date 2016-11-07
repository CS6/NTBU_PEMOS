

<?php
// Use fopen function to open a file
$file = fopen("family.txt", "r");
// Read the file line by line until the end
while (!feof($file)) {
$value = fgets($file);
print "The value of this line is " . $value . "<br>";
}
// Close the file that no longer in use
fclose($file);
?>
