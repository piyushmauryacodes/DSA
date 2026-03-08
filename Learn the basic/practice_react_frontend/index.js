// function abc(a,...b){
//     console.log(a)
//     console.log(...b)
// }

// abc(2,34,32,53,23)

str1="Piyush"
str2="s"

function abc(str1, str2){
    new_str=""
    min=Math.min(str1.length, str2.length)
    for (let i = 0; i < min; i++) {  
        new_str+=str1[i]+ str2[i]
    }
    return new_str + str1.slice(min) + str2.slice(min)
}

console.log(abc(str1, str2))