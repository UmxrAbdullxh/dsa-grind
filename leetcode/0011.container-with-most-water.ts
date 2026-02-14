function maxArea(height: number[]): number {
    let result = 0
    let l = 0
    let r = height.length - 1
    while(l<r) {
        let length = r -l
        let breadth = Math.min(height[l], height[r])
        let area = length * breadth
        result = Math.max(result, area)
        if(height[l] < height[r]) {
            l += 1
        }
        else {
            r -= 1
        }
    }
    return result
};