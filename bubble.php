<?php
// bubble sort algorithm in php

function bubbleSort() {
    $array = func_get_args();
    $count = func_num_args();

    for($i = 0; $i < $count; $i++) {
        for($j = 0; $j < $count - 1; $j++) {
            if($array[$j] > $array[$j + 1]) {
                $temp = $array[$j];
                $array[$j] = $array[$j + 1];
                $array[$j + 1] = $temp;
            }
        }
    }

    return $array;
}

$sorted_arr = bubbleSort(9, 6, 4, 8, 3, -7, 2, 1, 5);

error_log(print_r($sorted_arr, true));

// select sort algorithm in php
function selectSort() {
    $array = func_get_args();
    $count = func_num_args();
    
    $min_index = 0;
    for($i = 0; $i < $count; $i++) {
        $min_index = $i;
        for($j = $i + 1; $j < $count; $j++) {
            if($array[$j] < $array[$min_index]) {
                $min_index = $j;
            }
        }
        if($min_index != $i) {
            $temp = $array[$i];
            $array[$i] = $array[$min_index];
            $array[$min_index] = $temp;
        }
    }

    return $array;
}

$select_arr = selectSort(-9, 6, 4, 8, 3, 7, 2, 1, 5);
error_log(print_r($select_arr, true));