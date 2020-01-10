pub struct Solution {}

impl Solution {
    pub fn climb_stairs(n: i32) -> i32 {
        if n <= 2{
            return n
        }
        Solution::climb_stairs(n-1) + Solution::climb_stairs(n-2)
    }
}

fn main() {
    Solution::climb_stairs(1);
}
