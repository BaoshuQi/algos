object Solution {
     def isValid(s: String): Boolean = {
    import scala.collection.mutable.Stack
    val pair = Map("{" -> "}", "[" -> "]", "(" -> ")")
    val start = Set("(", "{", "[")
    var sk = new Stack[Char]

    for (c <- s) {
      if (start.contains(c.toString)) {
        sk.push(c)
      } else {
        if (sk.isEmpty) {
          return false
        } else {
          val last = sk.pop.toString

          if (pair(last)!= c.toString) {
            return false
          }

        }
      }

    }
    if (sk.isEmpty) {
      return true
    }
    return false


  }

}