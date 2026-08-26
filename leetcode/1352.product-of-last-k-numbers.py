class ProductOfNumbers:

    def __init__(self):
        self.product = []
        self.original = []
        self.zeroth_index = -1
        

    def add(self, num: int) -> None:
        self.original.append(num)
        len_product = len(self.product)
        if num == 0:
            if len_product <= 0:
                self.product.append(1)
            else:
                last_element = self.product[len_product-1]
                prefix = last_element * 1
                self.product.append(prefix)
            self.zeroth_index = len(self.product)-1
            return
        if len_product == 0:
            self.product.append(num)
        else:
            last_element = self.product[len_product-1]
            prefix = last_element * num
            self.product.append(prefix)

             
        

    def getProduct(self, k: int) -> int:
        len_original = len(self.original)-1
        len_prefix = len(self.product)-1
        diff = len_original - k
        if diff < self.zeroth_index:
            return 0
        if diff < 0:
            return self.product[len_prefix]
        productOfNumbers = self.product[len_prefix] // self.product[diff]
        return productOfNumbers if diff >= self.zeroth_index else 0
        


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)