class MinStack {
    stack: any
    min: any
    constructor() {
        this.stack = []
        this.min = null
    }

    push(val: number): void {
        if((this.min === null) || (this.min > val)) {
            this.min = val
        }
        this.stack.push([val, this.min])
    }

    pop(): void {
        this.stack.pop()
        this.min = this.stack.length > 0 ? this.stack[this.stack.length - 1][1] : null;

    }

    top(): number {
        return this.stack[this.stack.length-1][0]
    }

    getMin(): number {
        return this.stack[this.stack.length-1][1]
    }
}

/**
 * Your MinStack object will be instantiated and called as such:
 * var obj = new MinStack()
 * obj.push(val)
 * obj.pop()
 * var param_3 = obj.top()
 * var param_4 = obj.getMin()
 */