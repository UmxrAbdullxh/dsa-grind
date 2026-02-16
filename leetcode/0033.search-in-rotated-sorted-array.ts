function search(nums: number[], target: number): number {
    let low = 0
    let high = nums.length - 1

    while(low<=high) {
        let mid = Math.floor((low+high) / 2)
        if(nums[mid] == target) {
            return mid
        }
        /**
        Mental Model:
        1. Check if left half is sorted by nums[low] <= nums[mid]
        2. If it is, then check if number lies in that range by nums[low] <= target and nums[mid] >= target. If is is, go left. Else go right
        3. Check if target lies in right by checking target >= nums[mid] and target <= nums[high]. Go right in this scenario, else go left.
         */
        if(nums[low] <= nums[mid]) {
            if(nums[low] <= target && nums[mid] > target) {
                high = high - 1
            }
            else {
                low = low + 1
            }
        }
        else {
            if(nums[mid] < target && nums[high] >= target) {
                low = low + 1
            }
            else {
                high = high - 1
            }
        }
    }
    return -1
};