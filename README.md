# Auto-Likes-for-All-Videos-in-YouTube-Playlist
Auto Likes for All Videos in YouTube Playlist Using Localhost Using Selenium with python

## It will also like all the popular uploaded videos. Just open the 'Popular Uploads' section of the channel, copy the URL, and replace it in the 20th line of the 'like.py' script.

https://www.youtube.com/watch?v=FVumnHy5Tzo&t=1s&ab_channel=HelloWorld

#Watch up to 3 minutes and 46 seconds, and then remain in the remaining part copying the part of the script and save it as l.py. The script is used to automatically like a particular YouTube video with multiple accounts

## replace 20th line with playlist url in like.py file..

First, open Chrome file location and bypass the location restriction using an extension such as Touch VPN. In my case, the Chrome location(use start in: path) is

C:\Users\Hp\AppData\Local\Google\Chrome\Application

Next, in the command prompt, navigate to the Chrome directory using the command cd C:\Users\Hp\AppData\Local\Google\Chrome\Application

Then,

use the command

chrome.exe --remote-debugging-port=9222 --user-data-dir="enter your localhost path here"

to open Chrome with remote debugging enabled. In my case, the command was

chrome.exe --remote-debugging-port=9222 --user-data-dir="C:\Users\Hp\Desktop\Bots\Chromedriver\Localhost"

## then new terminal in that folder and enter like.py

After opening Chrome, paste the following two lines of code from the script into the command prompt and hit enter. This will open
The playlist URL will open and do the auto likes to all of the video in the playlist..

Finally, in the command prompt, enter "pip install Random" and hit enter to install the necessary library.

👉Note:-

👉If you have the latest version of Selenium, the code may not run

👉open cmd and enter pip uninstall selenium

And enter

pip install selenium==4.2.0

and hit enter

and

python -c "import selenium; print(selenium.version)"

𝙏𝙝𝙞𝙨 𝙞𝙣𝙛𝙤𝙧𝙢𝙖𝙩𝙞𝙤𝙣 𝙞𝙨 𝙤𝙣𝙡𝙮 𝙛𝙤𝙧 𝙚𝙙𝙪𝙘𝙖𝙩𝙞𝙤𝙣al 𝙥𝙪𝙧𝙥𝙤𝙨𝙚 𝙖𝙣𝙙 𝙬𝙚 𝙖𝙧𝙚 𝙣𝙤𝙩 𝙧𝙚𝙨𝙥𝙤𝙣𝙨𝙞𝙗𝙡𝙚 𝙛𝙤𝙧 𝙖𝙣𝙮 𝙠𝙞𝙣𝙙 𝙤𝙛 𝙞𝙡𝙡𝙚𝙜𝙖𝙡 𝙖𝙘𝙩𝙞𝙫𝙞𝙩𝙮 𝙙𝙤𝙣𝙚 𝙗𝙮 𝙩𝙝𝙞𝙨 𝙩𝙤𝙤𝙡.
