In case you've got an error:
"selenium.common.exceptions.SessionNotCreatedException: 
Message: session not created: This version of ChromeDriver 
only supports Chrome version X"

Go to https://chromedriver.chromium.org/downloads 
and download the chromedriver version that suits your Chrome 
browser version. Delete the existing chromedriver file, extract
a new one from downloaded archive and delete the archive.

If you're using OS other than Windows, you're also have to change 
path to the chromedriver file in vocalizer.py code.

If you're 2 lazy, run the update_chromedriver.py program like:
update_chromedriver.py [driver verison] [platform]



driver version = any existing, the last chromedriver version 
                 will be downloaded

platform = accepts only win32, linux, mac