fun main(){
    //immutable list
    var immlist= listOf("Apple","orange",23,3.3)
    for(item in immlist){
        println("list vlaue: $item")
    }

    //immutable set
    var immset= setOf(1,2,3,3,"one","three")
    for (value in immset){
        println("set value: $value")
    }

    //immutable map
    var immmap=mapOf(9 to "nine",7 to "seven",8 to "eight")
    for (key in immmap.keys){
        println("map value: $immmap[key]")
    }


    val name:String? ="Draj"
    if(name!=null){
        println("\n\nName: $name")
    }
    // println(name?.toUpperCase())  warning: 'toUpperCase(): String' is deprecated. Use uppercase() instead.
    println(name?.uppercase())
}