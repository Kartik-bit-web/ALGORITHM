//This is Sort the arrays with bubble method in JavaScript:-
function sort(arr, size){
    for (i=0; i<size-1; i++){
        for(j=0; j<size-i-1; j++){
            if(arr[j] > arr[j+1]){
                var temp = arr[j];
                arr[j] = arr[j+1];
                arr[j+1] = temp;
            }
        }
    }
}
var arr = [4, 3, 5, 2, 46];
var size = arr.length;
result = sort(arr, size);
console.log(arr)

/*
Advantages:-
Bubble sort  is easy to understand and implement.
It is not require any additional memory space.
It is adatablility to different of data.

Disadvantage:-
Bubble sort has time complaexity of O(n^2) which makes it very slow.
It is not efficient for large data set
It is not stable sort algorithm, becouse element in same key value may not maintain
*/