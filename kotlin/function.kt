fun addnum(n1:Double, n2:Double):Int{
    val sum=n1+n2;
    val sumInt = sum.toInt()
    return sumInt;
}
fun main(){
    val num1=12.3
    val num2=3.5
    val result:Int
    result = addnum(num1,num2)
    println("Result = $result")


    //default parameter
    display() //not argument it'll take the default values
    display('*')//first argument is *
    display('#',4)// first argument is # and second args is 4


    //lamda expression function
    val greeding={println("hey there, how are you")}
    greeding()

    val product={a:Int, b:Int -> a*b}
    val repo=product(21,9)
    println(repo)
}
fun display(Character:Char='=',length:Int=9){
    for(i in 1..length){
        print(" $Character")
    }
    println()
}
