/**
1. Track capacity
2. Maintain a hashamp, which stores key to node. Node is (key, val)
3. Keep left and right pointers. Left points to LRU node and right points to MRU node.
 */

class LinkNode {
    key:number
    val: number
    prev: LinkNode | null
    next: LinkNode | null
    constructor(key: number, val: number) {
        this.key = key
        this.val = val
        this.prev = null
        this.next = null
    }
}

class LRUCache {
    cap: number
    cache: any
    left: LinkNode
    right: LinkNode
    constructor(capacity: number) {
        this.cap = capacity
        this.cache = {}
        // left LRU, right MRU. Initially both point to each other
        this.left = new LinkNode(0, 0)
        this.right = new LinkNode(0, 0)
        this.left.next = this.right
        this.right.prev = this.left
    }

    /**
    1. Get prev, next nodes of current node
    2. Make prev node point to next node
    3. Make next node pont to prev node
     */
    remove(node: LinkNode): void {
        let prev = node.prev
        let nxt = node.next
        if(prev) {
            prev.next = nxt
        }
        if(nxt) {
            nxt.prev = prev
        }
    }

    /**
    1. Get right and prev from right node
    2. prev.next points to node, node.prev points to prev
    3. node.next points to right and right.prev points to node
     */
    insert(node: LinkNode): void {
        let prev = this.right.prev
        let right = this.right
        node.prev = prev
        if(prev) {
            prev.next = node
        }
        node.next = right
        right.prev = node
    }

    /**
    1. Get key from hashMap if it exists
    2. If it does not, return -1
    3. Update node to most recent used
     */
    get(key: number): number {
        if(this.cache[key] != undefined) {
            let node = this.cache[key]
            // update to most recent used
            // will remove from list
            this.remove(node)
            // will insert it at the end
            this.insert(node)
            return node.val
        }
        return -1
    }

    /**
    1. Check if key exists in cache
    2. Update the new value in cache and list
    3. Check if key length exceeds Capacity
    4. If it does, Get LRU from left pointer
    5. Remove it from the list and cache
     */
    put(key: number, value: number): void {
        if(this.cache[key] != undefined) {
            let node = this.cache[key]
            this.remove(node)
        }
        let newNode = new LinkNode(key, value)
        this.cache[key] = newNode
        this.insert(newNode)

        if(Object.keys(this.cache).length > this.cap) {
            // get left node
            let lru = this.left.next
            if(lru) {
                this.remove(lru)
                delete this.cache[lru.key]
            }
        } 
    }
}

/**
 * Your LRUCache object will be instantiated and called as such:
 * var obj = new LRUCache(capacity)
 * var param_1 = obj.get(key)
 * obj.put(key,value)
 */