function solution(n){
    let count3x = 0
    while (n > 0) {
        count3x++
        if (count3x.toString().includes('3')){
            continue
        }
        if (count3x % 3 == 0) {
            continue
        }
        n--
    }
    return count3x
}