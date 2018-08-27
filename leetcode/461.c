#include <stdio.h>


int hammingDistance(int x, int y);

int main()
{
    int dis;
    dis = hammingDistance(1, 4);
    printf("dis: %d\n", dis);
    return dis;
}

int
hammingDistance(int x, int y)
{
    int z = x ^ y;
    int dis = 0;
    while (z > 0){
        if ((z & 1) == 1)
            dis++;
        z = z >> 1;
    }
    return dis;
}
