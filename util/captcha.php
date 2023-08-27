<?php
function generateNewCaptchaCode()
{
    $alphanum = "ABCDEFGHIJKLMNPQRSTUVWXYZ123456789";
    $rand = substr(str_shuffle($alphanum), 0, 5);
    return $rand;
}


for ($i = 1; $i <= 1000; $i++) {

    $padded_i = sprintf("%05d", $i);
    
    $rand = generateNewCaptchaCode();
    
    $image = imagecreatefrompng('./verify.png');
    
    $textColor = imagecolorallocate($image, 0, 0, 0);
    imagestring($image, 5, 28, 4, $rand, $textColor);
    
    imagepng($image, './test/' . $rand . '.png');

    // imagepng($image, './captcha/dataset/images/' . $padded_i . '.png');
    // file_put_contents('./captcha/dataset/labels/' . $padded_i . '.txt', $rand);
    
    imagedestroy($image);

}

?>
