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
        if (x == -2147483648){
            return false;
        }
        x = -1 * x;
        return false;
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

    printf("length is  %d, odd. \n", length);

    int tmp = length - 1;
    while (x > 0){
        int a = x / pow(10, tmp);
        int b = fmod(x, 10);
        printf("%d, %d, %d\n", a, b, x);

        if ( a != b){
            return false;
        }
        x -= b * pow(10, tmp);
        tmp = tmp - 2;
        x = x / 10;
    }

    return true;
}


int test_solution(){
    assert(true == true);
    assert(isPalindrome(0) == true);
    assert(isPalindrome(11) == true);
    assert(isPalindrome(1011) == false);
    assert(isPalindrome(54322345) == true);
    assert(isPalindrome(543212345) == true);
    assert(isPalindrome(-2147483648) == false);
    assert(isPalindrome(-11) == false);
    assert(isPalindrome(101) == true);
    return 0;
}
