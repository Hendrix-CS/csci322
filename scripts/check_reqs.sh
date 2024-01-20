#!/bin/zsh
for d in *(/); do
    echo '----------';
    echo $d;
    ls $d/*.(hdl|asm) | cut -d'/' -f2 | comm -23 reqs.txt -;
done
