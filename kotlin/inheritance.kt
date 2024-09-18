open class myParentClass{
    val x=5
}
class myClildClass : myParentClass(){
    fun myfunction(){
        print(x)
    }
}
fun main(){
    val myobj=myClildClass()
    myobj.myfunction()
}