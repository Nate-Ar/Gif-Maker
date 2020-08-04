import os
os.system('/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"')
os.system('brew install libtiff libjpeg webp little-cms2')
os.system('brew install freetype harfbuzz fribidi')
os.system('sudo pip install Pillow')