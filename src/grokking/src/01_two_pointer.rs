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

    pub fn compare(str1: String, str2: String) -> bool {
        fn next_valid(iter: &mut impl Iterator<Item = char>) -> Option<char> {
            let mut counter = 0;
            while let Some(c) = iter.next() {
                match c {
                    '#' => counter += 1,
                    _ if counter > 0 => counter -= 1,
                    _ => return Some(c),
                }
            }
            None
        }

        let (mut iter1, mut iter2) = (str1.chars().rev(), str2.chars().rev());
        loop {
            match (next_valid(&mut iter1), next_valid(&mut iter2)) {
                (None, None) => return true,
                (Some(c1), Some(c2)) if c1 == c2 => continue,
                _ => return false,
            }
        }
    }

    pub fn compare_stream(str1: String, str2: String) -> bool {
        fn build(s: &str) -> Vec<char> {
            let mut stack = vec![];
            s.chars().for_each(|c| {
                if c == '#' {
                    stack.pop();
                } else {
                    stack.push(c);
                }
            });
            stack
        }
        build(&str1) == build(&str2)
    }
}
