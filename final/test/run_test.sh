#!/bin/sh
c=0
for library in lib*
do
        holder="${library}_result"
        bad_holder="${library}_bad_result"
        echo $holder
        mkdir $holder
        mkdir $bad_holder
        while [[ $c -lt 100 ]]
        do
                { time ./../pynwheel.py --file ./$library; } 2> ./$holder/tester; cat ./$holder/tester | grep real > ./$holder/$c.txt
                { time ./$library; } 2> ./$bad_holder/tester; cat ./$bad_holder/tester | grep real > ./$bad_holder/$c.txt
                let c=c+1
        done
        rm ./$holder/tester
        rm ./$bad_holder/tester
        let c=0
done

