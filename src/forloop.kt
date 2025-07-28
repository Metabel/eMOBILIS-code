fun main() {
    val students = listOf("sam","alex","patricia","elizabeth")
    // loop through a list
    for (x in students) {
        println(x)
    }

    // looping through an array
    val fruits = arrayOf("mangoes","apples","oranges")
    for (fruit in fruits) {
        println(fruit)
    } // closes the for loop



        // loop from 2 until 10
        for (a in 2 until 10) {
            println("The number is $a")
        }

        // loop with step and break
        for (z in 1 until 10 step 1) {
            if (z == 5) break
            println("$z")
        }
    }







