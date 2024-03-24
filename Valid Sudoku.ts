function isValidSudoku(board: string[][]): boolean {
    const width=9
    const height=9


const box1 = {}
const box2 = {}
const box3 = {}
const box4 = {}
const box5 = {}
const box6 = {}
const box7 = {}
const box8 = {}
const box9 = {}

    for(let i=0; i<width; i++){
        const checkMemo1 = {}
        const checkMemo2 = {}
        for(let j=0; j<height; j++){
            //가로체크
            if (checkMemo1[board[i][j]] != undefined && board[i][j] != '.'){
                // console.log(i, j, board[i][j],checkMemo1[board[i][j]])
                return false
            }
            checkMemo1[board[i][j]] = true
          
            //세로체크
            if (checkMemo2[board[j][i]] != undefined && board[j][i] != '.'){
                // console.log(i, j, board[i][j],checkMemo2[board[j][i]])
                return false
            }
            checkMemo2[board[j][i]] = true


            //작은 사각형 구역 체크
            if(0<= i && i<=2 && 0<=j && j<=2){
                if (box1[board[i][j]] != undefined && board[i][j] != '.'){
                    console.log(i, j, board[i][j], box1[board[i][j]])
                    return false
                }
                box1[board[i][j]] = true
            }

            if(0<= i && i<=2 && 3<=j && j<=5){
                if (box2[board[i][j]] != undefined && board[i][j] != '.'){
                    console.log(i, j, board[i][j], box2[board[i][j]])
                    return false
                }
                box2[board[i][j]] = true
            }

            if(0<= i && i<=2 && 6<=j && j<=8){
                if (box3[board[i][j]] != undefined && board[i][j] != '.'){
                    console.log(i, j, board[i][j], box3[board[i][j]])
                    return false
                }
                box3[board[i][j]] = true
            }

            if(3<= i && i<=5 && 0<=j && j<=2){
                if (box4[board[i][j]] != undefined && board[i][j] != '.'){
                    console.log(i, j, board[i][j], box4[board[i][j]])
                    return false
                }
                box4[board[i][j]] = true
            }

            if(3<= i && i<=5 && 3<=j && j<=5){
                if (box5[board[i][j]] != undefined && board[i][j] != '.'){
                    console.log(i, j, board[i][j], box5[board[i][j]])
                    return false
                }
                box5[board[i][j]] = true
            }

            if(3<= i && i<=5 && 6<=j && j<=8){
                if (box6[board[i][j]] != undefined && board[i][j] != '.'){
                    console.log(i, j, board[i][j], box6[board[i][j]])
                    return false
                }
                box6[board[i][j]] = true
            }

            if(6<= i && i<=8 && 0<=j && j<=2){
                if (box7[board[i][j]] != undefined && board[i][j] != '.'){
                    console.log(i, j, board[i][j], box7[board[i][j]])
                    return false
                }
                box7[board[i][j]] = true
            }

            if(6<= i && i<=8 && 3<=j && j<=5){
                if (box8[board[i][j]] != undefined && board[i][j] != '.'){
                    console.log(i, j, board[i][j], box8[board[i][j]])
                    return false
                }
                box8[board[i][j]] = true
            }

            if(6<= i && i<=8 && 6<=j && j<=8){
                if (box9[board[i][j]] != undefined && board[i][j] != '.'){
                    console.log(i, j, board[i][j], box9[board[i][j]])
                    return false
                }
                box9[board[i][j]] = true
            }

        }
        
    }

    return true
};

const board = 
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

console.log(isValidSudoku(board))