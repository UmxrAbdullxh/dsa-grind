function threeSum(nums: number[]): number[][] {
    const result = []
    const map = {}
    nums.sort((a, b) => a - b); 

    for(let i=0; i<nums.length; i++){
        let l = i+1;
        let r = nums.length -1

        while(l<r) {
            let temp = nums[i] + nums[l] + nums[r]
            if(temp < 0) {
                l += 1
            }
            else if(temp > 0) {
                r -= 1
            }
            else {
                let res = [nums[i], nums[l], nums[r]]
                const mapKey = `${nums[i]},${nums[l]},${nums[r]}`; 
                if(map[mapKey] === undefined) {
                    map[mapKey] = 1
                    result.push(res)
                }

                l += 1
            }

        }
    }
    return result
};