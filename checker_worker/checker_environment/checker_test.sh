#!/usr/bin/env bash
no_proc=$1
executable="tema3"
export OMPI_MCA_btl_vader_single_copy_mechanism=none

# mpicc homework.c -o tema3
# make > /dev/null

#echo -e "Corectness"

filters=(
    "emboss"
    "smooth"
    "sharpen"
    "mean"
    "blur"
    "bssembssem"
)

pgm_images=(
    "despicable-me"
    "landscape"
    "macro"
)

pnm_images=(
    "macro"
    "scroll-of-truth"
)

correct=0
total=0


for p in "${pgm_images[@]}"; do
    #echo -e "image: $p.pgm"
    for i in "${filters[@]}"; do
        #echo -e "$i filter\n"
        total=$((total+1))

        if [ "$i" == "bssembssem" ]; then
            mpirun -np 1 $executable in/PGM/$p.pgm bssembssem1.pgm blur smooth sharpen emboss mean blur smooth sharpen emboss mean
            mpirun -np 2 $executable in/PGM/$p.pgm bssembssem2.pgm blur smooth sharpen emboss mean blur smooth sharpen emboss mean
            mpirun -np 4 $executable in/PGM/$p.pgm bssembssem3.pgm blur smooth sharpen emboss mean blur smooth sharpen emboss mean

            ok_diff1=$(diff bssembssem1.pgm bssembssem2.pgm | wc -l)
            ok_diff2=$(diff bssembssem2.pgm bssembssem3.pgm | wc -l)
            ok_diff3=$(diff bssembssem3.pgm bssembssem4.pgm | wc -l)
            if (( $ok_diff1 == 0 )) && (( $ok_diff2 == 0 )) && (( $ok_diff3 == 0 )); then
                #echo "Diff ok"
                ok_compare_py=$(python3 compare.py ref/pgm/$p-bssembssem.pgm bssembssem1.pgm)
                if [[ $ok_compare_py == "Images are equal." ]]; then
                    correct=$((correct+1))
                    #echo -e "compare.py ok\n"
                # else
                    #echo -e "compare.py NOT ok\n"
                fi
            # else
                #echo -e "Diff NOT ok\n"
            fi
        else
            mpirun -np 1 $executable in/PGM/$p.pgm "${i}1.pgm" $i
            mpirun -np 2 $executable in/PGM/$p.pgm "${i}2.pgm" $i
            mpirun -np 4 $executable in/PGM/$p.pgm "${i}3.pgm" $i

            ok_diff1=$(diff ${i}1.pgm ${i}2.pgm | wc -l)
            ok_diff2=$(diff ${i}2.pgm ${i}3.pgm | wc -l)
            ok_diff3=$(diff ${i}3.pgm ${i}4.pgm | wc -l)
            if (( $ok_diff1 == 0 )) && (( $ok_diff2 == 0 )) && (( $ok_diff3 == 0 )); then
                #echo "Diff ok"
                ok_compare_py=$(python3 compare.py ref/pgm/$p-$i.pgm ${i}1.pgm)
                if [[ $ok_compare_py == "Images are equal." ]]; then
                    correct=$((correct+1))
                    #echo -e "compare.py ok\n"
                # else
                    #echo -e "compare.py NOT ok\n"
                fi
            # else
                #echo -e "Diff NOT ok\n"
            fi
        fi
        rm *pgm *pnm 2> /dev/null
    done
done


for p in "${pnm_images[@]}"; do
    #echo -e "image: $p.pnm"
    for i in "${filters[@]}"; do
        #echo -e "$i filter\n"
        total=$((total+1))
        if [ "$i" == "bssembssem" ]; then
            mpirun -np 1 $executable in/PNM/$p.pnm bssembssem1.pnm blur smooth sharpen emboss mean blur smooth sharpen emboss mean
            mpirun -np 2 $executable in/PNM/$p.pnm bssembssem2.pnm blur smooth sharpen emboss mean blur smooth sharpen emboss mean
            mpirun -np 4 $executable in/PNM/$p.pnm bssembssem3.pnm blur smooth sharpen emboss mean blur smooth sharpen emboss mean

            ok_diff1=$(diff bssembssem1.pnm bssembssem2.pnm | wc -l)
            ok_diff2=$(diff bssembssem2.pnm bssembssem3.pnm | wc -l)
            ok_diff3=$(diff bssembssem3.pnm bssembssem4.pnm | wc -l)
            if (( $ok_diff1 == 0 )) && (( $ok_diff2 == 0 )) && (( $ok_diff3 == 0 )); then
                #echo "Diff ok"
                ok_compare_py=$(python3 compare.py ref/pnm/$p-bssembssem.pnm bssembssem1.pnm)
                if [[ $ok_compare_py == "Images are equal." ]]; then
                    correct=$((correct+1))
                    #echo -e "compare.py ok\n"
                # else
                    #echo -e "compare.py NOT ok\n"
                fi
            # else
                #echo -e "Diff NOT ok\n"
            fi
        else
            mpirun -np 1 $executable in/PNM/$p.pnm "${i}1.pnm" $i
            mpirun -np 2 $executable in/PNM/$p.pnm "${i}2.pnm" $i
            mpirun -np 4 $executable in/PNM/$p.pnm "${i}3.pnm" $i

            ok_diff1=$(diff ${i}1.pnm ${i}2.pnm | wc -l)
            ok_diff2=$(diff ${i}2.pnm ${i}3.pnm | wc -l)
            ok_diff3=$(diff ${i}3.pnm ${i}4.pnm | wc -l)
            if (( $ok_diff1 == 0 )) && (( $ok_diff2 == 0 )) && (( $ok_diff3 == 0 )); then
                #echo "Diff ok"
                ok_compare_py=$(python3 compare.py ref/pnm/$p-$i.pnm ${i}1.pnm)
                if [[ $ok_compare_py == "Images are equal." ]]; then
                    correct=$((correct+1))
                    #echo -e "compare.py ok\n"
                # else
                    #echo -e "compare.py NOT ok\n"
                fi
            # else
                #echo -e "Diff NOT ok\n"
            fi
        fi
        rm *pgm *pnm 2> /dev/null
    done
done

# make clean > /dev/null

echo $correct
echo $total
