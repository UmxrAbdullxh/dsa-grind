function dailyTemperatures(temperatures: number[]): number[] {
    const result = new Array(temperatures.length).fill(0)
    const stack = []

    for(let i=0; i<temperatures.length; i++) {
        if(stack.length == 0) {
            stack.push([temperatures[i], i])
        } else {
            while(stack.length && (stack[stack.length-1][0] < temperatures[i]) ) {
                let element = stack.pop()
                let prevIndex = element[1]
                let sub = i - prevIndex
                result[prevIndex] = sub
            }
            stack.push([temperatures[i], i])
        }
    }
    return result
};