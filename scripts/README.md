omxplayer -o local rit_horn_short_band.wav 
mpg123 -q rit_horn_short_band.wav&

--
alsamixer -- Command line tool to adjust output volume
amixer -q sset PCM 97% -- Set volume of output
    100% = 100%
    97% = 88%
    95% = 82%
    93% = 75%
    
    -- Set with gain
    0 = 0.00 db gain (86%)
    100 = 1.00 db gain (89%)
    
    