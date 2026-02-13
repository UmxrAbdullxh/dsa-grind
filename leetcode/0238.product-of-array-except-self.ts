function productExceptSelf(nums: number[]): number[] {
    const n = nums.length;
    const result = new Array(n).fill(1);
    let prefix = 1
    let suffix = 1
    
    for(let i=0; i<n; i++) {
        result[i] = prefix
        prefix = prefix*nums[i]
    }

    for(let j=n-1;j>=0;j--) {
        result[j] = result[j]*suffix
        suffix = suffix*nums[j]
    }
    return result
};