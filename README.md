# whmcs-captcha-solver

WHMCS is an automation platform that simplifies and automates all aspects of operating an online web hosting and domain registrar business. It is widely used for different purposes.

## captcha

WHMCS provides at least two types of captchas, one is the traditional captcha with 5 characters and a simple background (but no noise in this case). Also there is reCaptcha provided for better security and you should always choose this option over the traditional one.

## here's why

Below, you can see a sample of the traditional captcha provided in one of the latest versions of whmcs.

![alt text](https://github.com/Pmoonesi/whmcs-captcha-solver/blob/master/verifyimage.png?raw=true)

As you can see it is a pretty simple one. All I needed to do was to gather an appropriate dataset, create the model and start training.

## dataset

The captcha is produced using a php script named as `verifyimage.php`. All I needed to do was to find this on the internet and run it a few thousand times. So, that was what I did ([verifyimage.php](https://github.com/puarudz/WHMCS-7.8.0-decoded/blob/master/includes/verifyimage.php)).
You can also find the script I used to create my datasets under `util/captcha.php`.

## training

I used [CaptchaCracker](https://github.com/WooilJeong/CaptchaCracker) for training which is really straightforward and easy to use. In addition, you can see the notebook I used to train my model in `whmcs_captcha.ipynb`. Moreover, I used Google Colab for my computations.
Finally, the accuracy of the model was 99% which was anticipated because of the simplicity of the captchas.

## webserver

I also created a tiny webserver using fastAPI for which you can find the code in `http-server`. You have to install the dependencies mentioned in the requirements.txt file before running the webserver. Also make sure you have tensorflow installed. I recommend using tensorflow on docker if you don't already have it installed.
To start the server you should just run `python main.py`.
