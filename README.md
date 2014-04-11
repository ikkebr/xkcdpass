## Inspiration
![The Inspiration](http://imgs.xkcd.com/comics/password_strength.png)

This script was inspired by the above xkcd strip, [this](http://preshing.com/20110811/xkcd-password-generator/) post by Jeff Preshing, and the letter D.
This port was inspired by Daniel McGraw's code, available at https://github.com/danielmcgraw/xkcdpass

## Install

xkcdpass is a python script, so drop it and the dictionary in the same place and make sure it's added
to your `$PATH`.

## Usage

Just run xkcdpass and you will get a random four word password chosen from 5000 common english words.

    ./xkcdpass.py
    scary cost couch thigh

You can also specify the number of words you'd like your password to be made of by passing the **-l** or **--length** option.

    ./xkcdpass.py -l 6
    walk office face bloody come controversy

If the you'd rather use a different dictionary, such as your machines word list, by passing the **-d** or **--dictionary** option.

    ./xkcdpass.py --dictionary=/usr/share/dict/words
    cryptographist pseudograph amoebae overwhelmingness
