function lengthOfLongestSubstring(s: string): number {
    let res = 0;
    let l = 0;
    let r = 0;
    let map = new Map<string, number>();
    const getCount = (ch: string) => map.get(ch) ?? 0;
    const N = s.length - 1;
    while(r <= N) {
        while(getCount(s[r]) > 0) {
            map.set(s[l], getCount(s[l]) - 1 )
            if(getCount(s[l]) == 0) {
                map.delete(s[l])
            }
            l = l + 1
        } 
        map.set(s[r], getCount(s[r]) + 1)
        r += 1
        res = Math.max(res, r-l)
    }
    return res
};