function countAndSay(n: number): string {
    if (n==1) {
        return '1' 
    }
    
    const result = countAndSay(n-1)

    let current_num = ''
    let count = 0
    let thisResult = ''
    
    for(let i=0; i< result.length; i++){
        if(current_num == result[i]){
            count++
        }else{
            if(current_num != ''){
                thisResult = thisResult + String(count)+current_num
            }

            current_num=result[i]
            count = 1
        }
    }
    
    thisResult = thisResult + String(count)+current_num

    return thisResult

};


console.log(countAndSay(4))