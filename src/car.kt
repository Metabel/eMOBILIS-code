class Car {
    //properties
    var color:String=""
    var model:String=""
    var brand:String=""
    var topspeed:Int=0
    //method to display car details
    fun displayinfo(){
        println("The car is:brand $brand of model: $model,color: $color, topspeed: $topspeed")
    }
}
fun main(){
    //creating an object
    val car1=Car()
    car1.color="white"
    car1.model="Demio"
    car1.brand="Mazda"
    car1.topspeed=200

    car1.displayinfo()

    }

