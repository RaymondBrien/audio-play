# idea brainstorm:

*big picture: freq to hex (int to #0000000)*

## RESEARCH:

https://newt.phys.unsw.edu.au/jw/notes.html

- freq - integer representing Hz 
    - max range human can hear:
      - 20 to 17,000 Hz
    - most likely range for this purpose (imagine a lead melodic line):
      - 21Hz to 4186Hz (range of piano)

    - for now, let's assume no microtones:
      - 4165 possible frequencies
        - TODO: later, make
        - TODO add bins safety by rounding down to the nearest of the 4165 notes considered


- hex - str, of # then 6 digits
    - 16,777,216 possible colors
      - 4028 colors (16,777,216 // 4165 possible frequencies)
      - 671 colors per slot (6 in total in hex format)
        - or 1342 colors per 2-chunk slot

    - Darkest:
        #000000 - This hex colour code represents pure black colour
    - Lightest:
        #FFFFFF - This hex colour code represents pure white colour.

Alt bins:
        #FF0000 - This hex colour code represents pure red colour.
        #0000FF - This hex colour code represents blue colour.
        #FFFF00 - This hex colour code represents yellow colour.
        #00FFFF - This hex colour code represents Cyan colour.
        #FF00FF - This hex colour code represents Magenta colour.
        #00FF00 - Mixture of red and green colour, defined as yellow.
        #0000FF - Mixture of more green and maximum blue obtains colour like the sky.

____

Logic:

Higher the frequency, the brighter the color and the longer it lasts for
The lower the freq, the darker the color

safety:
    - is there a defined 'safe' range in dB I will handle?
    - ensure rounding to x amount of digits to ensure not too expensive
        - (can edit or extended logic for more features later if needed)

____


Map hex logic:
- what is bright
- what is dark


- how do increments on that scale work?


Conversion logic:

- safety:
    - ensure freq is int
    - ensure freq is within expected range

    - ensure hex (final result after conversion from freq) is:
        - str only
        - in correct format (contains # then 6 nums)
        - raises error without stopping or crashing if not
            - if raises error, defaults to a predefined backup color so the stream is unaffected

