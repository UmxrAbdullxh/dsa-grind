function groupAnagrams(strs: string[]): string[][] {

    const anagramMap:any = {}
    for(let s of strs) {
        const sorted = s.split('').sort().join('');
        if(anagramMap[sorted] === undefined) {
            anagramMap[sorted] = [s]
        } 
        else {
            anagramMap[sorted].push(s)
        }
    }
    
    return Object.values(anagramMap)
    
};