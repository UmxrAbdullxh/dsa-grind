function topKFrequent(nums: number[], k: number): number[] {
    let freqMap: Record<string, number> = {}
    const n = nums.length
    const bucket = Array.from({length: n}, () => [])
    const result = []
    for(let n of nums) {
        freqMap[n] == undefined ? freqMap[n] = 1 : freqMap[n] = freqMap[n] + 1
    }
    for (const [key, value] of Object.entries(freqMap)) {
        bucket[value-1]?.push(key);
    }
    for(let j=bucket.length-1; j>=0; j--) {
        let temp = bucket[j]
        for(const t of temp) {
            result.push(parseInt(t))
            if(result.length == k) {
                return result
            }
        }
    }
};