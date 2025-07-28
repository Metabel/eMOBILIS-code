fun main() {
    println("enter a number to display the day of the week:")
    val num=readLine()?.toIntOrNull()
    when(num){
        1 -> println("Today is Monday")
        2 -> println("Today is Tuesday")
        3 -> println("Today is Wednesday")
        4 -> println("Today is Thursday")
        5 -> println("Today is Friday")
        6-> println("Today is Saturday")
        7 -> println("Today is Sunday")
        else -> println("enter a num between 1 .. 7")
    }
    println("please enter your mark:")
    val marks=readLine()?.toIntOrNull()
    if(marks!==null){
    when{
        marks >= 80 -> println("grade A")
        marks >= 70 -> println("grade B")
        marks >= 60 -> println("grade C")
        marks >= 50 -> println("grade D")
        else -> println("Fail")
    }
} else{
    print("enter a valid mark between 1 to 100")
}
}


