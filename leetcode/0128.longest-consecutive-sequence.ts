function longestConsecutive(nums: number[]): number {
    const numset = new Set(nums);
    let result = 1
    for(let n of numset) {
        if(!nums.includes(n-1)) {
            let count = 0
            while(nums.includes(n)) {
                count += 1
                n += 1
            }
            if(count > result ) {
                result = count
            }
        }
    }
    result = (nums.length>0) ? result : 0;
    return result 
};