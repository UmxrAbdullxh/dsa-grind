function evalRPN(tokens: string[]): number {
    const stack = []

    for(const t of tokens) {
        switch(t) {
            case "+":
                const aExp1 = stack.pop()
                const aExp2 = stack.pop()
                const aResult = parseInt(aExp1) + parseInt(aExp2)
                stack.push(aResult)
                break
            case "-":
                const subExp1 = stack.pop()
                const subExp2 = stack.pop()
                const subResult = parseInt(subExp2) - parseInt(subExp1)
                stack.push(subResult)
                break
            case "*":
                const result3 = parseInt(stack.pop()) * parseInt(stack.pop())
                stack.push(result3)
                break
            case "/":
                const dExp1 = parseInt(stack.pop())
                const dExp2 = parseInt(stack.pop())
                const dResult = Math.trunc(dExp2 / dExp1)
                stack.push(dResult)
                break
            default:
                stack.push(t)
                break;
        }
    }
    return parseInt(stack[0])
};