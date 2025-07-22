pub struct Solution;

impl Solution {
    pub fn sort_colors(nums: &mut Vec<i32>) {
        let (mut mid, mut high) = (0, 0);
        let mut i = 0;
        while i < nums.len() {
            match nums[i] {
                0 => {
                    nums.swap(i, high);
                    nums.swap(mid, high);
                    mid += 1;
                    high += 1;
                    i += 1;
                }
                1 => {
                    nums.swap(i, high);
                    high += 1;
                    i += 1;
                }
                _ => {
                    i += 1;
                }
            }
        }
    }

    pub fn sort_colors_2(nums: &mut Vec<i32>) {
        let (mut low, mut mid, mut high) = (0, 0, nums.len() as usize - 1);
        while mid <= high {
            match nums[mid] {
                0 => {
                    nums.swap(mid, low);
                    low += 1;
                    mid += 1;
                }
                1 => {
                    mid += 1;
                }
                2 => {
                    nums.swap(mid, high);
                    if high == 0 {
                        break;
                    }
                    high -= 1;
                }
                _ => {}
            }
        }
    }
}
