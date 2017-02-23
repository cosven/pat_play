#include <stdio.h>
#include <stdbool.h>
#include <assert.h>
#include <math.h>

int test_solution();


int main(){
    test_solution();
    return 0;
}


bool isPalindrome(int x) {
    printf("x: %d\n", x);

    if (x == 0){
        return true;
    }

    if (x < 0) {
        x = -1 * x;
    }

    assert( x >= 0 );

    int length = 1;
    int quotient;

    for (length=1; length<=11; length++){
        quotient = x / pow(10, length);
        if (quotient == 0){
            break;
        }
    }

    if ((length + 1) % 2){
        printf("length is  %d, even. \n", length);

        int j = 0;
        int mid = length / 2 - 1;
        while (j++ <= mid){
            if ( (x / pow(10, length - j - 1)) != fmod(x, pow(10, j + 1)) ){
                return false;
            }
        }
    }
    else {
        printf("length is  %d, odd. \n", length);

        int j = 0;
        int mid = length / 2;
        while (j < mid){
            int a = x / pow(10, length - j - 1);
            int b = fmod(x, pow(10, j + 1));
            printf("%d, %d, %d \n", a, b, j);
            if ( a != b){
                return false;
            }
            j++;
        }
    }

    return true;
}


int test_solution(){
    assert(true == true);
    assert(isPalindrome(0) == true);
    assert(isPalindrome(11) == true);
    assert(isPalindrome(1011) == false);
    assert(isPalindrome(543212345) == true);
    assert(isPalindrome(-11) == true);
    assert(isPalindrome(101) == true);
    return 0;
}
