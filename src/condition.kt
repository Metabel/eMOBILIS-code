fun main() {
    val x=5
    if(x>3){
        println("$x is greater than 3")
    }
    print("what is your age? :")
    val age=readLine()?.toIntOrNull()
    if(age!=null)
    {
        if(age>=18){
            println("you are elligible to vote")
        }
        else{
            println("you are not elligible to vote")
        }
    }
    val correctusername="admin"
    val correctpassword="1234"
    println("enter a username:")
    val username=readLine()
    println("enter a password")
    var password=readLine()
    if(username==correctusername && password==correctpassword)
        println("login successfull !welcome $username")
    else{
        println("invalid username or password")
    }
}


