/*
  Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

  Find the maximum area of an island in the given 2D array. (If there is no island, the maximum area is 0.)

  Example 1:
  [[0,0,1,0,0,0,0,1,0,0,0,0,0],
  [0,0,0,0,0,0,0,1,1,1,0,0,0],
  [0,1,1,0,1,0,0,0,0,0,0,0,0],
  [0,1,0,0,1,1,0,0,1,0,1,0,0],
  [0,1,0,0,1,1,0,0,1,1,1,0,0],
  [0,0,0,0,0,0,0,0,0,0,1,0,0],
  [0,0,0,0,0,0,0,1,1,1,0,0,0],
  [0,0,0,0,0,0,0,1,1,0,0,0,0]]
  Given the above grid, return 6. Note the answer is not 11, because the island must be connected 4-directionally.
  Example 2:
  [[0,0,0,0,0,0,0,0]]
  Given the above grid, return 0.
  Note: The length of each dimension in the given grid does not exceed 50.

  ------------------------------
  ------------------------------
  ------------------------------

  1. traversing the 2D array,
    - if we meet 1, goto (2)
    - if we meet 0, continue
  2. find its neighbor by using
  3. when a number is visited, set it to 0
  (we can also create a 2D array to save visited points,
   which costs O(n) memory.)
*/

class Solution {
public:
  int maxAreaOfIsland(vector<vector<int>>& grid) {
    int maxArea = 0;
    int x_size = grid[0].size();
    int y_size = grid.size();

    for (int x=0; x<x_size; x++){
      for (int y=0; y<y_size; y++){
        if (grid[y][x] == 0){
          continue;
        }
        grid[y][x] = 0;  // set visited point to 0
        int area = 1;
        queue<pair<int, int>> q;  // pairs are a particular case of tuple
        q.push({y, x});
        while (!q.empty()){
          int y = q.front().first, x = q.front().second;
          q.pop();
          if ((x - 1) >= 0 && grid[y][x-1] != 0)
            {
              q.push({y, x-1});
              area++;
              grid[y][x-1] = 0;
            }

          if ((y - 1) >= 0 && grid[y-1][x] != 0)
            {
              q.push({y-1, x});
              area++;
              grid[y-1][x] = 0;
            }

          if ((x + 1) < x_size && grid[y][x+1] !=0)
            {
              q.push({y, x+1});
              area++;
              grid[y][x+1] = 0;
            }

          if ((y + 1) < y_size && grid[y+1][x] != 0)
            {
              q.push({y+1, x});
              area++;
              grid[y+1][x] = 0;
            }
        }
        maxArea = max(maxArea, area);
      }
    }
    return maxArea;
  }
};
