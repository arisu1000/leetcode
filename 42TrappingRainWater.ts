function trap(height: number[]): number {


    //0이 아닌게 처음 나올때까지 확인
    //그 다음 부터는 높낮이를 체크한다.

    //저장해두고 그 다음부터 낮아지는지 확인
    //낮아지면 물 높이 체크 시작으로 인식한다.
    //다시 높아질때까지 확인.
    //높아지는건 왼쪽벽의 높이 이상이 될때까지 기다린다.
    //x,y를 확인해서 담긴 물 확인.

    //낮아질때도 쌍이 맞으면 물은 고인다.

    // const checkLeftPositionAndHeight = [0, 0]
    // const checkRightPositionAndHeight = [0, 0]
    // for(let i=0; i< height.length; i++){
    //     if(height[i] >= checkLeftPositionAndHeight[1]){
    //         checkLeftPositionAndHeight[0] = i
    //         checkLeftPositionAndHeight[1] = height[i]
    //     }
        

    //     if(i > 0 &&  height[i-1] < height[i]){
    //         checkRightPositionAndHeight[0] = i
    //         checkRightPositionAndHeight[1] = height[i]
    //     }
    //     console.log('left, right',checkLeftPositionAndHeight, checkRightPositionAndHeight)
    // }

    // return 0

    let left = 0;
    let right = height.length - 1;
    let leftMax = 0;
    let rightMax = 0;
    let waterTrapped = 0;
  
    while (left < right) {
      if (height[left] < height[right]) {
        if (height[left] > leftMax) {
          leftMax = height[left];
        } else {
          waterTrapped += leftMax - height[left];
        }
        left++;
      } else {
        if (height[right] > rightMax) {
          rightMax = height[right];
        } else {
          waterTrapped += rightMax - height[right];
        }
        right--;
      }
    }
  
    return waterTrapped;
};


console.log(trap([0,1,0,2,1,0,1,3,2,1,2,1]), 6)