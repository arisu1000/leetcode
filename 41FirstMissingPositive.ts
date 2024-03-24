function firstMissingPositive(nums: number[]): number {

    let minNum = 1
    let existOne = false

    if(nums.length == 1){    
        if(nums[0] == 1){
            return 2
        }
        return 1
    }
    
    nums.sort((a, b)=>a-b)

    for(let i=0; i< nums.length; i++){
        if(nums[i] > 0) {
            if(nums[i] - minNum > 1){
                if(existOne) {
                    return minNum + 1
                }else{
                    return 1
                }
            }
                minNum = nums[i]
                if(nums[i] == 1){
                    existOne = true
                }   
        }
    }


    if(existOne){
        return minNum + 1
    }else{
        return 1
    }

};

console.log(firstMissingPositive([0]), 1)
console.log(firstMissingPositive([2]), 1)
console.log(firstMissingPositive([2, 2]), 1)
console.log(firstMissingPositive([2, 2, 4]), 1)
console.log(firstMissingPositive([1,2,0]), 3)
console.log(firstMissingPositive([3,4,-1,1]), 2)
console.log(firstMissingPositive([7,8,9,11,12]), 1)