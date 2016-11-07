<html>
<body>
<?php

    $filename = "test.txt";
    $result = array();
 
    if ( file_exists($filename) ) {
        $file = fopen( $filename, "r" );
  
        if ( $file != NULL ) {
            while ( !feof($file) ) {
                $result[] = fgets( $file );  //  fgets一次抓一行
            }  //  while 
   
            fclose( $file );
        }  //  if  判斷檔案內容是否為空
    }  //  判斷是否有該檔案
 
    echo join("</br>", $result);

?>
</body>
</html>
