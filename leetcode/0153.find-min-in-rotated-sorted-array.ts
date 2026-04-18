function findMin(nums: number[]): number {
    let l = 0;
    let r = nums.length - 1
    let res = nums[0]

    while(l<=r) {
        // if left and right are already sorted
        if(nums[l] < nums[r]) {
            res = Math.min(res, nums[l])
            break
        }
        let m = Math.floor((l+r) / 2)
        res = Math.min(res, nums[m])
        // check if m in left sorted array
        if(nums[m] >= nums[l]) {
            l = m + 1
        }
        else {
            r = m - 1
        }
    }
    return res
};