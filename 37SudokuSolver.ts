/**
 Do not return anything, modify board in-place instead.
 */
 function solveSudoku(board: string[][]): void {

//규칙을 확인하자.
//가로쪽으로 먼저 돌면서 확인
//숫자이면 해당 숫자 저장
// . 이면 기존에 나왔던 숫자가 아닌 다른 숫자로 저장
// 그리고 다시 규칙 확인
// 규칙이 어긋나면 숫자를 변경하고 다시 진행.
// 틀리면 다시 첨부터 돌림

    solve(board)
 
    console.log(board)
 };

function solve(board: string[][]): boolean {
    const width=9
    const height=9

    for(let i=0; i< width; i++){
        for(let j=0; j< height; j++){
            if (board[i][j] === '.') {
                for(let k=1; k<10; k++){
                    if(isValid(board, i,j,String(k))){
                        board[i][j]=String(k)

                        if(solve(board)){
                            return true
                        }

                        board[i][j] = '.'
                    }
                }

                return false
            }
    
        }
        
    }

    return true

}

function isValid(board: string[][], row: number, col: number, value: string): boolean {
    for(let i=0; i< 9; i++){
        if(board[row][i] === value) {
            return false
        }
        if(board[i][col] === value) {
            return false
        }
    }

    const startRow = 3*Math.floor(row/3)
    const startCol = 3*Math.floor(col/3)
    for(let i=0; i< 3; i++){
        for(let j=0; j<3; j++){
            if( board[startRow+i][startCol+j]===value){
                return false
            }
        }
    }

    return true

}

 
const boardinput = [
    ["5","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
]

solveSudoku(boardinput)
