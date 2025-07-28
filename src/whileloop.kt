fun main (){
    var z=5
    do{
        println("the value of z is $z")
        z++
    }while(z<=10)
    var pin: String
    do{
        println("enter a four digit pin:")
        pin= readln()
    }while(pin.length!=4 &&pin.toIntOrNull()==null)
    println("pin accepted")
}