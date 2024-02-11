type MinStack struct {
    arr []int
}


func Constructor() MinStack {
    return MinStack{
        arr: []int{},
    }
}

func (this *MinStack) Push(val int)  {
    this.arr = append(this.arr, val);
}


func (this *MinStack) Pop()  {
    index := len(this.arr)
    this.arr = append(this.arr[:index-1], this.arr[index:]...)
}


func (this *MinStack) Top() int {
    return this.arr[len(this.arr)-1]
}


func (this *MinStack) GetMin() int {
    i := this.arr[0]
    for _, num := range this.arr {
        if num < i {
            i = num
        }
    }
    return i
}


/**
 * Your MinStack object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Push(val);
 * obj.Pop();
 * param_3 := obj.Top();
 * param_4 := obj.GetMin();
 */